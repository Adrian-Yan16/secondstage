from socket import *

#创建套接字
sock = socket(type=SOCK_DGRAM)

#接发消息
ADDR = ("127.0.0.1",24016)
while True:
    word = input("请输入要查询的单词：")
    if not word:
        break
    sock.sendto(word.encode(),ADDR)
    data,addr = sock.recvfrom(1024)
    print("%s的注释为：%s"%(word,data.decode()))

#关闭
sock.close()