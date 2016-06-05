# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import time
import re
from my_exception import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        # 'Upgrade-Insecure-Requests' : 1,
        # 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }

# tag that is this
def is_this_tag(tag):
    """
    used in get_fiction_url_pool()
    refer to: http://beautifulsoup.readthedocs.io/zh_CN/latest/#id25
    """
    return tag.has_attr('align') and tag.has_attr('class') and tag['align'] == u'center' and tag['class'] == [u'tr3', u't_one']

def get_fiction_url_pool(pagenum=1):
    """
    return prefix, list[url, ...]
    """
    # define returned
    prefix = 'http://t66y.com/'
    url_lst = []
    # get the response
    fiction_list_url = 'http://t66y.com/thread0806.php?fid=20&search=&page=' + str(pagenum)
    request = urllib2.Request(fiction_list_url, '', headers)
    try:
        response = urllib2.urlopen(request, timeout=20)
    except:
        pass
    else:
        html = response.read()
        # get the content
        soup = BeautifulSoup(html, 'html.parser', from_encoding='GB18030')
        tags = soup.find_all(is_this_tag)#'tr', [u'tr3', u't_one'])
        for tmp_tag in tags:
            try:
                tmp_a = tmp_tag.td.a
            except:
                continue
            else:
                tmp_url = tmp_a['href']
                if tmp_url[:3] != 'htm':
                    continue
                url_lst.append(tmp_url)
    finally:
        # return 
        return prefix, url_lst

def get_fiction(url):
    """
    return (title, content)
    """
    title = ''
    content = ''
    # try to raise a request
    request = urllib2.Request(url, '', headers)
    try:
        response = urllib2.urlopen(request, timeout=10)
    except:
        pass
    else:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser', from_encoding='GB18030')
        # obtain tags
        try:    
            content_tags = soup.find_all('div', [u'tpc_content', u'do_not_catch'])

            # build content
            content_tag = content_tags[0]
            # as for content_tag has children, .string return None
            # unicode translate obj. to unicode
            content_generator = content_tag.stripped_strings

            for i in content_generator:
                try:
                    content += '    ' + unicode(i)+'\n'
                except:
                    continue   

            # build title
            title_tag = content_tag.find_parent('td').h4
            title = unicode(title_tag.string)
        except:
            pass
        else:
            pass
    finally:
        return title, content

def get_picture_page_url_pool():
    """
    return list[page_url, ...]
    """
    pass

def get_picture_url_pool(page_url):
    """
    return title, list[url, ...]
    every page is a list
    """
    # construct return value
    title = ''
    pic_lst = []
    # construct the request
    request = urllib2.Request(page_url, '', headers)
    try:
        # raise a HTTP request
        response = urllib2.urlopen(request)
        # analysis the response
    except:
        pass
    else:
        # try to analysis the response
        try:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser', from_encoding='GB18030')
            # the div[0] contains <input src=''>, get the src
            content_tags = soup.find_all('div', [u'tpc_content', u'do_not_catch'])
            content_tag = content_tags[0]
            pic_tags = content_tag.find_all('input', type='image')
            
            for pic_tag in pic_tags:
            # try to get the src of each picture
                try:
                    pic_lst.append(pic_tag['src'])
                except:
                    continue

            # try to get the title of pictures
            try:
                title_tag = content_tag.find_parent('td').h4
                title = unicode(title_tag.string)
            except:
                pass
            
        except:
            pass
        finally:
            pass

    finally:
        return title, pic_lst


def build_pic_name(id_of_this_page, page_title, id_in_this_page, pic_uri):
    """
    filename = id_of_the_page + id_in_this_page + time 
    refer to : http://www.runoob.com/python/python-date-time.html
    """
    time_string = str(id_of_this_page) + ' - ' + page_title + ' - ' + str(id_in_this_page) + ' - ' + str(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

    # try to match the filename
    # don't add space char into regex
    pattern = re.compile(r'.+?\.([a-zA-Z0-9]{1,6})$', re.I)
    try:
        match = pattern.match(pic_uri)
        if match is not None:
            time_string = time_string + '.' + match.group(1)
        else:
            raise Re_failure
    except:
        raise Re_failure
    else:
        return time_string
    



def save_pictures(pic_uris, id_of_this_page, page_title):
    """ 
    save the picture
    recieve : lst of uri
    return : list[filename1, ...]
    name = datetime + - id - + randomnum
    """
    for idx, pic_uri in enumerate(pic_uris):
        # try to raise an HTTP request
        try:
            print u'\n正在请求 %s ...' % pic_uri
            request = urllib2.Request(pic_uri, '', headers)
            response = urllib2.urlopen(request, timeout=10)
            # try to save the picture to local
            try:
                picname = '../img/' + build_pic_name(id_of_this_page, page_title, idx, pic_uri)
                print u'正在保存 %s' % pic_uri
                with open(picname, 'wb+') as f:
                    f.write(response.read())
                print u'成功保存:\n%s' % picname
            except:
                print u'保存失败'
            else:
                picname_lst.append(picname)
        except:
            print u'请求失败...'
            continue



if __name__ == '__main__':
    # get_picture()

    title, pic_lst = get_picture_url_pool('http://t66y.com/htm_data/16/1606/1950866.html')
    print title.encode('gbk')
    print '\n'.join(pic_lst)
    print '\n\n'

    # get_pictures()
    save_pictures(pic_lst, 3, title)
    

