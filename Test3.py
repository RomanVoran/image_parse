from urllib import request
import requests

url1 = 'https://imgur.com/aaa1'
url2 = 'https://imgur.com/vhjda2'
url3 = 'https://imgur.com/vhja4'
url4 = 'https://imgur.com/vhja2'
url5 = 'https://imgur.com/vhja0'
url6 = 'https://imgur.com/yasl5'

r = requests.get(url6)

a = str(r)
print(a[11])