import os
from dotenv import load_dotenv

load_dotenv()

jwt_config = {
    "TOKEN_KEY": os.getenv("TOKEN_KEY", "my_secret_key"),
    "EXP_TIME_MIN": int(os.getenv("EXP_TIME_MIN", "30")),
    "REFRESH_TIME_MIN": int(os.getenv("REFRESH_TIME_MIN", "10")),
}
