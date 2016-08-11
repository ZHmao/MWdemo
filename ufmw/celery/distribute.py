# -*- coding: utf-8 -*-
"""
根据消息队列名称进行任务分发
"""
from __future__ import absolute_import, unicode_literals

import importlib
from ufmw import config


def distribute_task(**kwargs):
    routing_key = kwargs.get('routing_key')
    start = get_starter(routing_key)
    if start is None:
        print 'log it, cant find the starter'
    start(**kwargs)


def get_starter(routing_key):
    spider_module_name = config.SPIDER_MAP.get(routing_key)
    absolute_module_name = config.SPIDER_HOME + "." + spider_module_name
    func_name = config.SPIDER_FUNC
    return get_func_obj(func_name, absolute_module_name)


def get_func_obj(func_name, absolute_module_name):
    try:
        spider_module = importlib.import_module(absolute_module_name)
    except AttributeError, e:
        pass
    start_obj = None
    if hasattr(spider_module, func_name):
        start_obj = getattr(spider_module, func_name)
    return start_obj
