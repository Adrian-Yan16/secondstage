"""
IO多路复用
重点代码
思路：
    将关注的IO加入监听列表
    IO就绪时通过select返回
    遍历返回值列表，判断是哪一个IO就绪
"""

from socket import *
from select import *

ADDR = ("127.0.0.1",24016)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

rlist = [s]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)   #设置监听
    for r in rs:
        if r is s:                         #有客户端连接
            c,addr = s.accept()
            print("connect from:",addr)
            rlist.append(c)                #添加监听IO
        else:                              #有客户端发消息
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)            #撤销监听
                r.close()
                continue
            print(data)
            #r.send(b"OK")
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)                    #发一次撤销一次监听
    for x in xs:
        pass
