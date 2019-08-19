import os, sys
from socket import *

ADDR = ("127.0.0.1", 24016)


def main():
    """
    网络搭建
    :return:
    """
    s = socket(type=SOCK_DGRAM)
    raise_request(s)


def raise_request(sockfd):
    """
    向服务器发出请求
    :param sockfd: 套接字
    :return:
    """
    user_name = raise_login(sockfd)
    raise_chat(sockfd, user_name)


def raise_login(sockfd):
    """
    向服务器发出登录请求
    :param sockfd:
    :return:
    """
    name = input("请输入姓名：")
    user_name = "L " + name
    sockfd.sendto(user_name.encode(), ADDR)
    server_response, addr = sockfd.recvfrom(1024)
    if server_response.decode() == "OK":
        print("你已进入聊天室")
    else:
        print(server_response.decode())
        raise_login(sockfd)
    return name


def raise_chat(sockfd, user_name):
    """
    创建多线程，使接收消息和发送消息互不干扰
    :param sockfd:
    :param user_name:用户姓名
    :return:
    """
    process = os.fork()
    while True:
        if process < 0:
            sys.exit("Connect fail")
        elif process == 0:
            send_msg(sockfd, user_name)
        else:
            recv_msg(sockfd)


def send_msg(sockfd, user_name):
    """
    向服务器发送消息
    :param sockfd:
    :param user_name:用户姓名
    :return:
    """
    while True:
        try:
            content = input(">>")
        except KeyboardInterrupt:
            content = "quit"
        if content == "quit":
            quit_msg(sockfd,user_name)
            return
        chat_content = "C %s %s"%(user_name,content)
        sockfd.sendto(chat_content.encode(), ADDR)


def quit_msg(sockfd,user_name):
    """
    接收退出指令
    :param sockfd:
    :param user_name:
    :return:
    """
    quit_content = "Q " + user_name
    sockfd.sendto(quit_content.encode(), ADDR)
    sys.exit("退出客户端")



def recv_msg(sockfd):
    """
    接收服务器消息
    :param sockfd: 套接字
    :return:
    """
    while True:
        try:
            data, addr = sockfd.recvfrom(1024)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode() == "exit":
            sys.exit()
        print(data.decode() + "\n>>" ,end="")


main()
