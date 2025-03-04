from django.http import JsonResponse
from ninja import Router

from sports_api.database.models import UnderstatTeamSituation
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
