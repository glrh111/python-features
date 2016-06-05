import urllib2
import re

url = 'http://t66y.com/htm_data/20/1606/1952804.html'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
}
request = urllib2.Request(url, '', headers)

response = urllib2.urlopen(request)

html = response.read()

pattern = re.compile(r'<div\s+class="tpc_content do_not_catch">(.*?)</div>', re.I | re.M)

match = pattern.finditer(html)

pattern2 = re.compile(r'<br>', re.I)
with open('zhao.txt', 'w+') as f:
    for i in match:
        f.write(pattern2.sub('\n', i.group(1)))

