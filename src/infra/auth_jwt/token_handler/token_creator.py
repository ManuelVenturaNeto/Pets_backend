import logging
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

        self.log = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )

    def create(self, uid: int) -> str:
        """
        Return JWT
        :param  - uid: animal_shelter identify
        :return - string with token
        """
        self.log.info(f"Creating token for UID: {uid}")
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

            self.log.info(f"Refreshing token for UID: {uid}")
            return self.__encode_token(uid=uid)

        self.log.info(f"Token for UID: {uid} does not require refresh.")
        return token



    def __encode_token(self, uid: int):
        """
        Encode and creating an jwt with payload
        :param  - uid: animal_shelter identify
        :return - string with token
        """

        validate_entry = isinstance(uid, int)

        if validate_entry:
            self.log.info(f"Encoding token for UID: {uid}")
            return jwt.encode(
                {
                    "uid": uid,
                    "exp": datetime.now(tz=timezone.utc)
                    + timedelta(minutes=self.__EXP_TIME_MIN),
                },
                key=self.__TOKEN_KEY,
                algorithm="HS256",
            )
        self.log.error("UID must be an integer to encode token.")
        return None
