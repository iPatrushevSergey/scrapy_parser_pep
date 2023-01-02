import logging

from pep_parse.constants import LOG_FORMAT, LOGGER_DATETIME_FORMAT

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}

LOG_FILE = 'logs/logs.py'
LOG_LEVEL = logging.INFO
LOG_FORMAT = LOG_FORMAT
LOG_DATEFORMAT = LOGGER_DATETIME_FORMAT
