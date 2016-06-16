# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup

import random, time
import sys

from models import session, Hot

class Func:
	func_name = sys._getframe().f_back.f_code.co_name
	line_number = sys._getframe().f_back.f_lineno   

class Qiushibaike:
	# http://www.qiushibaike.com/hot/page/2/
	HOT_BASE_URL = 'http://www.qiushibaike.com/hot/page/'

def build_url(num):
	'''
	build_url(num)
	num : page num
	return : page url
	'''
	return Qiushibaike.HOT_BASE_URL + str(num)

def get_content_soup_from_url(url):
	'''
	get_content_from_url(url)
	url : page url
	return : requests.get(url).content
	'''
	try:
		response = requests.get(url)
		return BeautifulSoup(response.content.decode('utf-8', \
			'ignore'), 'html.parser', from_encoding='utf-8')
	except:
		raise

def get_page_amount():
	'''
	get_page_amount()
	return : amount of page, according to buttons on the bottom
	'''
	try:
		url = build_url(1)
		soup = get_content_soup_from_url(url)

		page_amount_tag = soup.find_all('span', [u'page-numbers'])[-1]

		return int(unicode(page_amount_tag.string))
	except:
		raise

def get_content_from_page(url):
	'''
	get_content_from_page(url)
	url : page url
	return : list of (author, content)
	'''
	content_lst = []
	try:
		page_url = url
		soup = get_content_soup_from_url(url)
	except:
		print u'Error accors because GETTING SOUP in: %s' % Func.func_name
	else:
		try:
			content_tags = soup.find_all('div', \
				[u'article', u'block', u'untagged', u'mb15'])
		except:
			print u'Error in parsing content from soup'
		else:
			for tag in content_tags:
				try:
					author = tag.h2.string
					content = (tag.find_all('div')[1]).string
					content_lst.append((author, content))
				except:
					continue
	finally:
		return content_lst

def get_whole_page_content(amount):
	'''
	get_whold_page_content()
	amount : get_page_amount()
	return : write sqlite
	'''
	count = 0
	for page_num in range(1, amount+1):
		print u'Scraping page <%3d>...' % page_num


		url = build_url(page_num)

		print u'Now in: %s' % url

		# get page_content
		content_lst = get_content_from_page(url)

		print u'Get <%3d> pices from this page.\n' % len(content_lst)

		for author, content in content_lst:
			content_obj = Hot(author=author, content=content)
			session.add(content_obj)
			count += 1

		if count >= 100:
			session.commit()
			count = 0

		# couldn't be too soon
		time.sleep(3)

	session.commit()
	return 





if __name__ == '__main__':
	# amount = get_page_amount()
	# get_whole_page_content(amount)	
	for instance in session.query(Hot).all():
		print instance.author
		print instance.content
		time.sleep(0.5)