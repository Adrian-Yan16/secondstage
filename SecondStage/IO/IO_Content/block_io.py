"""
非阻塞IO
"""

from socket import socket
from time import ctime,sleep

ADDR = ("127.0.0.1",24016)
s = socket()
s.bind(ADDR)
s.listen(5)

#设置非阻塞IO,若需要recv也为非阻塞，须设置其对象即c即可
s.setblocking(False)

#设置超时检测
#s.settimeout(3)

while True:
    print("waiting for connecting...")
    try:
        c,addr = s.accept()
    except Exception as e:
        sleep(3)
        f = open("log.txt","a+")
        f.write("%s-%s\n"%(ctime(),e))
    else:
        print("connect from:",addr)
        while True:
            data = c.recv(1024)
            print(data.decode())