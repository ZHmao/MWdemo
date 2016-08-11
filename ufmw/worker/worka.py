# -*- coding: utf-8 -*-

import time


def start(**kwargs):
    uuid = kwargs.get('uuid')
    msg = kwargs.get('msg')
    print 'worka start......'
    time.sleep(5)
    print msg
    raise AttributeError('test error')
    print 'worka finished......'
