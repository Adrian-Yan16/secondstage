from socket import *
#创建套接字
sockfd = socket()

#连接
sockfd.connect(('127.0.0.1',24016))

#收发消息
while True:
    send_message = input("msg>>")
    if not send_message:
        break
    sockfd.send(send_message.encode())
    data = sockfd.recv(1024)
    print("server:",data.decode())

#关闭
sockfd.close()

