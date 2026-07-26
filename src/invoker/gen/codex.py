from __future__ import annotations

import hashlib
import json
import queue
import shutil
import subprocess
import tempfile
import threading
from collections.abc import Callable
from datetime import UTC, datetime
from typing import Protocol, TypeVar

from pydantic import BaseModel, ValidationError

from invoker.gen.client import (
    GenerationError,
    GenerationProvenance,
    GenerationResult,
    StructuredResult,
)

CODEX_GENERATION_MODEL = "gpt-5.6-sol"
CODEX_TRANSPORT = "codex-app-server"
_RECEIVE_TIMEOUT = 900.0

T = TypeVar("T", bound=BaseModel)


class AppServerTransport(Protocol):
    """Line-oriented stdio to one `codex app-server` daemon."""

    def send_line(self, line: str) -> None: ...

    def receive_line(self, timeout: float) -> str: ...

    def close(self) -> None: ...


class _AppServerProcess:
    """The real transport: owns the daemon subprocess. A reader thread
    feeds a queue so receive timeouts work without select-on-buffered-pipe
    pitfalls (the server writes notification bursts in one flush)."""

    def __init__(self, codex_bin: str) -> None:
        self._proc = subprocess.Popen(
            [codex_bin, "app-server"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        self._lines: queue.Queue[str | None] = queue.Queue()
        self._reader = threading.Thread(target=self._read, daemon=True)
        self._reader.start()

    def _read(self) -> None:
        assert self._proc.stdout is not None
        for line in self._proc.stdout:
            self._lines.put(line)
        self._lines.put(None)

    def send_line(self, line: str) -> None:
        stdin = self._proc.stdin
        assert stdin is not None
        try:
            stdin.write(line + "\n")
            stdin.flush()
        except (BrokenPipeError, OSError) as exc:
            raise GenerationError("codex app-server stdin closed; daemon died") from exc

    def receive_line(self, timeout: float) -> str:
        try:
            line = self._lines.get(timeout=timeout)
        except queue.Empty as exc:
            raise GenerationError(f"codex app-server sent nothing for {timeout:.0f}s") from exc
        if line is None:
            raise GenerationError("codex app-server exited unexpectedly")
        return line

    def close(self) -> None:
        self._proc.terminate()
        try:
            self._proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self._proc.kill()


def _spawn_app_server(codex_bin: str = "codex") -> AppServerTransport:
    return _AppServerProcess(codex_bin)


class CodexClient:
    """Generation backend over the `codex app-server` JSON-RPC daemon
    (user's Codex/ChatGPT token budget; protocol pinned against
    codex-cli 0.145.0).

    Same result/provenance surface as ClaudeCliClient. Each call runs on a
    fresh ephemeral thread whose baseInstructions replace the harness
    system prompt; the sandbox is read-only with approvals disabled and an
    empty working directory, so no tool runs and no AGENTS.md leaks into
    the prompt. Structured outputs use the server's native outputSchema
    constraint and are still validated client-side — a bad payload raises
    instead of degrading (project hard line). Token counts are recorded as
    the server reports them, or None when it reports none.
    """

    def __init__(
        self,
        *,
        model: str = CODEX_GENERATION_MODEL,
        spawn: Callable[[], AppServerTransport] = _spawn_app_server,
    ) -> None:
        self.model = model
        self._spawn = spawn
        self._transport: AppServerTransport | None = None
        self._next_id = 0
        self._cwd: str | None = None

    def generate(
        self,
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        effort: str | None = None,
    ) -> GenerationResult:
        text, served_model, usage, status = self._run_turn(
            prompt_name, system, user_content, effort, output_schema=None
        )
        if not text.strip():
            raise GenerationError(f"{prompt_name}: codex returned no text")
        return GenerationResult(
            text=text,
            provenance=self._provenance(
                prompt_name, prompt_version, system, user_content, None,
                served_model, usage, status,
            ),
        )

    def generate_structured(
        self,
        output_type: type[T],
        *,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        effort: str | None = None,
    ) -> StructuredResult[T]:
        schema = output_type.model_json_schema()
        text, served_model, usage, status = self._run_turn(
            prompt_name, system, user_content, effort, output_schema=schema
        )
        try:
            output = output_type.model_validate_json(text)
        except ValidationError as exc:
            raise GenerationError(
                f"{prompt_name}: codex output does not validate as "
                f"{output_type.__name__}: {exc}"
            ) from exc
        return StructuredResult(
            output=output,
            provenance=self._provenance(
                prompt_name, prompt_version, system, user_content, schema,
                served_model, usage, status,
            ),
        )

    def close(self) -> None:
        if self._transport is not None:
            self._transport.close()
            self._transport = None
        if self._cwd is not None:
            shutil.rmtree(self._cwd, ignore_errors=True)
            self._cwd = None

    def __enter__(self) -> CodexClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    # -- one call = initialize (once) + ephemeral thread + one turn --------

    def _run_turn(
        self,
        prompt_name: str,
        system: str,
        user_content: str,
        effort: str | None,
        output_schema: dict | None,
    ) -> tuple[str, str, dict, str]:
        """Returns (text, served model, usage breakdown, turn status).
        Any mid-call error tears the daemon down so the next call starts
        clean — a restart is transport management, not a retry."""
        try:
            self._ensure_started()
            thread_id, served_model = self._start_thread(prompt_name, system)
            turn_params: dict = {
                "threadId": thread_id,
                "input": [{"type": "text", "text": user_content}],
            }
            if effort is not None:
                turn_params["effort"] = effort
            if output_schema is not None:
                turn_params["outputSchema"] = output_schema
            turn = self._request("turn/start", turn_params, prompt_name)
            turn_id = turn["turn"]["id"]
            return self._collect_turn(prompt_name, thread_id, turn_id, served_model)
        except GenerationError:
            self.close()
            raise

    def _ensure_started(self) -> None:
        if self._transport is not None:
            return
        self._cwd = tempfile.mkdtemp(prefix="invoker-codex-")
        self._transport = self._spawn()
        self._request(
            "initialize",
            {"clientInfo": {"name": "invoker", "version": "0"}},
            "initialize",
        )

    def _start_thread(self, prompt_name: str, system: str) -> tuple[str, str]:
        result = self._request(
            "thread/start",
            {
                "ephemeral": True,
                "model": self.model,
                "baseInstructions": system,
                "approvalPolicy": "never",
                "sandbox": "read-only",
                "cwd": self._cwd,
                "config": {"mcp_servers": {}},
            },
            prompt_name,
        )
        served_model = result.get("model")
        if not served_model:
            raise GenerationError(
                f"{prompt_name}: thread/start reported no model; "
                "refusing to record unknown provenance"
            )
        if served_model != self.model:
            raise GenerationError(
                f"{prompt_name}: requested model {self.model!r} but the thread "
                f"resolved to {served_model!r}; refusing the substitution"
            )
        return result["thread"]["id"], served_model

    def _collect_turn(
        self,
        prompt_name: str,
        thread_id: str,
        turn_id: str,
        served_model: str,
    ) -> tuple[str, str, dict, str]:
        texts: list[str] = []
        usage: dict = {}
        while True:
            msg = self._receive(prompt_name)
            if "id" in msg and "method" in msg:
                raise GenerationError(
                    f"{prompt_name}: codex sent a server request "
                    f"({msg['method']}) — tool use under a no-tools contract"
                )
            method = msg.get("method")
            params = msg.get("params") or {}
            if method == "model/rerouted" and params.get("threadId") == thread_id:
                raise GenerationError(
                    f"{prompt_name}: model rerouted {params.get('fromModel')!r} -> "
                    f"{params.get('toModel')!r} ({params.get('reason')}); "
                    "refusing the substitution"
                )
            if method == "item/completed" and params.get("turnId") == turn_id:
                item = params.get("item") or {}
                if item.get("type") == "agentMessage":
                    texts.append(str(item.get("text") or ""))
            if method == "thread/tokenUsage/updated" and params.get("turnId") == turn_id:
                usage = (params.get("tokenUsage") or {}).get("last") or {}
            if method == "turn/completed" and (params.get("turn") or {}).get("id") == turn_id:
                turn = params["turn"]
                status = str(turn.get("status"))
                if status != "completed":
                    error = turn.get("error") or {}
                    raise GenerationError(
                        f"{prompt_name}: codex turn {status}: "
                        f"{error.get('message', 'no error detail')}"
                    )
                return "\n".join(texts), served_model, usage, status

    # -- JSON-RPC plumbing -------------------------------------------------

    def _request(self, method: str, params: dict, prompt_name: str) -> dict:
        transport = self._transport
        assert transport is not None
        self._next_id += 1
        request_id = self._next_id
        transport.send_line(
            json.dumps({"jsonrpc": "2.0", "id": request_id, "method": method, "params": params})
        )
        while True:
            msg = self._receive(prompt_name)
            if msg.get("id") == request_id and "method" not in msg:
                if "error" in msg:
                    raise GenerationError(
                        f"{prompt_name}: codex {method} failed: "
                        f"{msg['error'].get('message', msg['error'])}"
                    )
                return msg.get("result") or {}
            # Notifications between request and response carry nothing a
            # fresh ephemeral thread needs; turn traffic is read in
            # _collect_turn after turn/start returns.

    def _receive(self, prompt_name: str) -> dict:
        transport = self._transport
        assert transport is not None
        line = transport.receive_line(_RECEIVE_TIMEOUT).strip()
        if not line:
            return {}
        try:
            return json.loads(line)
        except json.JSONDecodeError as exc:
            raise GenerationError(
                f"{prompt_name}: codex app-server emitted non-JSON: {line[:200]}"
            ) from exc

    def _provenance(
        self,
        prompt_name: str,
        prompt_version: str,
        system: str,
        user_content: str,
        output_schema: dict | None,
        served_model: str,
        usage: dict,
        status: str,
    ) -> GenerationProvenance:
        fingerprint_fields: dict = {
            "requested_model": self.model,
            "system": system,
            "messages": [{"role": "user", "content": user_content}],
            "prompt": f"{prompt_name}@{prompt_version}",
        }
        if output_schema is not None:
            fingerprint_fields["output_schema"] = output_schema
        fingerprint = json.dumps(fingerprint_fields, sort_keys=True)
        input_tokens = usage.get("inputTokens")
        output_tokens = usage.get("outputTokens")
        return GenerationProvenance(
            model=served_model,
            transport=CODEX_TRANSPORT,
            prompt_name=prompt_name,
            prompt_version=prompt_version,
            request_sha256=hashlib.sha256(fingerprint.encode()).hexdigest(),
            input_tokens=int(input_tokens) if input_tokens is not None else None,
            output_tokens=int(output_tokens) if output_tokens is not None else None,
            stop_reason=status,
            generated_at=datetime.now(UTC).isoformat(),
        )
