from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


class KVParseError(ValueError):
    pass


@dataclass(frozen=True)
class _Token:
    value: str
    line: int
    col: int


class KV1Parser:
    """Narrow KV1 parser for Valve text files used by the snapshot command."""

    def __init__(self, text: str, *, source: str = "<string>") -> None:
        self._text = text
        self._source = source
        self._tokens = self._tokenize()
        self._pos = 0

    def parse(self) -> dict[str, Any]:
        parsed: dict[str, Any] = {}
        while not self._at_end():
            key = self._read_token()
            value = self._read_value()
            parsed[key.value] = value
        return parsed

    def _read_value(self) -> Any:
        if self._peek_value("{"):
            self._read_token()
            return self._read_block()
        return self._read_token().value

    def _read_block(self) -> dict[str, Any]:
        block: dict[str, Any] = {}
        while not self._at_end():
            if self._peek_value("}"):
                self._read_token()
                return block
            key = self._read_token()
            value = self._read_value()
            block[key.value] = value
        raise self._error("unterminated block")

    def _tokenize(self) -> list[_Token]:
        tokens: list[_Token] = []
        i = 0
        line = 1
        col = 1
        text = self._text
        while i < len(text):
            ch = text[i]
            if ch in " \t\r\ufeff":
                i += 1
                col += 1
                continue
            if ch == "\n":
                i += 1
                line += 1
                col = 1
                continue
            if ch == "/" and i + 1 < len(text) and text[i + 1] == "/":
                i += 2
                col += 2
                while i < len(text) and text[i] != "\n":
                    i += 1
                    col += 1
                continue
            if ch == "/" and i + 1 < len(text) and text[i + 1] == "*":
                raise self._error("block comments are not supported", line=line, col=col)
            if ch == "#":
                raise self._error("preprocessor directives are not supported", line=line, col=col)
            if ch == "[" and i + 1 < len(text) and text[i + 1] == "$":
                raise self._error("conditional gates are not supported", line=line, col=col)
            if ch in "{}":
                tokens.append(_Token(ch, line, col))
                i += 1
                col += 1
                continue
            if ch == '"':
                start_line = line
                start_col = col
                i += 1
                col += 1
                chars: list[str] = []
                while i < len(text):
                    ch = text[i]
                    if ch == '"':
                        i += 1
                        col += 1
                        tokens.append(_Token("".join(chars), start_line, start_col))
                        break
                    if ch == "\\" and i + 1 < len(text):
                        chars.append(text[i + 1])
                        i += 2
                        col += 2
                        continue
                    if ch == "\n":
                        chars.append(ch)
                        i += 1
                        line += 1
                        col = 1
                        continue
                    chars.append(ch)
                    i += 1
                    col += 1
                else:
                    raise self._error("unterminated quoted string", line=start_line, col=start_col)
                continue

            start = i
            start_col = col
            while i < len(text) and text[i] not in " \t\r\n{}":
                if text[i] == "#":
                    raise self._error(
                        "preprocessor directives are not supported", line=line, col=col
                    )
                i += 1
                col += 1
            tokens.append(_Token(text[start:i], line, start_col))
        return tokens

    def _read_token(self) -> _Token:
        if self._at_end():
            raise self._error("unexpected end of file")
        token = self._tokens[self._pos]
        self._pos += 1
        return token

    def _peek_value(self, value: str) -> bool:
        return not self._at_end() and self._tokens[self._pos].value == value

    def _at_end(self) -> bool:
        return self._pos >= len(self._tokens)

    def _error(
        self,
        message: str,
        *,
        line: int | None = None,
        col: int | None = None,
    ) -> KVParseError:
        if line is None or col is None:
            if self._pos < len(self._tokens):
                token = self._tokens[self._pos]
                line = token.line
                col = token.col
            else:
                line = self._text.count("\n") + 1
                col = 1
        return KVParseError(f"{self._source}:{line}:{col}: {message}")


def parse_kv1(text: str, *, source: str = "<string>") -> dict[str, Any]:
    return KV1Parser(text, source=source).parse()


def parse_kv1_file(path: Path) -> dict[str, Any]:
    return parse_kv1(path.read_text(), source=str(path))
