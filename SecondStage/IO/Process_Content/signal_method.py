import os
import signal
#通过signal方式解决僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

#创建子进程
pid = os.fork()

if pid == 0:
    print("The new process")
    print("id:",os.getpid())
    os._exit(0)
#父进程执行
else:
    while True:
        pass

