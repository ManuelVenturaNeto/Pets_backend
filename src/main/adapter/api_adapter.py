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

        # Convert specific parameters to integer if they exist
        if "pet_id" in query_string_params:
            query_string_params["pet_id"] = int(query_string_params["pet_id"])
            log.info(f"Converted pet_id to integer: {query_string_params['pet_id']}")

        if "animal_shelter_id" in query_string_params:
            query_string_params["animal_shelter_id"] = int(query_string_params["animal_shelter_id"])
            log.info(f"Converted animal_shelter_id to integer: {query_string_params['animal_shelter_id']}")

        if "specie_id" in query_string_params:
            query_string_params["specie_id"] = int(query_string_params["specie_id"])
            log.info(f"Converted specie_id to integer: {query_string_params['specie_id']}")

        if "address_id" in query_string_params:
            query_string_params["address_id"] = int(query_string_params["address_id"])
            log.info(f"Converted address_id to integer: {query_string_params['address_id']}")
        
        # For any other keys that have digit values, convert them to integer
        for key, value in query_string_params.items():
            if key not in ["pet_id", "animal_shelter_id", "specie_id", "address_id"]:
                try:
                    if value.isdigit():
                        query_string_params[key] = int(value)
                        log.info(f"Converted {key} to integer: {query_string_params[key]}")
                except (AttributeError, ValueError):
                    # Value is not a string or can't be converted to int
                    pass

    except Exception as e:
        http_error = HttpErrors.error_400()
        log.error(f"Bad Request: Error processing query parameters - {str(e)}")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    try:
        body = None
        if request.method in ['POST', 'PUT', 'PATCH']:
            if request.is_json:
                body = request.get_json()
                log.info(f"Request body for {request.method}: {body}")
            else:
                log.warning(f"{request.method} request without JSON content-type")
                body = request.data if request.data else None
        else:
            # For GET, DELETE, etc., body is typically None
            log.info(f"{request.method} request - no body expected")
        # Create HttpRequest with correct parameter names
        http_request = HttpRequest(
            headers=request.headers, 
            body=body, 
            query_params=query_string_params,
            path_params=request.view_args if hasattr(request, 'view_args') else None,
            url=request.url,
            ipv4=request.remote_addr
        )

        response = api_route.route(http_request)
        log.info("Request processed successfully")

    except IntegrityError as e:
        http_error = HttpErrors.error_409()
        log.error(f"Conflict Error: Integrity constraint violated - {str(e)}")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    except Exception as e:
        http_error = HttpErrors.error_500()
        log.error(f"Internal Server Error occurred - {str(e)}")
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    log.info("Response generated successfully")
    return response