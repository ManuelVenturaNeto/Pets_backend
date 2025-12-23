import logging
from src.main.configs import app

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s, %(message)s",
        # filename="./pipeline_logs.log",
    )

    app.run(host="0.0.0.0", port=5000)
