# -*- coding: utf-8 -*-

import time


def start(**kwargs):
    uuid = kwargs.get('uuid')
    msg = kwargs.get('msg')
    print 'worka start......'
    print msg
    time.sleep(5)
    raise AttributeError('test error')
