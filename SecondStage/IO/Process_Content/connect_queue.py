from multiprocessing import Process,Queue
from random import randint

#通过信息队列方式通信，先入队的先访问
q = Queue()

def handle():
    for i in range(6):
        data = randint(1,33)
        q.put(data)
        print(data)
    q.put(randint(1,16))


def request():
    for i in range(6):
        data = q.get()
        print(data,end=",")


p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()

