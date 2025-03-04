from datetime import datetime
from typing import List
from sports_api.routes.understat.schemas.team_schema import (
    InternalUnderstatTeamFormationSchema,
    InternalUnderstatTeamResultSchema,
    InternalUnderstatTeamSituationSchema,
    UnderstatTeamResultSchema,
    UnderstatTeamStatsSchema,
)


def create_public_id(season: int, team_title: str, key: str):
    return team_title + "-" + str(season) + "-" + key


def calculate_percent_goals(numerator: int, denominator: int):
    return (float(numerator) / float(denominator)) * 100.0


def map_understat_team_result_to_internal(
    team_results: UnderstatTeamResultSchema, season: int
) -> List[InternalUnderstatTeamResultSchema]:
    mapped_results = []
    for team_result in team_results:
        result: InternalUnderstatTeamResultSchema = {
            "public_id": str(team_result["id"]),
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
    team_stats: UnderstatTeamStatsSchema, season: int, team_title: str
) -> List[InternalUnderstatTeamSituationSchema]:
    mapped_results = []
    team_situation = team_stats["situation"]

    total_goals_scored = 0
    total_against_goals_scored = 0
    for team_situation_key in team_situation:
        team_stat = team_situation[team_situation_key]
        total_goals_scored += team_stat["goals"]
        total_against_goals_scored += team_stat["against"]["goals"]

    for team_situation_key in team_situation:  # Type of UnderstatTeamSituationEnum
        team_stat = team_situation[team_situation_key]
        team_shots = team_stat["shots"]
        team_goals = team_stat["goals"]
        against_shots = team_stat["against"]["shots"]
        against_goals = team_stat["against"]["goals"]
        result: InternalUnderstatTeamSituationSchema = {
            "public_id": create_public_id(season, team_title, team_situation_key),
            "team": team_title,
            "source": team_situation_key,
            "shots": team_shots,
            "goals": team_goals,
            "xG": team_stat["xG"],
            "against_shots": against_shots,
            "against_goals": against_goals,
            "against_xG": team_stat["against"]["xG"],
            "percent_shots_made": calculate_percent_goals(team_goals, team_shots),
            "percent_shots_made_across_all_goals": calculate_percent_goals(
                team_goals, total_goals_scored
            ),
            "percent_against_shots_made": calculate_percent_goals(
                against_goals, against_shots
            ),
            "percent_against_shots_made_across_all_goals": calculate_percent_goals(
                against_goals, total_against_goals_scored
            ),
        }

        mapped_results.append(result)

    return mapped_results


def map_understat_team_stat_to_formation(
    team_stats: UnderstatTeamStatsSchema, season: int, team_title: str
) -> List[InternalUnderstatTeamFormationSchema]:
    mapped_results = []
    team_formation = team_stats["formation"]

    total_goals_scored = 0
    total_against_goals_scored = 0
    for team_situation_key in team_formation:
        team_formation_data = team_formation[team_situation_key]
        total_goals_scored += team_formation_data["goals"]
        total_against_goals_scored += team_formation_data["against"]["goals"]

    for team_formation_key in team_formation:  # Type of UnderstatTeamSituationEnum
        team_formation_data = team_formation[team_formation_key]
        team_shots = team_formation_data["shots"]
        team_goals = team_formation_data["goals"]
        against_shots = team_formation_data["against"]["shots"]
        against_goals = team_formation_data["against"]["goals"]
        result: InternalUnderstatTeamSituationSchema = {
            "public_id": create_public_id(season, team_title, team_formation_key),
            "time_spent": team_formation_data["time"],
            "team": team_title,
            "source": team_formation_key,
            "shots": team_shots,
            "goals": team_goals,
            "xG": team_formation_data["xG"],
            "against_shots": against_shots,
            "against_goals": against_goals,
            "against_xG": team_formation_data["against"]["xG"],
            "percent_shots_made": calculate_percent_goals(team_goals, team_shots),
            "percent_shots_made_across_all_goals": calculate_percent_goals(
                team_goals, total_goals_scored
            ),
            "percent_against_shots_made": calculate_percent_goals(
                against_goals, against_shots
            ),
            "percent_against_shots_made_across_all_goals": calculate_percent_goals(
                against_goals, total_against_goals_scored
            ),
        }

        mapped_results.append(result)

    return mapped_results
