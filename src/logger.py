import sys

from loguru import logger


def my_filter(record):
    # Exclude log messages with level 'DEBUG'
    if record["level"].name == "ERROR":
        pass
    return record["level"].name != "DEBUG"


# https://pypi.org/project/loguru/
logger.remove()  # Remove the default logger
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level: <8}</level> {module}:{function}:{line: <3} {message}",
    level="INFO",
    filter=my_filter,
)
logger.add("logs/access.log", rotation="100 MB", retention="7 days")

if __name__ == "__main__":
    logger.info("Hello World!")
    logger.debug("This is a debug message")
    logger.warning(f"Warning: Something wrong")
    logger.error("Something went wrong.")
    logger.critical("Critical error!")
