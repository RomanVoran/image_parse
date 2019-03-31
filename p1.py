import random
import urllib
from urllib import request

url = 'http://i.imgur.com/mqvd4.jpg'



def download_web_images(url):

    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_images(url)