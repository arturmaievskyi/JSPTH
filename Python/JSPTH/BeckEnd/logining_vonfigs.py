# logging_config.py

import logging

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("session_audit.log"),
            logging.StreamHandler(),
        ],
    )

