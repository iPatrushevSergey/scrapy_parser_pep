from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOGGER_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
LOG_FORMAT_WITH_NAME = ('"%(asctime)s - %(name)s - '
                        '[%(levelname)s] - %(message)s"')
ERROR_TEXT = 'An error has occured: '
