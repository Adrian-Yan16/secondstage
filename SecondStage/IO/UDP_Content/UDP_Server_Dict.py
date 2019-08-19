from socket import *
from file_operate import *

#创建套接字
sock = socket(type=SOCK_DGRAM)

#绑定地址
ADDR = ("127.0.0.1",24016)
sock.bind(ADDR)

#接发消息
while True:
    data,addr = sock.recvfrom(1024)
    if not data:
        break
    dict_search = WordSearch()
    annotation = dict_search.word_search(data.decode())
    if not annotation:
        sock.sendto("未找到".encode(), addr)
    sock.sendto(annotation.encode(),addr)


#关闭
sock.close()





