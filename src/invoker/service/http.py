from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, urlparse

from invoker.service.core import KnowledgeService, KnowledgeServiceError


def handle_http_request(
    service: KnowledgeService,
    *,
    method: str,
    path: str,
    body: bytes = b"",
) -> tuple[int, dict[str, Any]]:
    parsed = urlparse(path)
    name = parsed.path.strip("/")
    params = _query_params(parsed.query)
    try:
        payload = _json_body(body)
        args = {**params, **payload}
        result = _dispatch(service, method.upper(), name, args)
    except KnowledgeServiceError as exc:
        return exc.status_code, {
            "error": {"code": exc.code, "message": exc.message, "details": exc.details}
        }
    except (KeyError, TypeError, ValueError) as exc:
        return 400, {"error": {"code": "bad_request", "message": str(exc), "details": {}}}
    return 200, result


def make_handler(service: KnowledgeService) -> type[BaseHTTPRequestHandler]:
    class KnowledgeRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            self._handle()

        def do_POST(self) -> None:
            self._handle()

        def log_message(self, format: str, *args: Any) -> None:
            return

        def _handle(self) -> None:
            length = int(self.headers.get("Content-Length") or "0")
            status, payload = handle_http_request(
                service,
                method=self.command,
                path=self.path,
                body=self.rfile.read(length) if length else b"",
            )
            raw = json.dumps(payload, indent=2).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

    return KnowledgeRequestHandler


def serve(service: KnowledgeService, *, host: str, port: int) -> None:
    server = ThreadingHTTPServer((host, port), make_handler(service))
    server.serve_forever()


def _dispatch(
    service: KnowledgeService,
    method: str,
    name: str,
    args: dict[str, Any],
) -> dict[str, Any]:
    if method not in {"GET", "POST"}:
        raise KnowledgeServiceError(
            "method_not_allowed",
            f"method {method} is not supported",
            status_code=405,
        )
    if name == "list_bundle_patches":
        return service.list_bundle_patches()
    if name == "lookup_hero":
        return service.lookup_hero(args["query"], patch=args.get("patch"))
    if name == "get_hero_constants":
        return service.get_hero_constants(args["hero"], patch=args.get("patch"))
    if name == "kb_catalog":
        return service.kb_catalog(patch=args.get("patch"), kind=args.get("kind"))
    if name == "kb_resolve":
        return service.kb_resolve(args["query"], patch=args.get("patch"))
    if name == "kb_card":
        return service.kb_card(args["id"], patch=args.get("patch"))
    if name == "kb_article":
        return service.kb_article(args["id"], patch=args.get("patch"))
    if name == "search_changelog":
        return service.search_changelog(
            grep=args.get("grep"),
            entity=args.get("entity"),
            note_patch=args.get("note_patch"),
            patch=args.get("patch"),
        )
    if name == "resolve_team":
        return service.resolve_team(args["query"], patch=args.get("patch"))
    if name == "resolve_player":
        return service.resolve_player(args["query"], team=args.get("team"), patch=args.get("patch"))
    if name == "get_team_profile":
        return service.get_team_profile(args["team"], patch=args.get("patch"))
    if name == "get_team_roster":
        return service.get_team_roster(args["team"], patch=args.get("patch"))
    if name == "get_team_hero_pool":
        return service.get_team_hero_pool(args["team"], patch=args.get("patch"))
    if name == "get_team_player_hero_pool":
        return service.get_team_player_hero_pool(
            args["team"], args["player"], patch=args.get("patch")
        )
    raise KnowledgeServiceError(
        "route_not_found",
        f"unknown knowledge route: /{name}",
        status_code=404,
    )


def _json_body(body: bytes) -> dict[str, Any]:
    if not body:
        return {}
    raw = json.loads(body.decode("utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("request JSON body must be an object")
    return raw


def _query_params(query: str) -> dict[str, str]:
    return {
        key: values[-1]
        for key, values in parse_qs(query).items()
        if values
    }
