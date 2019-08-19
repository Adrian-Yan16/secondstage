from multiprocessing import Process,Semaphore
from time import sleep
from os import getpid

#通过信号量方式管理一次可执行的线程数
sem = Semaphore(3)
def sema():
    sem.acquire()
    print("%s开始"%getpid())
    sleep(1)
    print("%s结束"%getpid())
    sem.release()

for i in range(5):
    p1 = Process(target=sema)
    p1.start()
