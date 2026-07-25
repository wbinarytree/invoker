from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path

import markdown

from invoker.corpus.registry import load_registry
from invoker.corpus.store import page_slug
from invoker.gen.artifacts import ConceptArtifact
from invoker.gen.concepts import load_concept_article

_MARK_PATTERN = re.compile(r"\[corpus:([^\]\s]+)\]")
_KEY_PATTERN = re.compile(r"^(?P<host>[^/]+)/(?P<slug>[^@]+)@(?P<rev>\d+)(?:#(?P<anchor>.+))?$")

_CSS = """
:root { --fg: #1c1c1c; --muted: #6a6a6a; --line: #e3e0d8; --accent: #8a5a2b;
        --bg: #faf8f4; --card: #f1eee6; }
* { box-sizing: border-box; }
body { margin: 0; font: 16px/1.65 Georgia, 'Times New Roman', serif;
       color: var(--fg); background: var(--bg); }
.layout { display: flex; min-height: 100vh; }
nav { width: 240px; flex-shrink: 0; border-right: 1px solid var(--line);
      padding: 1.5rem 1.25rem; }
nav h1 { font-size: 1rem; margin: 0 0 1rem; letter-spacing: 0.04em; }
nav a { display: block; color: var(--fg); text-decoration: none;
        padding: 0.15rem 0; font-size: 0.9rem; }
nav a:hover { color: var(--accent); }
nav .missing { color: var(--muted); font-style: italic; }
main { flex: 1; max-width: 46rem; padding: 2.5rem 3rem; }
h1, h2, h3 { line-height: 1.25; }
a.mark { color: var(--accent); text-decoration: none; font-size: 0.72em;
         vertical-align: super; }
table { border-collapse: collapse; width: 100%; font-size: 0.9rem; }
th, td { text-align: left; padding: 0.35rem 0.6rem;
         border-bottom: 1px solid var(--line); }
.status-generated { color: #2e6b30; }
.status-missing { color: var(--muted); font-style: italic; }
.card { background: var(--card); border: 1px solid var(--line);
        border-radius: 6px; padding: 1rem 1.25rem; margin: 1.5rem 0; }
.card li { margin-bottom: 0.4rem; }
footer.prov { margin-top: 2.5rem; border-top: 1px solid var(--line);
              color: var(--muted); font-size: 0.78rem; }
code { font-size: 0.85em; }
"""


@dataclass(frozen=True)
class SiteReport:
    out_dir: Path
    generated: int
    missing: int


def _mark_link(host_base_urls: dict[str, str], key: str) -> str:
    parsed = _KEY_PATTERN.match(key)
    label = html.escape(key)
    if parsed is None:
        return f'<a class="mark" title="{label}">[{label}]</a>'
    base = host_base_urls.get(parsed["host"])
    anchor = f"#{parsed['anchor']}" if parsed["anchor"] else ""
    if base is None:
        return f'<a class="mark" title="{label}">[src]</a>'
    url = f"{base.rstrip('/')}/index.php?oldid={parsed['rev']}{anchor}"
    return f'<a class="mark" href="{html.escape(url)}" title="{label}">[src]</a>'


def _render_article_html(article: str, host_base_urls: dict[str, str]) -> str:
    """Escape + markdown the article with marks stashed as placeholders.

    Marks must never pass through html.escape or markdown: keys carry `&`
    and `_`, which the pipeline mangles into double-escaped anchors and
    spurious <em> spans."""
    stashed_keys: list[str] = []

    def stash(match: re.Match[str]) -> str:
        stashed_keys.append(match.group(1))
        return f"MARKREF{len(stashed_keys) - 1}ENDMARKREF"

    stashed = _MARK_PATTERN.sub(stash, article)
    body = markdown.markdown(html.escape(stashed))
    for index, key in enumerate(stashed_keys):
        body = body.replace(f"MARKREF{index}ENDMARKREF", _mark_link(host_base_urls, key))
    return body


def _page(title: str, nav_html: str, body: str) -> str:
    return (
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<meta name='viewport' content='width=device-width, initial-scale=1'>"
        f"<title>{html.escape(title)}</title><style>{_CSS}</style></head>"
        f"<body><div class='layout'><nav>{nav_html}</nav><main>{body}</main></div></body></html>"
    )


