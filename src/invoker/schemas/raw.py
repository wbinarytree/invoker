from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ODHero(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: int
    name: str
    localized_name: str
    primary_attr: str
    attack_type: str
    roles: list[str] = Field(default_factory=list)


class ODMatchup(BaseModel):
    model_config = ConfigDict(extra="ignore")
    hero_id: int
    games_played: int
    wins: int


class ODProMatch(BaseModel):
    model_config = ConfigDict(extra="ignore")
    match_id: int
    radiant_team_id: int | None = None
    dire_team_id: int | None = None
    radiant_win: bool | None = None
    start_time: int | None = None
    patch: int | None = None
    picks_bans: list[dict] | None = None


class ODAbility(BaseModel):
    model_config = ConfigDict(extra="ignore")
    dname: str | None = None
    behavior: str | list[str] | None = None
    desc: str | None = None
    attrib: list[dict] | None = None


class StratzSynergyEdge(BaseModel):
    model_config = ConfigDict(extra="ignore")
    heroId1: int  # noqa: N815
    heroId2: int  # noqa: N815
    synergy: float
    winsAverage: float | None = None  # noqa: N815
    matchCount: int  # noqa: N815


class LiquipediaAbility(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str
    text: str
