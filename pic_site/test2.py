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
