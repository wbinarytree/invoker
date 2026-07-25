from __future__ import annotations

import asyncio
from collections.abc import Callable
from dataclasses import dataclass, field

import httpx

from invoker.corpus.fetch import USER_AGENT, CorpusFetchError
from invoker.corpus.mediawiki import MediaWikiClient, MediaWikiError
from invoker.corpus.schemas import CorpusHost, CorpusRegistry
from invoker.corpus.store import CorpusStore

ProgressCallback = Callable[[str, str], None]


@dataclass
class HostExpandReport:
    """Outcome of one host's expanded-text pass over the fetch index."""

    host_key: str
    expanded: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    failed: list[tuple[str, str]] = field(default_factory=list)


async def expand_host_corpus(
    host_key: str,
    host: CorpusHost,
    store: CorpusStore,
    *,
    limit: int | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
    progress: ProgressCallback | None = None,
) -> HostExpandReport:
    """Fetch template-expanded HTML for every indexed page revision that does
    not have it yet. Iterates the fetch index (resolved pages), so run
    fetch-corpus first. Parse calls are slow by design (strict rate limit);
    the pass is incremental — an already-expanded revision is never
    re-fetched."""
    report = HostExpandReport(host_key=host_key)
    index = store.load_index(host_key)
    client = MediaWikiClient(
        host.api_url,
        user_agent=USER_AGENT,
        requests_per_minute=host.max_requests_per_minute,
        parse_requests_per_minute=host.max_parse_requests_per_minute,
        transport=transport,
    )
    try:
        for slug, page in sorted(index.pages.items()):
            revision_id = page.latest_revision_id
            if store.has_expanded(host_key, slug, revision_id):
                report.skipped.append(slug)
                continue
            if limit is not None and len(report.expanded) >= limit:
                break
            try:
                html = await client.fetch_expanded_html(revision_id)
            except (httpx.HTTPError, MediaWikiError) as exc:
                report.failed.append((slug, str(exc)))
                continue
            store.write_expanded(host_key, slug, revision_id, html)
            report.expanded.append(slug)
            if progress is not None:
                progress(host_key, slug)
    finally:
        await client.close()
    return report


def expand_corpus(
    registry: CorpusRegistry,
    store: CorpusStore,
    *,
    only_host: str | None = None,
    limit: int | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
    progress: ProgressCallback | None = None,
) -> list[HostExpandReport]:
    host_keys = list(registry.hosts)
    if only_host is not None:
        if only_host not in registry.hosts:
            raise CorpusFetchError(
                f"unknown corpus host {only_host!r}; registry has: {', '.join(host_keys)}"
            )
        host_keys = [only_host]

    async def _run() -> list[HostExpandReport]:
        reports = []
        for host_key in host_keys:
            reports.append(
                await expand_host_corpus(
                    host_key,
                    registry.hosts[host_key],
                    store,
                    limit=limit,
                    transport=transport,
                    progress=progress,
                )
            )
        return reports

    return asyncio.run(_run())