def render_kb_site(kb_dir: Path, patch: str, out_dir: Path) -> SiteReport:
    """Render the KB archive for one patch into a browsable static site.

    Coverage = every curated corpus page vs the artifacts that exist; the
    index is the audit surface for what is populated and what is missing.
    """
    registry = load_registry()
    host_base_urls = {key: host.page_base_url for key, host in registry.hosts.items()}

    concepts_dir = kb_dir / "concepts"
    artifacts: dict[str, tuple[ConceptArtifact, str]] = {}
    if concepts_dir.exists():
        for artifact_path in sorted(concepts_dir.glob("*/artifact.json")):
            artifact, article = load_concept_article(artifact_path)
            artifacts[artifact.slug] = (artifact, article)

    curated: dict[str, str] = {}
    for host in registry.hosts.values():
        for title in host.pages:
            curated[page_slug(title)] = title

    nav_items = ["<h1>invoker KB</h1>", "<a href='index.html'>Coverage</a><hr>"]
    concept_nav = ["<h1>invoker KB</h1>", "<a href='../index.html'>Coverage</a><hr>"]
    for slug in sorted(set(curated) | set(artifacts)):
        if slug in artifacts:
            nav_items.append(f"<a href='concepts/{slug}.html'>{html.escape(slug)}</a>")
            concept_nav.append(f"<a href='{slug}.html'>{html.escape(slug)}</a>")
        else:
            nav_items.append(f"<span class='missing'>{html.escape(slug)}</span>")
            concept_nav.append(f"<span class='missing'>{html.escape(slug)}</span>")
    nav_html = "".join(nav_items)
    concept_nav_html = "".join(concept_nav)

    out_concepts = out_dir / "concepts"
    out_concepts.mkdir(parents=True, exist_ok=True)

    for slug, (artifact, article) in artifacts.items():
        article_html = _render_article_html(article, host_base_urls)
        card_items = "".join(
            f"<li>{html.escape(s.text)} "
            + " ".join(_mark_link(host_base_urls, m.removeprefix("corpus:")) for m in s.marks)
            + "</li>"
            for s in artifact.card.sentences
        )
        prov = artifact.article_provenance
        body = (
            f"<p><em>{html.escape(artifact.title)} — patch {html.escape(artifact.patch)}</em></p>"
            f"<div class='card'><strong>Card ({len(artifact.card.sentences)} sentences)</strong>"
            f"<ul>{card_items}</ul></div>"
            f"{article_html}"
            f"<footer class='prov'>model {html.escape(prov.model)} · transport "
            f"{html.escape(prov.transport)} · prompt {html.escape(prov.prompt_name)}@"
            f"{html.escape(prov.prompt_version)} · packet {artifact.packet_sha256[:12]} · "
            f"article {artifact.article_sha256[:12]} · {html.escape(prov.generated_at)}</footer>"
        )
        (out_concepts / f"{slug}.html").write_text(
            _page(f"{artifact.title} — invoker KB", concept_nav_html, body)
        )

    rows = []
    for slug in sorted(set(curated) | set(artifacts)):
        if slug in artifacts:
            artifact, _ = artifacts[slug]
            rows.append(
                f"<tr><td><a href='concepts/{slug}.html'>{html.escape(slug)}</a></td>"
                f"<td class='status-generated'>generated</td>"
                f"<td>{len(artifact.citations)}</td>"
                f"<td>{len(artifact.card.sentences)}</td>"
                f"<td><code>{html.escape(artifact.article_provenance.prompt_version)}</code></td></tr>"
            )
        else:
            rows.append(
                f"<tr><td>{html.escape(slug)}</td><td class='status-missing'>missing</td>"
                f"<td>—</td><td>—</td><td>—</td></tr>"
            )
    index_body = (
        f"<h1>Coverage — patch {html.escape(patch)}</h1>"
        f"<p>{len(artifacts)} generated / {len(set(curated) | set(artifacts))} curated pages.</p>"
        f"<table><tr><th>concept</th><th>status</th><th>citations</th>"
        f"<th>card</th><th>prompt</th></tr>{''.join(rows)}</table>"
    )
    (out_dir / "index.html").write_text(_page(f"invoker KB — {patch}", nav_html, index_body))

    return SiteReport(
        out_dir=out_dir,
        generated=len(artifacts),
        missing=len(set(curated) - set(artifacts)),
    )
