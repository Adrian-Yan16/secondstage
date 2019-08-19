import os
import time

print("让子弹飞一会儿")
a = 1
#创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")

#子进程执行
elif pid == 0:
    print("a:",a)
    print("The new process")
    a = 100

#父进程执行
else:
    time.sleep(1)
    print("a:",a)
    print("The old process")

#父子进程均执行
print("Fork test over")