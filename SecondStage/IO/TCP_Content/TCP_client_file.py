from socket import *
from time import  sleep
#创建套接字
sockfd = socket()

#连接
sockfd.connect(('127.0.0.1',4017))

#收发消息
f = open("毕业照.JPG","rb")
while True:
    send_message = f.read(1024)
    sleep(0.5)
    if not send_message:
        break
    sockfd.send(send_message)


#关闭
f.close()
sockfd.close()

