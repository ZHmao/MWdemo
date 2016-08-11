# -*- coding: utf-8 -*-

import time


def start(**kwargs):
    uuid = kwargs.get('uuid')
    msg = kwargs.get('msg')
    print 'workc start......'
    time.sleep(5)
    print msg
    print 'workc finished......'
