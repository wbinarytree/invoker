from __future__ import annotations

import asyncio
from dataclasses import dataclass, field

import httpx

from invoker.corpus.fetch import USER_AGENT
from invoker.corpus.mediawiki import MediaWikiClient
from invoker.corpus.registry import select_host_keys
from invoker.corpus.schemas import CorpusHost, CorpusRegistry
from invoker.corpus.store import CorpusStore


@dataclass
class HostCoverageReport:
    """Diff between a host's category universe and the curated registry.

    `unreviewed` is the actionable bucket: pages that exist in the coverage
    categories but were neither fetched nor explicitly omitted with a reason.
    """

    host_key: str
    universe_size: int = 0
    covered: list[str] = field(default_factory=list)
    omitted: list[tuple[str, str]] = field(default_factory=list)
    omitted_by_rule: list[tuple[str, str, int]] = field(default_factory=list)
    unreviewed: list[str] = field(default_factory=list)
    outside_categories: list[str] = field(default_factory=list)


def _resolved_registry_titles(host: CorpusHost, store: CorpusStore, host_key: str) -> set[str]:
    """Registry titles plus their canonical resolutions from the fetch index,
    so redirected pages count as covered under their canonical name.

    Only index entries whose requested title is still in the registry count:
    a page dropped from pages.yaml must resurface as unreviewed, not stay
    silently covered by its stale index entry."""
    titles = set(host.pages)
    index = store.load_index(host_key)
    titles.update(
        page.resolved_title
        for page in index.pages.values()
        if page.requested_title in titles
    )
    return titles


async def coverage_for_host(
    host_key: str,
    host: CorpusHost,
    store: CorpusStore,
    *,
    transport: httpx.AsyncBaseTransport | None = None,
) -> HostCoverageReport:
    report = HostCoverageReport(host_key=host_key)
    if not host.coverage_categories:
        return report

    client = MediaWikiClient(
        host.api_url,
        user_agent=USER_AGENT,
        requests_per_minute=host.max_requests_per_minute,
        transport=transport,
    )
    try:
        universe: dict[str, None] = {}
        for category in host.coverage_categories:
            for title in await client.list_category_members(category):
                universe.setdefault(title, None)
    finally:
        await client.close()

    covered_titles = _resolved_registry_titles(host, store, host_key)
    omit_reasons = {page.title: page.reason for page in host.omit}
    rule_counts = {rule.prefix: 0 for rule in host.omit_prefixes}

    report.universe_size = len(universe)
    for title in universe:
        if title in covered_titles:
            report.covered.append(title)
        elif title in omit_reasons:
            report.omitted.append((title, omit_reasons[title]))
        else:
            rule = next(
                (rule for rule in host.omit_prefixes if title.startswith(rule.prefix)),
                None,
            )
            if rule is not None:
                rule_counts[rule.prefix] += 1
            else:
                report.unreviewed.append(title)
    report.omitted_by_rule = [
        (rule.prefix, rule.reason, rule_counts[rule.prefix]) for rule in host.omit_prefixes
    ]

    index = store.load_index(host_key)
    resolved_by_requested = {
        page.requested_title: page.resolved_title for page in index.pages.values()
    }
    for requested in host.pages:
        resolved = resolved_by_requested.get(requested, requested)
        if resolved not in universe:
            report.outside_categories.append(requested)
    return report


def corpus_coverage(
    registry: CorpusRegistry,
    store: CorpusStore,
    *,
    only_host: str | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
) -> list[HostCoverageReport]:
    host_keys = select_host_keys(registry, only_host)

    async def _run() -> list[HostCoverageReport]:
        reports = []
        for host_key in host_keys:
            reports.append(
                await coverage_for_host(
                    host_key,
                    registry.hosts[host_key],
                    store,
                    transport=transport,
                )
            )
        return reports

    return asyncio.run(_run())
