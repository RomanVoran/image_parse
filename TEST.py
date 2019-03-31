import random
import threading

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


class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__(self, name="threddy" + num)
        self.num = num
    def run(self):
        print ("Thread ", self.num),

thread1 = MyThread("1")
thread2 = MyThread("2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()