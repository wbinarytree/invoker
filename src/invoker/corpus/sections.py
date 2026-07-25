from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser

from invoker.corpus.store import CorpusStore

_BLOCK_TAGS = {
    "p",
    "div",
    "ul",
    "ol",
    "li",
    "dl",
    "dt",
    "dd",
    "table",
    "caption",
    "tr",
    "blockquote",
    "pre",
    "br",
    "center",
}
_HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


class CorpusSectionError(RuntimeError):
    pass


@dataclass(frozen=True)
class CorpusSection:
    """One heading-delimited slice of an expanded corpus document.

    `anchor` is the MediaWiki heading id — the same fragment the live wiki
    uses — so citation keys stay resolvable against both the stored revision
    and the source page. The lead (pre-first-heading) section has no anchor.
    """

    host_key: str
    slug: str
    revision_id: int
    anchor: str | None
    heading: str | None
    level: int
    breadcrumbs: tuple[str, ...]
    text: str

    @property
    def citation_key(self) -> str:
        key = f"{self.host_key}/{self.slug}@{self.revision_id}"
        return f"{key}#{self.anchor}" if self.anchor else key


class _SectionParser(HTMLParser):
    """Linear scan over expanded MediaWiki HTML.

    Skipped subtrees: the table of contents (`div#toc`), section edit links
    (`span.mw-editsection`), and script/style. Image alt text is dropped —
    Liquipedia duplicates every inline icon for light/dark mode and the
    adjacent link text already carries the meaning.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.sections: list[tuple[int, str | None, str, list[str]]] = []
        self._parts: list[str] = []
        self._level = 0
        self._anchor: str | None = None
        self._heading_parts: list[str] | None = None
        self._heading_tag: str | None = None
        self._skip_tag: str | None = None
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self._skip_tag is not None:
            if tag == self._skip_tag:
                self._skip_depth += 1
            return
        attr_map = dict(attrs)
        if (
            tag in {"script", "style"}
            or (tag == "div" and attr_map.get("id") == "toc")
            or (tag == "span" and "mw-editsection" in (attr_map.get("class") or ""))
        ):
            self._skip_tag = tag
            self._skip_depth = 1
            return
        if tag in _HEADING_TAGS:
            self._finalize_section()
            self._level = int(tag[1])
            self._anchor = attr_map.get("id")
            self._heading_parts = []
            self._heading_tag = tag
            return
        if tag in _BLOCK_TAGS:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self._skip_tag is not None:
            if tag == self._skip_tag:
                self._skip_depth -= 1
                if self._skip_depth == 0:
                    self._skip_tag = None
            return
        if self._heading_tag is not None and tag == self._heading_tag:
            self._heading_tag = None
            return
        if tag in {"td", "th"}:
            self._parts.append(" | ")
        elif tag in _BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_tag is not None:
            return
        if self._heading_parts is not None and self._heading_tag is not None:
            self._heading_parts.append(data)
            return
        self._parts.append(data)

    def close(self) -> None:
        super().close()
        self._finalize_section()

    def _finalize_section(self) -> None:
        heading = None
        if self._heading_parts is not None:
            heading = " ".join("".join(self._heading_parts).split()) or None
        self.sections.append((self._level, self._anchor, heading or "", self._parts))
        self._parts = []
        self._heading_parts = None


def _clean_text(parts: list[str]) -> str:
    lines = []
    for raw_line in "".join(parts).split("\n"):
        line = " ".join(raw_line.split())
        line = line.strip("| ").strip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def slice_expanded_html(
    html: str, *, host_key: str, slug: str, revision_id: int
) -> list[CorpusSection]:
    """Slice expanded HTML into addressable sections, in document order.

    The lead section is kept only when it has text; heading sections are kept
    even when empty so every anchor on the page stays citable.
    """
    parser = _SectionParser()
    parser.feed(html)
    parser.close()

    sections: list[CorpusSection] = []
    crumb_stack: list[tuple[int, str]] = []
    for level, anchor, heading, parts in parser.sections:
        text = _clean_text(parts)
        if level == 0 and not text:
            continue
        while crumb_stack and crumb_stack[-1][0] >= level:
            crumb_stack.pop()
        if heading:
            crumb_stack.append((level, heading))
        sections.append(
            CorpusSection(
                host_key=host_key,
                slug=slug,
                revision_id=revision_id,
                anchor=anchor,
                heading=heading or None,
                level=level,
                breadcrumbs=tuple(crumb for _, crumb in crumb_stack),
                text=text,
            )
        )
    return sections


def load_sections(
    store: CorpusStore,
    host_key: str,
    slug: str,
    revision_id: int | None = None,
) -> list[CorpusSection]:
    """Load and slice a stored expanded document; latest revision by default."""
    if revision_id is None:
        index = store.load_index(host_key)
        page = index.pages.get(slug)
        if page is None:
            raise CorpusSectionError(
                f"page {slug!r} not in the {host_key} corpus index; run fetch-corpus"
            )
        revision_id = page.latest_revision_id
    path = store.expanded_path(host_key, slug, revision_id)
    if not path.exists():
        raise CorpusSectionError(
            f"no expanded text for {host_key}/{slug}@{revision_id}; run expand-corpus"
        )
    return slice_expanded_html(
        path.read_text(), host_key=host_key, slug=slug, revision_id=revision_id
    )
