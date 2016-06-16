import StringIO
import urllib2
headers = {
    'Authorization': 'Basic aHVnZTpmaWxl',
}

request1 = urllib2.Request('http://www.pythonchallenge.com/pc/return/evil2.gfx', '', headers)

# request2 = urllib2.Request('http://www.pythonchallenge.com/pc/return/evil4.jpg', '', headers)

response = urllib2.urlopen(request1)

gfx = response.read()

gfx_in_mem = StringIO.StringIO(gfx)

# with open('12evil.gfx', 'w') as f:
#     f.write(gfx)

types = ['jpg', 'png', 'gif', 'png', 'jpg']

for i in range(5):
    with open('12evil-%s.%s' % (i, types[i]), 'wb+') as f:
        f.write(gfx[i::5])

# re : dis pro port ional ity

