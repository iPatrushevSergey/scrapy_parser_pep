import logging

from pep_parse.constants import LOG_FORMAT_WITH_NAME, LOGGER_DATETIME_FORMAT

pep_logger = logging.getLogger('PEP logger')
file_handler = logging.StreamHandler()
formatter = logging.Formatter(
    LOG_FORMAT_WITH_NAME,
    datefmt=LOGGER_DATETIME_FORMAT
)
file_handler.setFormatter(formatter)
pep_logger.addHandler(file_handler)


pipelines_logger = logging.getLogger('Pipelines logger')
file_handler = logging.StreamHandler()
formatter = logging.Formatter(
    LOG_FORMAT_WITH_NAME,
    datefmt=LOGGER_DATETIME_FORMAT
)
file_handler.setFormatter(formatter)
pipelines_logger.addHandler(file_handler)
