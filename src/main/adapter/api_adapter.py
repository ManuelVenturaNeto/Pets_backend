import logging
from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interfaces import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        query_string_params = request.args.to_dict()

        if "pet_id" in query_string_params:
            query_string_params["pet_id"] = int(query_string_params["pet_id"])
            log.info(f"Converted pet_id to integer: {query_string_params['pet_id']}")

        if "animal_shelter_id" in query_string_params:
            query_string_params["animal_shelter_id"] = int(query_string_params["animal_shelter_id"])
            log.info(f"Converted animal_shelter_id to integer: {query_string_params['animal_shelter_id']}")

    except Exception:
        http_error = HttpErrors.error_400()
        log.error("Bad Request: Error processing query parameters")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    try:
        http_request = HttpRequest(header=request.headers, body=request.json, query=query_string_params)
        response = api_route.route(http_request)
        log.info("Request processed successfully")

    except IntegrityError:
        http_error = HttpErrors.error_409()
        log.error("Conflict Error: Integrity constraint violated")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    except Exception:
        http_error = HttpErrors.error_500()
        log.error("Internal Server Error occurred")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    log.info("Response generated successfully")
    return response
