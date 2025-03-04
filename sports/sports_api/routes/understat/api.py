import ssl
from typing import List
import aiohttp
import json
from ninja import Router
from understat import Understat
from asgiref.sync import sync_to_async

from sports_api.database.models import UnderstatTeamResult
from sports_api.helpers.mappers import map_understat_team_result_to_internal
from sports_api.helpers.sort import sort_by_datetime_desc
from sports_api.routes.understat.schema import (
    UnderstatPlayerSchema,
    UnderstatTeamResultSchema,
)


# Create a custom SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

router = Router()


@router.get("/player", response=List[UnderstatPlayerSchema])
async def get_league_player(request):

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context)
    ) as session:
        query_params = request.GET.dict()

        league_name = query_params.get("league_name")
        year = int(query_params.get("year"))
        player_name = query_params.get("player_name")
        team_title = query_params.get("team_title")

        understat = Understat(session)
        player = await understat.get_league_players(
            league_name, year, player_name=player_name, team_title=team_title
        )
        print(json.dumps(player))
        return player


@router.get("/team-results", response=List[UnderstatTeamResultSchema])
async def get_team_results(request):

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context)
    ) as session:
        query_params = request.GET.dict()

        team_title = query_params.get("team_title")
        year = int(query_params.get("year"))
        side = query_params.get("side")

        understat = Understat(session)
        team_results = await understat.get_team_results(
            team_name=team_title, season=year, side=side
        )

        sorted_team_results = sort_by_datetime_desc(team_results)
        # print(json.dumps(sorted_team_results))

        mapped_team_results = map_understat_team_result_to_internal(sorted_team_results)
        for data in mapped_team_results:
            public_id = data.get("public_id")
            # Use Django's update_or_create method
            await sync_to_async(UnderstatTeamResult.objects.update_or_create)(
                public_id=public_id,
                defaults=data,
            )
        return sorted_team_results


@router.get("/team-stats")
async def get_team_stats(request):

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context)
    ) as session:
        query_params = request.GET.dict()

        team_title = query_params.get("team_title")
        year = int(query_params.get("year"))

        understat = Understat(session)
        team_stats = await understat.get_team_stats(team_name=team_title, season=year)

        # print(json.dumps(sorted_team_results))
        return team_stats
