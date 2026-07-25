from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import UTC, datetime
from urllib.parse import quote

import httpx

from invoker import __version__
from invoker.corpus.mediawiki import MediaWikiClient
from invoker.corpus.registry import select_host_keys
from invoker.corpus.schemas import CorpusDoc, CorpusHost, CorpusRegistry
from invoker.corpus.store import CorpusStore, page_slug

USER_AGENT = (
    f"invoker-kb/{__version__} (+https://github.com/wbinarytree/invoker; awangyaoda@gmail.com)"
)


@dataclass
class HostFetchReport:
    host_key: str
    fetched: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)


def source_page_url(page_base_url: str, resolved_title: str) -> str:
    return page_base_url + quote(resolved_title.replace(" ", "_"))


async def fetch_host_corpus(
    host_key: str,
    host: CorpusHost,
    store: CorpusStore,
    *,
    patch_context: str | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
) -> HostFetchReport:
    report = HostFetchReport(host_key=host_key)
    client = MediaWikiClient(
        host.api_url,
        user_agent=USER_AGENT,
        requests_per_minute=host.max_requests_per_minute,
        transport=transport,
    )
    try:
        revisions, missing = await client.fetch_revisions(host.pages)
    finally:
        await client.close()

    report.missing = [f"{page.requested_title} ({page.reason})" for page in missing]

    retrieved_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")
    for revision in revisions:
        slug = page_slug(revision.resolved_title)
        if store.has_revision(host_key, slug, revision.revision_id):
            report.unchanged.append(slug)
            continue
        doc = CorpusDoc(
            doc_id=f"{host_key}:{slug}@{revision.revision_id}",
            host_key=host_key,
            requested_title=revision.requested_title,
            resolved_title=revision.resolved_title,
            page_id=revision.page_id,
            revision_id=revision.revision_id,
            revision_timestamp=revision.revision_timestamp,
            content=revision.content,
            source_url=source_page_url(host.page_base_url, revision.resolved_title),
            license=host.license,
            retrieved_at=retrieved_at,
            patch_context=patch_context,
        )
        store.write_doc(doc)
        report.fetched.append(slug)
    return report


def fetch_corpus(
    registry: CorpusRegistry,
    store: CorpusStore,
    *,
    only_host: str | None = None,
    patch_context: str | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
) -> list[HostFetchReport]:
    host_keys = select_host_keys(registry, only_host)

    async def _run() -> list[HostFetchReport]:
        reports = []
        for host_key in host_keys:
            reports.append(
                await fetch_host_corpus(
                    host_key,
                    registry.hosts[host_key],
                    store,
                    patch_context=patch_context,
                    transport=transport,
                )
            )
        return reports

    return asyncio.run(_run())
