# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import celery
from kombu import Queue, Exchange
from ufmw import config


def get_celery_queues():
    """动态生成celery queues"""
    queues_list = []
    for k in config.SPIDER_MAP:
        q = Queue(name=k, exchange=Exchange(k), routing_key=k)
        queues_list.append(q)
    return queues_list


app = celery.Celery('ufmw', include=['ufmw.celery.tasks'],)
app.config_from_object('celeryconfig')
celery_queues = tuple(get_celery_queues())
app.conf.update(CELERY_QUEUES=celery_queues)
