# -*- coding: utf-8 -*-
import urllib2
from PIL import Image
import StringIO
import re

request = urllib2.Request('http://www.pythonchallenge.com/pc/def/oxygen.png')
response = urllib2.urlopen(request)

img = Image.open(StringIO.StringIO(response.read()))

width, height = img.size

print u'图片宽 %d 像素，高 %d 像素' % (width, height)

# guess the steps
gray_lst = [img.getpixel((wid, height/2))[0] for wid in range(0, width, 7)]

tip = ''.join(map(chr, gray_lst))

print tip

# from tip get the result lst 
pattern = re.compile(r'.*?\[([0-9,\s]+)\]')

match = pattern.match(tip)

buhuo = match.group(1)

buhuo_lst = map(int, re.split(r'[\s,]+', buhuo))



print buhuo_lst
print ''.join(map(chr, buhuo_lst))


