import ssl
from typing import List
import aiohttp
import json
from ninja import Router
from understat import Understat

from sports_api.routes.understat.schema import UnderstatPlayerSchema


# Create a custom SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

router = Router()


@router.get("/", response=List[UnderstatPlayerSchema])
async def getLeaguePlayer(request):

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
