from datetime import datetime
from sports_api.routes.understat.schema import (
    InternalUnderstatTeamResultSchema,
    UnderstatTeamResultSchema,
)


def map_understat_team_result_to_internal(
    team_results: UnderstatTeamResultSchema,
    season: int
) -> InternalUnderstatTeamResultSchema:
    mapped_results = []
    for team_result in team_results:
        result: InternalUnderstatTeamResultSchema = {
            "public_id": team_result["id"],
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
