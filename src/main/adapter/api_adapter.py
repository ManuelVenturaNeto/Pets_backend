from typing import Type
from src.main.interfaces import RouteInterface as Route
from src.presenters.helpers import HttpRequest


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """
    Adapter pattern to flask
    :param      - Flask Request
    :api_route: - Composite Routes
    """

    http_request = HttpRequest(body=request.json)
    response = api_route.route(http_request)

    return response
