from datetime import datetime
from typing import List
from sports_api.routes.understat.schemas.team_schema import (
    InternalUnderstatTeamResultSchema,
    InternalUnderstatTeamSituationSchema,
    UnderstatTeamResultSchema,
    UnderstatTeamStatsSchema,
)


def map_understat_team_result_to_internal(
    team_results: UnderstatTeamResultSchema, season: int
) -> List[InternalUnderstatTeamResultSchema]:
    mapped_results = []
    for team_result in team_results:
        result: InternalUnderstatTeamResultSchema = {
            "public_id": team_result["id"],
            "team": team_result["h"]["title"],
            "season": season,
            "is_result": team_result["isResult"],
            "side": team_result["side"],
            "h_id": team_result["h"]["id"],
            "h_title": team_result["h"]["title"],
            "h_short_title": team_result["h"]["short_title"],
            "a_id": team_result["a"]["id"],
            "a_title": team_result["a"]["title"],
            "a_short_title": team_result["a"]["short_title"],
            "goals_h": int(team_result["goals"]["h"]),
            "goals_a": int(team_result["goals"]["a"]),
            "xG_h": float(team_result["xG"]["h"]),
            "xG_a": float(team_result["xG"]["a"]),
            "datetime": datetime.strptime(team_result["datetime"], "%Y-%m-%d %H:%M:%S"),
            "forecast_w": team_result["forecast"]["w"],
            "forecast_d": team_result["forecast"]["d"],
            "forecast_l": team_result["forecast"]["l"],
            "result": team_result["result"],
        }
        mapped_results.append(result)

    return mapped_results


def map_understat_team_stat_to_situation(
    team_stats: UnderstatTeamStatsSchema, team_title: str
) -> List[InternalUnderstatTeamSituationSchema]:
    mapped_results = []
    team_situation = team_stats["situation"]
    for team_situation_key in team_situation: # Type of UnderstatTeamSituationEnum
        team_stat = team_situation[team_situation_key]
        team_shots = team_stat["shots"]
        team_goals = team_stat["goals"]
        against_shots = team_stat["against"]["shots"]
        against_goals = team_stat["against"]["goals"]
        result: InternalUnderstatTeamSituationSchema = InternalUnderstatTeamSituationSchema(
                public_id=team_stat["id"],
                team=team_title,
                source=team_situation_key,
                shots=team_shots,
                goals=team_goals,
                xG=team_stat["xG"],
                against_shots=against_shots,
                against_goals=against_goals,
                against_xG=team_stat["against"]["xG"],
                percent_shots_made=float(team_goals) / float(team_shots),
                percent_against_shots_made=float(against_goals) / float(against_shots),
            )
        

        mapped_results.append(result)

    return mapped_results
