from ninja import Schema
from typing import Optional


class UnderstatPlayerSchema(Schema):
    id: str
    player_name: str
    games: str
    time: str
    goals: str
    xG: str
    assists: str
    xA: str
    shots: str
    key_passes: str
    yellow_cards: str
    red_cards: str
    position: str
    team_title: str
    npg: str
    npxG: str
    xGChain: str
    xGBuildup: str


class InternalUnderstatPlayerSchema(Schema):
    id: str
    public_id: str
    player_name: str
    lowercase_player_name: str
    team: str
    games: int
    time: int
    goals: int
    xG: float
    assists: int
    xA: float
    shots: int
    key_passes: int
    yellow_cards: int
    red_cards: int
    position: str
    npg: int
    npxG: float
    xGChain: float
    xGBuildup: float


class UnderstatPlayerCreateSchema(Schema):
    player_name: str
    games: int
    time: int
    goals: int
    xG: float
    assists: int
    xA: float
    shots: int
    key_passes: int
    yellow_cards: int = 0
    red_cards: int = 0
    position: str
    team_title: str
    npg: int
    npxG: float
    xGChain: float
    xGBuildup: float


class UnderstatPlayerUpdateSchema(Schema):
    player_name: Optional[str] = None
    games: Optional[int] = None
    time: Optional[int] = None
    goals: Optional[int] = None
    xG: Optional[float] = None
    assists: Optional[int] = None
    xA: Optional[float] = None
    shots: Optional[int] = None
    key_passes: Optional[int] = None
    yellow_cards: Optional[int] = None
    red_cards: Optional[int] = None
    position: Optional[str] = None
    team_title: Optional[str] = None
    npg: Optional[int] = None
    npxG: Optional[float] = None
    xGChain: Optional[float] = None
    xGBuildup: Optional[float] = None
