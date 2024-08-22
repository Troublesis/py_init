from config.config import settings
from logger import logger


def main():
    logger.info("Hello World!")
    logger.debug("This is a debug message")
    logger.warning("Warning: Something %s", "might")
    logger.error("Something went wrong.")
    logger.critical("Critical error!")


if __name__ == "__main__":
    main()
