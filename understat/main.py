import ssl
import json
import asyncio
import aiohttp
from understat import Understat


async def main():
    # Create a custom SSL context
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context)
    ) as session:
        understat = Understat(session)
        player = await understat.get_league_players(
            "epl", 2025, player_name="Erling Haaland", team_title="Manchester City"
        )
        print(json.dumps(player))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
