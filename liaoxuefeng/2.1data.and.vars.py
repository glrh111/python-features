#! /usr/bin/python
# -*- coding: utf-8 -*-


class Visitor(object):

    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_info(self):
        print '%s: %s' % (self.__name, self.__age)

# 下面是一些实例
wangli = Visitor('wangli', 21)
wangli.print_info()
