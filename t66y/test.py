# -*- coding: utf-8 -*-
from lib.models import *
from lib.spider import *
from lib.mail import *
import time
# use session. session.add(), session.commit()

# new = Fiction(title=u'你好啊a', content=u'很黄很暴力a')
# session.add(new)
# session.commit()

for idx, instance in enumerate(session.query(Fiction).filter(Fiction.id>330)):
    print '\n'
    try:
        print instance.id
        print instance.title[0]
        print instance.add_time
        print u'正在发送第 <%3d> 封邮件...' % (idx+1)
        send_email('good', instance.content)
    except:
        print u'发送失败 <%3d> :-(' % (idx+1)
    else:
        print u'发送成功 <%3d> :-)' % (idx+1)
    finally:
        time.sleep(60)


# if __name__ == '__main__':
#     for diyiceng in range(1, 30):
#         prefix, lst = get_fiction_url_pool(diyiceng)
#         length = len(lst)
#         for idx, endfix in enumerate(lst): 

#             try:
#                 url = prefix + endfix
#                 print u'\n正在读取第 <%3d> 个网页, 剩余 <%3d> 个网页...' % ((diyiceng-1)*length+idx+1, (31-diyiceng)*length+length-idx-1)
#                 print url
#                 title, content = get_fiction(url)
#                 print title.encode('gbk')
#             except:
#                 print '<%3d> There has been an error :(' % (idx+1)
#             else:
#                 # save to the db
#                 try:
#                     new_fiction = Fiction(title=title, content=content)
#                 except:
#                     pass
#                 else:
#                     session.add(new_fiction)
#                     print u'成功添加至数据库'
#                     if idx % 20 == 0:
#                         session.commit()
#             time.sleep(1)
#                 # print content.encode('gbk')
#         session.commit()

