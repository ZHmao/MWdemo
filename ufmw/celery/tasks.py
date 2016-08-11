# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
import redis
from ufmw.celery.celery import app
from ufmw.celery import distribute
from ufmw import config


r = redis.StrictRedis(host=config.CELERY_HOST, port=config.CELERY_PORT, db=config.CELERY_DB)


def get_count_of_retries(hkey_name, task_id):
    count = 0
    if r.hexists(name=hkey_name, key=task_id):
        count = r.hget(name=hkey_name, key=task_id) or 0
    return int(count)


def set_count_of_retries(hkey_name, task_id, value):
    r.hset(name=hkey_name, key=task_id, value=value)


def remove_name_from_hkey(hkey_name, task_id):
    r.hdel(hkey_name, task_id)


def put_in_exception_queue(queue_name, value):
    r.lpush(queue_name, value)


@app.task(bind=True)
def do_all_task(self, **kwargs):
    request = self.request
    delivery_info = request.delivery_info
    routing_key = delivery_info.get('routing_key')
    try:
        distribute.distribute_task(routing_key=routing_key, **kwargs)
    except Exception, e:
        # self.retry(exc=e, countdown=2, max_retries=3)
        # 目前使用routing_key
        task_id = request.id
        count = get_count_of_retries(hkey_name=config.RETRY_DICT, task_id=task_id)
        if count < config.MAX_RETRIES:
            count += 1
            set_count_of_retries(hkey_name=config.RETRY_DICT, task_id=task_id, value=count)
            self.apply_async(task_id=task_id, queue=routing_key, kwargs=kwargs)
        else:
            # 达到最大尝试次数，放入异常数据队列
            remove_name_from_hkey(hkey_name=config.RETRY_DICT, task_id=task_id)
            exception_task_info = {
                'exception_msg': e.message,
                'kwargs': kwargs
            }
            value = json.dumps(exception_task_info)
            put_in_exception_queue(config.EXCEPTION_QUEUE, value)
