# -*- coding: utf-8 -*-
import requests
import urllib

uri = 'https://downloads.mongodb.com/compass/stable/MongoDB_Compass.Setup-1.1.5-win32-x64.exe'

response = requests.get(uri)

with open('win32.exe', 'wb+') as f:
    f.write(response.content)
