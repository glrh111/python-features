# -*- coding: utf-8 -*-
import logging

# 日志级别level：criticle > error > warning > info > debug > notset
# logging.warning('content')

logging.basicConfig(level = logging.DEBUG,
	format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	datefmt = '%a, %Y %b %d %H:%M:%S',
	# filename = 'myapp.log',
	# filemode='w'
	)

logging.debug('hhh, test')
logging.info('nihaoa')
