#coding: UTF-8
from threading import Thread

def goga(fs,ss):
    ss = ss +1
    print(fs)

t1 = Thread(target=goga, args=('test2.txt',1))
t2 = Thread(target=goga, args=('415',1))

t1.start()
t2.start()
t1.join()
t2.join()