# -*- coding: utf-8 -*-
import unittest
import requests

picname = '../img/32.jpg'

uri = 'http://www.chuantupian.com/4/uploads/2016/05/IMG_20160530_225850.jpg'

response = requests.get(uri)

with open(picname, 'wb+') as f:
    f.write(response.content)