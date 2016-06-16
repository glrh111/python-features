from PIL import Image
import urllib2
import StringIO

request = urllib2.Request('http://www.pythonchallenge.com/pc/return/cave.jpg')

# with Authorization
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'info=you+should+have+followed+busynothing...'))
opener.addheaders.append(('Authorization', 'Basic aHVnZTpmaWxl'))
urllib2.install_opener(opener)

response = urllib2.urlopen(request)

img_in_mem = StringIO.StringIO(response.read())

img = Image.open(img_in_mem)

print img.size

w, h = img.size

for i in range(w):
    for j in range(h):
        if (i+j) % 2 != 1:
            # replace the odd color
            img.putpixel((i, j), 0)

img.save('1158081.png')