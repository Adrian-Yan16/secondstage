"""
协程
"""
from gevent import monkey
import gevent
monkey.patch_socket()
from socket import *

#创建TCP套接字
ADDR = ("127.0.0.1",24016)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"OK")


while True:
    c,addr = s.accept()
    print("connect from:",addr)
    gevent.spawn(handle,c)
