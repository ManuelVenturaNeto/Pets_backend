# pylint: disable=C0115, C0103

import time
from datetime import datetime, timedelta, timezone
import jwt


class TokenCreator:
    """
    Class to define Auth Token
    """

    def __init__(self, token_key: str, exp_time_min: int, refresh_time: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time

    def create(self, uid: int) -> str:
        """
        Return JWT
        :param  - uid: animal_shelter identify
        :return - string with token
        """

        return self.__encode_token(uid=uid)

    def refresh(self, token: str) -> str:
        """
        Function to create initial token when logging
        :parram - string with token
        :return - string with token
        """

        token_information = jwt.decode(token, key=self.__TOKEN_KEY, algorithms="HS256")
        uid = token_information["uid"]
        exp_time = token_information["exp"]

        if ((exp_time - time.time()) / 60) < self.__REFRESH_TIME_MIN:
            # If token refreshed in more than 15 minutes, new refresh

            return self.__encode_token(uid=uid)

        return token

    def __encode_token(self, uid: int):
        """
        Encode and creating an jwt with payload
        :param  - uid: animal_shelter identify
        :return - string with token
        """

        validate_entry = isinstance(uid, int)

        if validate_entry:
            return jwt.encode(
                {
                    "uid": uid,
                    "exp": datetime.now(tz=timezone.utc)
                    + timedelta(minutes=self.__EXP_TIME_MIN),
                },
                key=self.__TOKEN_KEY,
                algorithm="HS256",
            )

        return None
