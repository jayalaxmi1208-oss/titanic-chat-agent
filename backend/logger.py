import logging
import os

def setup_logger():
    logger = logging.getLogger("titanic_agent")
    logger.setLevel(logging.INFO)

    # Get absolute path of backend folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(base_dir, "app.log")

    file_handler = logging.FileHandler(log_path)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger