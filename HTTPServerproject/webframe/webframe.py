"""
接收httpserver请求
给httpserver发送反馈
逻辑功能处理
"""

from socket import *
import json,select
from HTTPServerproject.webframe.settings import *
from HTTPServerproject.webframe.urls import *

class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.connect_http()

    def connect_http(self):
        """
        创建与httpserver连接的套接字
        :return:
        """
        self.s = socket()
        self.rlist.append(self.s)
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.s.bind((FRAME_IP,FRAME_PORT))

    def start(self):
        """
        等待连接，如果http有连接，则将c套接字加入监听，并进行后续处理
        :return:
        """
        self.s.listen(5)
        print("listen from port ",FRAME_PORT)
        while True:
            rl,wl,xl = select.select(self.rlist,self.wlist,self.xlist)
            for r in rl:
                if r is self.s:
                    c, addr = self.s.accept()
                    print("connect from ", addr)
                    self.rlist.append(c)
                else:
                    self.handle_request(r)
                    self.rlist.remove(r)

    def handle_request(self,connfd):
        """
        处理http请求{“cmd”：“”，“content”：“”}，并向http反馈{“status”：“”，“content”：“”}
        :param connfd:
        :return:
        """
        request = connfd.recv(1024).decode()
        if not request:
            return
        request = json.loads(request)
        if request["cmd"] == "GET":
            if request["content"] == "/" or request["content"][-5:] == ".html":
                response = self.get_html(request["content"])
            else:
                response = self.get_data(request["content"])
        elif request["cmd"] == "POST":
            pass
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    def get_html(self,content):
        """
        处理浏览器的网页请求
        :param content:
        :return:
        """
        if content == "/":
            filename = DIR+"/index.html"
        else:
            filename = DIR + content
        try:
            f = open(filename)
        except:
            fd = open(DIR + '/404.html')
            return {"status":"404","content":fd.read()}
        else:
            return {"status":"200","content":f.read()}

    def get_data(self,content):
        """
        处理浏览器其他类型请求
        :param content:
        :return:
        """
        for cmd,func in urls:
            if cmd == content:
                return {"status":"200","content":func()}
        else:
            return {"status":"404","content":"Sorry..."}



if __name__ == '__main__':
    app = Application()
    app.start()





