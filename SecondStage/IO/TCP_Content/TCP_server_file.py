import socket
#创建套接字
sockfd = socket.socket(type= socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('127.0.0.1',4017))

#监听
sockfd.listen(5)

#阻塞，请求连接
while True:
    print("waiting for connecting")
    try:
        connfd,addr = sockfd.accept()
    except KeyboardInterrupt:
        print("Server Exit")
        break
    except Exception:
        print(Exception)
        continue
    print("对方地址",addr)

#接收及发送消息
    f = open("帅哥.JPG", "wb")
    while True:
        receive_message = connfd.recv(1024)
        if not receive_message:
            break
        f.write(receive_message)

    #关闭
    f.close()
    connfd.close()
sockfd.close()


