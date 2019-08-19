from socket import *
#创建套接字
sock = socket(type=SOCK_DGRAM)

#绑定地址
sock.bind(("127.0.0.1",24016))

#接发消息
while True:
    data,addr = sock.recvfrom(1024)
    print("client>>",data.decode())
    sock.sendto(b"lueluelue",addr)


