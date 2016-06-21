import requests

uri = 'http://www.qiushibaike.com/'

response = requests.get(uri)

print response.content

print