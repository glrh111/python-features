import zipfile
import StringIO
import urllib2
import re 

request = urllib2.Request('http://www.pythonchallenge.com/pc/def/channel.zip')

response = urllib2.urlopen(request)

try:
    string_in_mem = StringIO.StringIO(response.read())
    zip_from_mem = zipfile.ZipFile(string_in_mem)
    # print zip_from_mem.namelist()
    print zip_from_mem.getinfo(zip_from_mem.namelist()[-2]).comment
except:
    raise
# finally:
#     if string_in_mem:
#         string_in_mem.close()

# clear my brain
# all file list : z.namelist() 
# file content : z.read('filename')
# comment : z.getinfo('filename').comment       
# 1. notice is in the readme.txt

pattern = re.compile(r'Next nothing is (\d+)')



def next_num(now_num):
    # shi bai
    now_content = zip_from_mem.read('%s.txt' % now_num)
    match = pattern.match(now_content)
    if match is not None:
        return match.group(1)
    raise

num_lst = []
now_num = 90052
while True:
    try:
        num_lst.append(now_num)
        now_num = next_num(now_num)
    except:
        break
    finally:
        print now_num
        print zip_from_mem.read('%s.txt' % now_num)



# 2. collect the comment
comments = ''.join([zip_from_mem.getinfo('%s.txt' % zip_file).comment for zip_file in num_lst])

with open('6channel.txt', 'w') as f:
    f.write(comments)
