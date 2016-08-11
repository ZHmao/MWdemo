# -*- coding: utf-8 -*-


CELERY_HOST = 'localhost'

CELERY_PORT = 6379

CELERY_DB = 0

RETRY_DICT = 'dict:count:retry'

MAX_RETRIES = 3

EXCEPTION_QUEUE = 'queue:exception:tasks'

SPIDER_MAP = {
    'queue:task:worka': 'worka',
    'queue:task:workb': 'workb',
    'queue:task:workc': 'workc',
}

SPIDER_HOME = 'ufmw.worker'

SPIDER_FUNC = 'start'
