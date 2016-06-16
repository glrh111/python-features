# -*- coding: utf-8 -*-
import sys
import mechanize


'''
refer To :
http://blog.csdn.net/zhaodedong/article/details/46432921
'''
# create Browser
br = mechanize.Browser()

# options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# br.set_debug_http(True)
# br.set_debug_redirects(True)
# br.set_debug_responses(True)


# set headers
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]

# raise an HTTP request
response1 = br.open('https://www.google.com/')
# get forms
for f in br.forms():
    print f

br.select_form(nr = 0)

# search
br.form['q'] = 'hello'
br.submit()

# search for res
print br.response().read()

# nice!