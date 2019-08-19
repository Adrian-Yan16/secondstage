"""
通过创建二级子进程处理僵尸进程
"""
import os
from time import sleep

def parent():
    for i in range(3):
        sleep(2)
        print("写代码")

def child():
    for i in range(2):
        sleep(3)
        print("测代码")

pid = os.fork()

if pid < 0:
    print("fail")
elif pid == 0:
    print("c0 id:",os.getpid())
    cid = os.fork()
    if cid == 0:
        print("next_c id ：",os.getpid())
        print("c id:",os.getppid())
        child()
    else:
        os._exit(0)
else:
    os.wait()
    parent()