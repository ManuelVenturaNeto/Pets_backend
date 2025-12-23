import os
import logging
import subprocess
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s, %(message)s",
    # filename="./pipeline_logs.log",
)


def run_docker_commands() -> None:
    """
    Build and push the Docker image to Artifact Registry.
    """
    image_name = str(os.getenv("ARTIFACT_PATH"))

    try:
        # Build image without cache
        logging.debug("Building Docker image...")
        subprocess.run(
            ["docker", "build", "--no-cache", "-t", image_name, "."],
            check=True,
        )

        # Push image
        logging.debug("Pushing Docker image to Artifact Registry...")
        subprocess.run(
            ["docker", "push", image_name],
            check=True,
        )

        logging.debug("Build and push completed successfully!")

    except subprocess.CalledProcessError as error:
        logging.debug(f"Error executing command: {error}")


if __name__ == "__main__":
    run_docker_commands()
