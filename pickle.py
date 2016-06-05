import urllib2
import re
import pickle

def get_ch(s):
    url = 'http://www.pythonchallenge.com/pc/def/' + s
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response

banner = get_ch('banner.p').read()

data = pickle.loads(banner)

with open('tmp.txt','a') as f:
    re = ''
    for i in data :
        for j in i:
            re += j[0] * j[1] 
        re += '\n'
    f.write(re)