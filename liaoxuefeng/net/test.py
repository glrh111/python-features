#! /usr/bin/env
# -*- coding: utf-8 -*-


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print '[CONSUMER] Consumer %s...' % n
        r = '200 OK'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print '[PRODUCER] Producer %s...' % n
        r = c.send(n)
        print '[PRODUCER Consumer return: %s' % r
    c.close()

c = consumer()
producer(c)
