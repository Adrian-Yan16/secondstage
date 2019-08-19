"""
1.创建监听套接字
2.等待接收客户端请求
3.客户端连接创建新的进程处理客户端请求
4.原进程继续等待其他客户端连接
5.如果客户端退出，则销毁对应的进程
"""

from multiprocessing import Process
import os,signal
from socket import *

def handle(s,c):
    s.close()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
    os._exit(0)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("waiting for connecting 24016...")

#创建监听套接字
ADDR = ("0.0.0.0",24016)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#等待接收客户端请求
while True:
    try:
        c,addr = s.accept()
        print("connect from:",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    p = Process(target= handle,args = (s,c))
    p.daemon = True
    p.start()


