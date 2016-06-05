# -*- coding: utf-8 -*-

from lib.models import *
from lib.spider import *
from lib.mail import *
import time
import random
import re
import urllib2




headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        # 'Upgrade-Insecure-Requests' : 1,
        # 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }

uri = 'http://www.chuantupian.com/4/uploads/2016/05/IMG_20160530_230148.jpg'


