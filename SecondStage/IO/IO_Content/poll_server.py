"""
IO多路复用
重点代码
思路：
    建立fileno-->IO对象字典用于查找
"""

from socket import *
from select import *

ADDR = ("127.0.0.1",24016)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#创建fileno-->IO对象字典
fd = {s.fileno():s}

#创建poll对象
p = poll()

#将s加入关注
p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll()                     #等待监听
    for fn,event in events:               #循环遍历列表，查看是哪个IO就绪
        if fn == s.fileno():
            c,addr = fd[fn].accept()
            print("connect from:",addr)
            fd[c.fileno()] = c            #维护字典
            p.register(c,POLLIN|POLLERR)  #把客户端套接字加入关注
        elif event & POLLIN:               #如果event是POLLIN则执行
            data = fd[fn].recv(1024).decode()
            if not data:
                p.unregister(fn)          #撤销关注
                del fd[fn]                #维护字典
                continue
            fd[fn].send(b"OK")
            print(data)



