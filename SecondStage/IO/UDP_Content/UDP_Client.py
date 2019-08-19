from socket import *
#创建套接字
sock = socket(type=SOCK_DGRAM)

#接发消息
ADDR = ("127.0.0.1",24016)
while True:
    send_msg = input("msg>>")
    if not send_msg:
        break
    sock.sendto(send_msg.encode(),ADDR)
    data,addr = sock.recvfrom(1024)
    print("server>>",data.decode())

#关闭
sock.close()