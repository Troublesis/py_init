import sys

from loguru import logger

from config.config import settings


def my_filter(record):
    # Exclude log messages with level 'DEBUG'
    if record["level"].name == "ERROR":
        pass
    return record["level"].name != "DEBUG"


normal_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level: <8}</level> {module}:{function}:{line: <3} {message}"
error_format = "<red>{time:YYYY-MM-DD HH:mm:ss}</red> [ERROR] {module}:{function}:{line: <3} {message}"

# https://pypi.org/project/loguru/
logger.remove()  # Remove the default logger


filter = settings.get("DEBUG", False)
if filter:
    filter = None
else:
    filter = my_filter

logger.add(
    sys.stderr,
    format=normal_format,
    level="DEBUG",
    filter=filter,
)
logger.add(
    "logs/access.log", rotation="100 MB", retention="7 days", format=normal_format
)
logger.add("logs/error.log", level="ERROR", rotation="100 MB", format=error_format)

if __name__ == "__main__":
    logger.info("Hello World!")
    logger.debug("This is a debug message")
    logger.warning(f"Warning: Something wrong")
    logger.error("Something went wrong.")
    logger.critical("Critical error!")
