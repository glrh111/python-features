# -*- coding: utf-8 -*-
from lib.models import *
from lib.spider import *
from lib.mail import *
import time
import random
import re
import cookielib

import urllib

import requests

# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener() #urllib2.HTTPCookieProcessor(cookie))
# opener.addheaders.append(('Cookie', '__cfduid=d6c19704909712c5d08b92f2d7b8c3c7e1465003094'))
# urllib2.install_opener(opener)
'''
GET /4/uploads/2016/05/IMG_20160530_230148.jpg HTTP/1.1
Host: www.chuantupian.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4
Cookie: __cfduid=d6c19704909712c5d08b92f2d7b8c3c7e1465003094
'''

headers = {
        'Host': 'www.chuantupian.com',
        
        'If-Modified-Since' : 'Tue, 31 May 2016 07:33:41 GMT',
        'If-None-Match':'"574d3e55-eb56"',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
        'Cookie' : '__cfduid=d6c19704909712c5d08b92f2d7b8c3c7e1465003094',
    }

uri = 'http://www.chuantupian.com/4/uploads/2016/05/IMG_20160530_230148.jpg'



# request = urllib2.Request(uri, '', headers)

# response = urllib2.urlopen(request, timeout=10)



response = requests.get(uri)



with open('luanqide.jpg', 'wb+') as f:
    f.write(response.content)