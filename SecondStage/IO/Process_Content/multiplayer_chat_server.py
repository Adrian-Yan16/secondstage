import os, sys
from socket import *

ADDR = ("127.0.0.1", 24016)

user = {}


def main():
    """
    网络搭建
    :return:
    """
    s = socket(type=SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        while True:
            manager_info = input("管理员消息：")
            manager_information = "C 管理员 " + manager_info
            s.sendto(manager_information.encode(),ADDR)

    handle_request(s)


def handle_request(sockfd):
    """
    处理客户端请求
    :param sockfd: 套接字
    :return:
    """
    while True:
        """
        创建协议,"L"表示姓名,"C"表示聊天,"Q"表示退出
        """
        data, addr = sockfd.recvfrom(1024)
        client_request = data.decode().split(" ")
        text = " ".join(client_request[2:])#若聊天信息中也有空格，则会将其进行合并
        if client_request[0] is "L":
            handle_login(sockfd, client_request[1], addr)
        elif client_request[0] is "C":
            handle_chat(sockfd, client_request[1],text)
        elif client_request[0] is "Q":
            handle_quit(sockfd, client_request[1],addr)


def handle_login(sockfd, name, address):
    """
    处理客户端登录请求
    :param sockfd:
    :param name:
    :param address:
    :return:
    """
    if name in user:
        sockfd.sendto("\n姓名已存在".encode(), address)
        return
    else:
        sockfd.sendto("OK".encode(), address)
    for item in user:
        sockfd.sendto(("\n'%s'进入聊天室" % name).encode(), user[item])
    user[name] = address


def handle_chat(sockfd, name,text):
    """
    处理客户端聊天请求，并转发给其他用户
    :param sockfd:
    :param name:发消息这姓名
    :param text:发送的信息
    :return:
    """
    for item in user:
        if name != item:
            sockfd.sendto(("\n%s:%s"%(name,text)).encode(), user[item])


def handle_quit(sockfd, name,address):
    """
    处理客户端退出请求
    :param sockfd:
    :param name:
    :param address:
    :return:
    """
    for item in user:
        if name != item:
            sockfd.sendto(("\n'%s'退出了" % name).encode(), user[item])
        else:
            sockfd.sendto("exit".encode(), address)
    del user[name]


main()
