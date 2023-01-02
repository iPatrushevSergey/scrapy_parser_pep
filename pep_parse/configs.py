import logging
from logging.handlers import RotatingFileHandler

from pep_parse.constants import BASE_DIR, LOG_FORMAT, LOGGER_DATETIME_FORMAT


def configure_logging() -> None:
    """
    Creates a `parser.log` file, a handler and configures
    basic settings.
    """
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'parser.log'
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5
    )
    logging.basicConfig(
        datefmt=LOGGER_DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
