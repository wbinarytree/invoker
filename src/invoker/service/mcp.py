from __future__ import annotations

from typing import Any

from invoker.service.core import KnowledgeService


class KnowledgeMCPAdapter:
    """Small MCP-style adapter over KnowledgeService methods.

    This intentionally avoids an SDK dependency in the first slice. Agent
    runtimes can map these tool descriptors and calls onto their MCP transport.
    """

    def __init__(self, service: KnowledgeService) -> None:
        self.service = service

    def list_tools(self) -> list[dict[str, Any]]:
        return [
            {"name": "list_bundle_patches", "input_schema": {"type": "object", "properties": {}}},
            {"name": "lookup_hero", "input_schema": _schema(["query"], ["patch"])},
            {"name": "get_hero_constants", "input_schema": _schema(["hero"], ["patch"])},
            {"name": "kb_catalog", "input_schema": _schema([], ["patch", "kind"])},
            {"name": "kb_resolve", "input_schema": _schema(["query"], ["patch"])},
            {"name": "kb_card", "input_schema": _schema(["id"], ["patch"])},
            {"name": "kb_article", "input_schema": _schema(["id"], ["patch"])},
            {
                "name": "search_changelog",
                "input_schema": _schema([], ["grep", "entity", "note_patch", "patch"]),
            },
            {"name": "resolve_team", "input_schema": _schema(["query"], ["patch"])},
            {"name": "resolve_player", "input_schema": _schema(["query"], ["team", "patch"])},
            {"name": "get_team_profile", "input_schema": _schema(["team"], ["patch"])},
            {"name": "get_team_roster", "input_schema": _schema(["team"], ["patch"])},
            {"name": "get_team_hero_pool", "input_schema": _schema(["team"], ["patch"])},
            {
                "name": "get_team_player_hero_pool",
                "input_schema": _schema(["team", "player"], ["patch"]),
            },
        ]

    def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
        args = arguments or {}
        if name == "list_bundle_patches":
            return self.service.list_bundle_patches()
        if name == "lookup_hero":
            return self.service.lookup_hero(args["query"], patch=args.get("patch"))
        if name == "get_hero_constants":
            return self.service.get_hero_constants(args["hero"], patch=args.get("patch"))
        if name == "kb_catalog":
            return self.service.kb_catalog(patch=args.get("patch"), kind=args.get("kind"))
        if name == "kb_resolve":
            return self.service.kb_resolve(args["query"], patch=args.get("patch"))
        if name == "kb_card":
            return self.service.kb_card(args["id"], patch=args.get("patch"))
        if name == "kb_article":
            return self.service.kb_article(args["id"], patch=args.get("patch"))
        if name == "search_changelog":
            return self.service.search_changelog(
                grep=args.get("grep"),
                entity=args.get("entity"),
                note_patch=args.get("note_patch"),
                patch=args.get("patch"),
            )
        if name == "resolve_team":
            return self.service.resolve_team(args["query"], patch=args.get("patch"))
        if name == "resolve_player":
            return self.service.resolve_player(
                args["query"], team=args.get("team"), patch=args.get("patch")
            )
        if name == "get_team_profile":
            return self.service.get_team_profile(args["team"], patch=args.get("patch"))
        if name == "get_team_roster":
            return self.service.get_team_roster(args["team"], patch=args.get("patch"))
        if name == "get_team_hero_pool":
            return self.service.get_team_hero_pool(args["team"], patch=args.get("patch"))
        if name == "get_team_player_hero_pool":
            return self.service.get_team_player_hero_pool(
                args["team"], args["player"], patch=args.get("patch")
            )
        raise KeyError(f"unknown knowledge tool: {name}")


def _schema(required: list[str], optional: list[str]) -> dict[str, Any]:
    properties = {
        key: (
            {"type": ["string", "integer"]}
            if key in {"hero", "team", "player", "query"}
            else {"type": "string"}
        )
        for key in required + optional
    }
    return {"type": "object", "properties": properties, "required": required}
