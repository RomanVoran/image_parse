import random
import urllib
from urllib import request
import requests
import threading


max_pic = 10

def ranCh():
    return chr(random.randrange(97, 122))

def ranNum():
    return str(random.randrange(0, 9))

def switch(x):
    return {
        1: [ranCh(),ranCh(),ranCh(),ranCh(),ranNum()],
        2: [ranCh(),ranCh(),ranCh(),ranNum(),ranCh()],
        3: [ranCh(),ranCh(),ranNum(),ranCh(),ranCh()],
        4: [ranCh(),ranNum(),ranCh(),ranCh(),ranCh()],
        5: [ranNum(),ranCh(),ranCh(),ranCh(),ranCh()],
        6: [ranCh(),ranCh(),ranCh(),ranCh(),ranCh()],
    }[x]

def findImages(max_pic,gg):
    num = 0
    while num<=max_pic:
        name = []
        url = []
        a = []

        name = switch(random.randrange(1,6))
        name = ''.join(name)
        url = 'http://i.imgur.com/' + name + '.jpg'
        urs_page = 'https://imgur.com/' + name
        r = requests.get(urs_page)
        a = str(r)
        if a[11]=="2":
            print("Yep!")
        else:
            print("Nope :(")
        if a[11]=="2":
            print(url)
            fail_name = 'goga/' + str(name) + ".jpg"
            urllib.request.urlretrieve(url,fail_name)
            num = num + 1


t1 = threading.Thread(target=findImages, args=(max_pic, 1))
t1.start()
t1.join()

t2 = threading.Thread(target=findImages, args=(max_pic,1))
t2.start()
t2.join()

t3 = threading.Thread(target=findImages, args=(max_pic,1))
t3.start()
t3.join()

t4 = threading.Thread(target=findImages, args=(max_pic,1))
t4.start()
t4.join()

t5 = threading.Thread(target=findImages, args=(max_pic,1))
t5.start()
t5.join()

t6 = threading.Thread(target=findImages, args=(max_pic,1))
t6.start()
t6.join()

t7 = threading.Thread(target=findImages, args=(max_pic,1))
t7.start()
t7.join()

t8 = threading.Thread(target=findImages, args=(max_pic,1))
t8.start()
t8.join()


