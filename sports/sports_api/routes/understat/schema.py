from ninja import Schema
from typing import Optional
from datetime import datetime


class UnderstatPlayerSchema(Schema):
    id: str
    player_name: str
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
    team_title: str
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


class UnderstatTeamResultSchema(Schema):
    id: int
    isResult: bool
    side: str
    h: dict
    a: dict
    goals: dict
    xG: dict
    datetime: datetime
    forecast: dict
    result: str
    
class InternalUnderstatTeamResultSchema(Schema):
    public_id: int
    isResult: bool
    side: str
    h_id: str
    h_title: str
    h_short_title: str
    a_id: str
    a_title: str
    a_short_title: str
    goals_a: int
    goals_h: int
    xG_a: int
    xG_h: int
    forecast_w: float
    forecast_d: float
    forecast_l: float
    datetime: datetime
    result: str