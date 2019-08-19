from multiprocessing import Process
from time import sleep
import signal

#signal.signal(signal.SIGCHLD,signal.SIG_IGN)

#multiprocessing创建的子进程无法使用标准输入即input
def th1():
    sleep(2)
    print("老二")

def th2():
    sleep(1)
    print("老大")

def th3():
    sleep(4)
    print("老小")

things = [th1,th2,th3]
jobs = []

for i in things:
    p = Process(target=i)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

def th4(seconds,name):
    sleep(seconds)
    print("My name is ",name)

p = Process(target=th4,args=(2,"Tony"))
p.daemon = True#父进程结束后，子进程随之结束，不与join一起用
p.start()

#如果无法用join回收，则可以用signal回收
#p.join()
