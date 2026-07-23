import logging
import os
from logging.handlers import RotatingFileHandler

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("ApplicationLogger")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# File Handler (Rotates after 5 MB)
file_handler = RotatingFileHandler(
    "logs/application.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=5,
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add Handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def divide(a, b):
    logger.info(f"Dividing {a} by {b}")
    return a / b


def database():
    logger.info("Connecting to database...")
    logger.debug("Loading configuration...")
    logger.warning("Database connection is slow.")
    logger.info("Connected successfully.")


def file_operation():
    filename = "sample.txt"

    try:
        with open(filename, "r") as file:
            logger.info(f"Reading file: {filename}")
            print(file.read())

    except FileNotFoundError:
        logger.error(f"File '{filename}' not found.")

    except Exception:
        logger.exception("Unexpected error while reading file.")


def calculate():
    try:
        print(divide(100, 5))
        print(divide(10, 0))
    except Exception:
        logger.exception("Division failed.")


def main():
    logger.info("========== Application Started ==========")

    database()

    file_operation()

    calculate()

    logger.info("Application finished successfully.")


if __name__ == "__main__":
    main()
