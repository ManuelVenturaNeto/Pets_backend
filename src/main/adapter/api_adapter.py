from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interfaces import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        query_string_params = request.args.to_dict()

        if "pet_id" in query_string_params:
            query_string_params["pet_id"] = int(query_string_params["pet_id"])
        if "animal_shelter_id" in query_string_params:
            query_string_params["animal_shelter_id"] = int(query_string_params["animal_shelter_id"])

    except Exception:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    try:
        http_request = HttpRequest(
            header=request.headers, body=request.json, query=query_string_params
        )
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except Exception:
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
