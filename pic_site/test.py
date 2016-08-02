# -*- coding: utf-8 -*-
from lib.models import *
from lib.spider import *
from lib.mail import *
import time

import argparse


# use session. session.add(), session.commit()

# new = Fiction(title=u'你好啊a', content=u'很黄很暴力a')
# session.add(new)
# session.commit()

# for idx, instance in enumerate(session.query(Fiction).filter(Fiction.id>330)):
#     print '\n'
#     try:
#         print instance.id
#         print instance.title[0]
#         print instance.add_time
#         print u'正在发送第 <%3d> 封邮件...' % (idx+1)
#         send_email('good', instance.content)
#     except:
#         print u'发送失败 <%3d> :-(' % (idx+1)
#     else:
#         print u'发送成功 <%3d> :-)' % (idx+1)
#     finally:
#         time.sleep(60)


def save_fictions_to_db():

    # amount of the fiction list-page
    last_page_num = get_amount_list_page()
    # print last_page_num
    print u'一共 <%3s> 页待爬取...' % last_page_num
    # all list pages
    for diyiceng in range(1, last_page_num+1):

        # prefix is url_prefix
        prefix, lst = get_fiction_url_pool(diyiceng)
        # length : amount of fictions in one list page
        length = len(lst)

        # one list page
        for idx, endfix in enumerate(lst): 

            try:
                # build url
                url = prefix + endfix
                print u'\n正在读取第 <%3d> 个网页, 剩余 <%3d> 个网页...' % ((diyiceng-1)*length+idx+1, (31-diyiceng)*length+length-idx-1)
                print url
                # get content
                title, content = get_fiction(url)
                print title.encode('gbk')

            except:
                # raise
                print '<%3d> There has been an error :(' % (idx+1)
            else:
                # save to the db
                try:
                    new_fiction = Fiction(title=title, content=content)
                except:
                    # raise
                    pass
                else:
                    session.add(new_fiction)
                    print u'成功添加至数据库'
                    if idx % 20 == 0:
                        session.commit()
            time.sleep(1)
                # print content.encode('gbk')
        session.commit()

def save_images_to_local():

    try:
        last_page_num = get_amount_image_list_page()
    except:
        last_page_num = 100
        
    print u'一共 <%3s> 页待爬取...' % last_page_num

    for page_idx in range(4, last_page_num+1):

        page_url_base, page_lst = get_picture_page_url_pool(page_idx)

        # print page_lst

        if page_lst:
            for page_sub_idx, page_sub in enumerate(page_lst):

                title, pic_lst = get_picture_url_pool(page_url_base+page_sub)
                # print title.encode('gbk')
                # print '\n'.join(pic_lst)
                # print '\n\n'

                print u'正在保存第<%3d>页 - 第<%3d>小页的图片...' % (page_idx+1, page_sub_idx)
                save_pictures(pic_lst, page_idx, page_sub_idx, title)

def send_mails_to_little_partners():

    imgs = os.listdir('img/')[10:]

    def g():
        for idx in range(0, len(imgs), 2):
            yield (imgs[idx], imgs[idx+1])

    g = g()
    for idx, instance in enumerate(session.query(Fiction).filter(Fiction.id>30)):
        print '\n'
        try:
            print instance.id
            print instance.title[0]
            print instance.add_time
            print u'正在发送第 <%3d> 封邮件...' % (idx+1)
            # images
            images = g.next()
            # print type(images)
            print '\n'.join(images)
            print u'START AT: <%s>' % time.ctime()
            send_mail_with_file(instance.content, images)
            print u'END AT: <%s>' % time.ctime()
        except:
            # raise
            print u'发送失败 <%3d> :-(' % (idx+1)
        else:
            print u'发送成功 <%3d> :-)' % (idx+1)
        finally:
            time.sleep(120)

# parsers
parser = argparse.ArgumentParser(description='Get infos from t66y ~~~')
subparsers = parser.add_subparsers(help='Some usefool tools')

# get fictions :
fiction_parser = subparsers.add_parser('fiction', \
    help='Get fictions from t66y~')
fiction_parser.set_defaults(func=save_fictions_to_db)

# get images :
image_parser = subparsers.add_parser('image', \
    help='Get image from somewhere~')
image_parser.set_defaults(func=save_images_to_local)

# send emails with image and text in it
email_parser = subparsers.add_parser('email', \
    help='Send email to friends~')
email_parser.set_defaults(func=send_mails_to_little_partners)

if __name__ == '__main__':
    args = parser.parse_args()
    # print args.__dict__
    args.func()

