#! /usr/bin/env python
# -*- coding: utf-8 -*-

' a test module'

__author__ = 'wang li'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print 'Hello, world!'
	elif len(args) == 2:
		print 'Hello, %s!' % args[1]
	else:
		print 'Too many args!'

if __name__ == '__main__':
	test()
