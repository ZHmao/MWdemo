# -*- coding: utf-8 -*-
from kombu import Queue, Exchange

BROKER_URL = 'redis://localhost:6379/0'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_QUEUES = (
#     Queue(name='default', exchange=Exchange('default'), routing_key='default'),
#     Queue(name='for_task_a', exchange=Exchange('for_task_a'), routing_key='for_task_a'),
#     Queue(name='for_task_b', exchange=Exchange('for_task_b'), routing_key='for_task_b'),
#     Queue(name='for_task_b', exchange=Exchange('for_task_c'), routing_key='for_task_c'),
# )
#
# CELERY_ROUTES = {
#     'ufmw.celery.tasks.do_task_a': {'queue': 'for_task_a', 'routing_key': 'for_task_a'},
#     'ufmw.celery.tasks.do_task_b': {'queue': 'for_task_b', 'routing_key': 'for_task_b'},
#     'ufmw.celery.tasks.do_task_c': {'queue': 'for_task_c', 'routing_key': 'for_task_c'},
# }
