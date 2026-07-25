from __future__ import annotations

from dataclasses import dataclass

import httpx

from invoker.http.ratelimit import TokenBucket
from invoker.logging import get_logger

logger = get_logger(__name__)

BATCH_SIZE = 20


class MediaWikiError(RuntimeError):
    pass


@dataclass(frozen=True)
class PageRevision:
    requested_title: str
    resolved_title: str
    page_id: int
    revision_id: int
    revision_timestamp: str
    content: str


@dataclass(frozen=True)
class MissingPage:
    requested_title: str
    reason: str


class MediaWikiClient:
    """Rate-limited MediaWiki `action=query` client for revision-pinned page fetches.

    capacity=1 on the bucket enforces a strict gap between requests instead of
    allowing bursts; wiki hosts (Liquipedia in particular) ask for spaced calls.
    """

    def __init__(
        self,
        api_url: str,
        *,
        user_agent: str,
        requests_per_minute: int = 20,
        parse_requests_per_minute: int = 2,
        timeout: float = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.api_url = api_url
        self.bucket = TokenBucket(rate=requests_per_minute / 60.0, capacity=1)
        self.parse_bucket = TokenBucket(rate=parse_requests_per_minute / 60.0, capacity=1)
        self._client = httpx.AsyncClient(
            headers={"User-Agent": user_agent},
            timeout=timeout,
            transport=transport,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def fetch_revisions(
        self, titles: list[str]
    ) -> tuple[list[PageRevision], list[MissingPage]]:
        revisions: list[PageRevision] = []
        missing: list[MissingPage] = []
        for start in range(0, len(titles), BATCH_SIZE):
            chunk = titles[start : start + BATCH_SIZE]
            payload = await self._query(chunk)
            chunk_revisions, chunk_missing = _parse_query(chunk, payload)
            revisions.extend(chunk_revisions)
            missing.extend(chunk_missing)
        return revisions, missing

    async def list_category_members(self, category: str) -> list[str]:
        """Return all page titles in a category (pages only, paginated)."""
        titles: list[str] = []
        continue_token: str | None = None
        while True:
            params = {
                "action": "query",
                "format": "json",
                "formatversion": "2",
                "list": "categorymembers",
                "cmtitle": category,
                "cmtype": "page",
                "cmlimit": "500",
            }
            if continue_token is not None:
                params["cmcontinue"] = continue_token
            payload = await self._get(params, log_context=f"category={category}")
            members = payload["query"].get("categorymembers", [])
            titles.extend(member["title"] for member in members)
            continue_token = payload.get("continue", {}).get("cmcontinue")
            if continue_token is None:
                return titles

    async def fetch_expanded_html(self, revision_id: int) -> str:
        """Template-expanded HTML for an exact pinned revision (action=parse).

        Values computed by wiki templates (e.g. {{G|...}} globals) only exist
        in expanded output, not in raw wikitext. Parse calls use their own,
        much stricter rate bucket."""
        params = {
            "action": "parse",
            "format": "json",
            "formatversion": "2",
            "oldid": str(revision_id),
            "prop": "text",
        }
        await self.parse_bucket.acquire()
        logger.info("MediaWiki parse api=%s oldid=%d", self.api_url, revision_id)
        response = await self._client.get(self.api_url, params=params)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise MediaWikiError(f"unexpected MediaWiki parse response from {self.api_url}")
        parse = payload.get("parse")
        if not isinstance(parse, dict) or not isinstance(parse.get("text"), str):
            error = payload.get("error", {})
            detail = error.get("info") if isinstance(error, dict) else None
            raise MediaWikiError(
                f"parse failed for oldid={revision_id} on {self.api_url}"
                + (f": {detail}" if detail else "")
            )
        return parse["text"]

    async def _query(self, titles: list[str]) -> dict:
        params = {
            "action": "query",
            "format": "json",
            "formatversion": "2",
            "prop": "revisions",
            "rvprop": "ids|timestamp|content",
            "rvslots": "main",
            "redirects": "1",
            "titles": "|".join(titles),
        }
        return await self._get(params, log_context=f"titles={len(titles)}")

    async def _get(self, params: dict[str, str], *, log_context: str) -> dict:
        await self.bucket.acquire()
        logger.info("MediaWiki query api=%s %s", self.api_url, log_context)
        response = await self._client.get(self.api_url, params=params)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict) or "query" not in payload:
            raise MediaWikiError(f"unexpected MediaWiki response shape from {self.api_url}")
        return payload


def _parse_query(
    requested_titles: list[str], payload: dict
) -> tuple[list[PageRevision], list[MissingPage]]:
    query = payload["query"]
    forward = {title: title for title in requested_titles}
    for step in ("normalized", "redirects"):
        for entry in query.get(step, []):
            for requested, current in forward.items():
                if current == entry.get("from"):
                    forward[requested] = entry["to"]

    by_resolved: dict[str, list[str]] = {}
    for requested, resolved in forward.items():
        by_resolved.setdefault(resolved, []).append(requested)

    revisions: list[PageRevision] = []
    missing: list[MissingPage] = []
    for page in query.get("pages", []):
        title = page.get("title", "")
        requested_for_page = by_resolved.get(title, [title])
        if page.get("missing") or page.get("invalid"):
            reason = "invalid" if page.get("invalid") else "missing"
            missing.extend(
                MissingPage(requested_title=requested, reason=reason)
                for requested in requested_for_page
            )
            continue
        page_revisions = page.get("revisions") or []
        if not page_revisions:
            missing.extend(
                MissingPage(requested_title=requested, reason="no_revision")
                for requested in requested_for_page
            )
            continue
        revision = page_revisions[0]
        content = revision.get("slots", {}).get("main", {}).get("content")
        if content is None:
            missing.extend(
                MissingPage(requested_title=requested, reason="no_content")
                for requested in requested_for_page
            )
            continue
        for requested in requested_for_page:
            revisions.append(
                PageRevision(
                    requested_title=requested,
                    resolved_title=title,
                    page_id=page["pageid"],
                    revision_id=revision["revid"],
                    revision_timestamp=revision["timestamp"],
                    content=content,
                )
            )
    return revisions, missing
