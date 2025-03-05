from django.http import JsonResponse
from django.db.models import Q
from ninja import Router

from sports_api.database.models import (
    UnderstatTeamFormationStats,
    UnderstatTeamPlayerStats,
    UnderstatTeamSituation,
    UnderstatTeamTimingStats,
)
from sports_api.helpers.response import error_response, success_response


router = Router()


@router.get("/team-situation")
def get_team_situation(request):
    try:
        query_params = request.GET.dict()

        team_title = query_params.get("team_title")
        year = int(query_params.get("year"))
        source = query_params.get("source", None)

        # Query for all sources
        if not source:
            data = list(
                UnderstatTeamSituation.objects.filter(
                    season=year, team=team_title
                ).values()
            )
        else:
            data = list(
                UnderstatTeamSituation.objects.filter(
                    season=year, team=team_title, source=source
                ).values()
            )

        return JsonResponse(
            success_response(data, "Successfully retrieved team situation")
        )
    except:
        return JsonResponse(error_response("Failed to retrieve team situation."))


@router.get("/team-formation")
def get_team_formation(request):
    try:
        query_params = request.GET.dict()

        team_title = query_params.get("team_title")
        year = int(query_params.get("year"))
        formation = query_params.get("formation", None)

        # Query for all formations
        if not formation:
            data = list(
                UnderstatTeamFormationStats.objects.filter(
                    season=year, team=team_title
                ).values()
            )
        else:
            data = list(
                UnderstatTeamFormationStats.objects.filter(
                    season=year, team=team_title, source=formation
                ).values()
            )

        return JsonResponse(
            success_response(data, "Successfully retrieved team formation stats")
        )
    except:
        return JsonResponse(error_response("Failed to retrieve team formation stats."))


@router.get("/team-timing")
def get_team_timing_stats(request):
    try:
        query_params = request.GET.dict()

        team_title = query_params.get("team_title")
        year = int(query_params.get("year"))
        timing = query_params.get("timing", None)

        if not timing:
            data = list(
                UnderstatTeamTimingStats.objects.filter(
                    season=year, team=team_title
                ).values()
            )
        else:
            data = list(
                UnderstatTeamTimingStats.objects.filter(
                    season=year, team=team_title, source=timing
                ).values()
            )

        return JsonResponse(
            success_response(data, "Successfully retrieved team timing stats")
        )
    except:
        return JsonResponse(error_response("Failed to retrieve team timing stats."))


@router.get("/team-players")
def get_team_players_stats(request):
    try:
        query_params = request.GET.dict()

        team_title = query_params.get("team_title")
        year = int(query_params.get("year"))
        position = query_params.get("position")
        sort_by_goals = query_params.get("sort[goals]")
        sort_by_percent_shots_made = query_params.get("sort[percent_shots_made]")
        sort_by_xG = query_params.get("sort[xG]")

        # One sort parameter allowed for now

        if sort_by_goals:
            sort_direction = "goals" if sort_by_goals.lower() == "asc" else "-goals"
            data = UnderstatTeamPlayerStats.objects.filter(
                season=year, team=team_title
            ).order_by(sort_direction)

        elif sort_by_percent_shots_made:
            sort_direction = (
                "percent_shots_made_across_all_goals"
                if sort_by_percent_shots_made.lower() == "asc"
                else "-percent_shots_made_across_all_goals"
            )
            data = UnderstatTeamPlayerStats.objects.filter(
                season=year, team=team_title
            ).order_by(sort_direction)

        elif sort_by_percent_shots_made:
            sort_direction = "xG" if sort_by_xG.lower() == "asc" else "-xG"
            data = UnderstatTeamPlayerStats.objects.filter(
                season=year, team=team_title
            ).order_by(sort_direction)

        else:
            data = UnderstatTeamPlayerStats.objects.filter(season=year, team=team_title)

        if position:
            data = data.filter(position=position)

        data = list(data.values())

        return JsonResponse(
            success_response(data, "Successfully retrieved team players stats")
        )
    except:
        return JsonResponse(error_response("Failed to retrieve team players stats."))


@router.get("/search-players")
def search_players(request):
    try:
        query_params = request.GET.dict()
        name = query_params.get("name")
        team = query_params.get("team", None)

        players = UnderstatTeamPlayerStats.objects.filter(
            lowercase_player_name__istartswith=name
        )

        if name:
            players = players.filter(team=team)

        data = list(players.values())

        return JsonResponse(
            success_response(data, "Successfully retrieved players' stats")
        )

    except:
        return JsonResponse(error_response("Failed to find any player's stats."))
