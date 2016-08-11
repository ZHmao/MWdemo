# -*- coding: utf-8 -*-
"""
api
"""
from __future__ import absolute_import, unicode_literals

import json
from ufmw.celery.tasks import do_all_task


def push_task_in_the_queue(json_tasks):
    """
    填充任务
    :param json_tasks:
            serialized by json.
            example:    task = {'queue_name': 'queue:task:worka', 'kwargs': {'msg': 'this is a task'}}
                        tasks = [task,]
    :return: None or number of inserted
    """
    task_count = 0
    if not json_tasks:
        return

    list_tasks = json.loads(json_tasks)
    if not isinstance(list_tasks, list) or len(list_tasks) <= 0:
        return
    for task in list_tasks:
        if not isinstance(task, dict):
            continue
        queue_name = task.get('queue_name')
        kwargs = task.get('kwargs')
        do_all_task.apply_async(kwargs=kwargs, queue=queue_name)
        task_count += 1
    return task_count
