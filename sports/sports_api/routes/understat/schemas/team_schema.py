from datetime import datetime
from typing import Dict
from ninja import Schema

from sports_api.constants.understat_enum import UnderstatTeamSituationEnum


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


class UnderstatTeamResultSituationAgainstSchema(Schema):
    shots: int
    goals: int
    xG: float


class UnderstatTeamResultSituationSchema(Schema):
    shots: int
    goals: int
    xG: float
    against: UnderstatTeamResultSituationAgainstSchema


class UnderstatTeamStatsSchema(Schema):
    situation: Dict[
        UnderstatTeamSituationEnum, UnderstatTeamResultSituationAgainstSchema
    ]
    
class InternalUnderstatTeamSituationSchema(Schema):
    public_id: int
    team: str
    source: str
    shots: int
    goals: int
    xG: int
    against_shots: int
    against_goals: int
    against_xG: int
    percent_shots_made: float
    percent_against_shots_made: float

