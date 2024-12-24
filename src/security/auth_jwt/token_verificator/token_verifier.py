import os
from functools import wraps
import jwt
from flask import jsonify, request
from src.infra.repo.user_repository import UserRepository
from src.data.find_user import FindUser
from src.security.auth_jwt.token_handler import token_creator


def token_verify(function: callable) -> callable:
    """Checking the valid Token and refreshing it. If not valid, return
    Info and stopping client request
    :parram - http request.headers: (Username / Token)
    :return - Json with the corresponding information.
    """

    @wraps(function)
    def decorated(*arg, **kwargs):
        raw_token = request.headers.get("Authorization")
        name = request.args.get("name")

        user_repo = UserRepository()
        find_user = FindUser(user_repo)

        user_response = find_user.by_name(name=name)
        user = user_response["Data"][0]
        uid = user.id

        # Without Token
        if not raw_token and not uid:
            return jsonify({"error": "Bad Request"}), 400

        try:
            token = raw_token.split()[1]
            token_information = jwt.decode(
                token, key=str(os.getenv("TOKEN_KEY")), algorithms="HS256"
            )
            token_uid = token_information["uid"]

        except jwt.ExpiredSignatureError:
            return (
                jsonify(
                    {
                        "message": "Token is Expired",
                    }
                ),
                401,
            )

        except jwt.InvalidSignatureError:
            return (
                jsonify(
                    {
                        "message": "Token is invalid",
                    }
                ),
                401,
            )

        except KeyError:
            return (
                jsonify(
                    {
                        "message": "Token is invalid",
                    }
                ),
                401,
            )

        if uid and token_uid and (int(token_uid) != int(uid)):
            return (
                jsonify(
                    {
                        "message": "User Unauthorized",
                    }
                ),
                401,
            )

        next_token = token_creator.refresh(token)

        return function(next_token, *arg, **kwargs)

    return decorated
