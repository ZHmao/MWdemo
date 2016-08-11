# -*- coding: utf-8 -*-

import time


def start(**kwargs):
    uuid = kwargs.get('uuid')
    msg = kwargs.get('msg')
    print 'workb start......'
    time.sleep(5)
    print msg
    print 'workb finished......'
