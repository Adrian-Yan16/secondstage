"""
接收浏览器请求
给浏览器发送反馈
给webframe发送请求
得到webframe反馈
"""

from socket import *
from threading import Thread
import re,json
from HTTPServerproject.httpserver.config import *

class HTTPServer:
    def __init__(self):
        self.connect_client()

    def connect_client(self):
        """
        创建与客户端（浏览器）连接的套接字
        :return:
        """
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.s.bind((HTTP_IP,HTTP_PORT))

    def connect_web(self,dict_):
        """
        创建与webframe连接的套接字，发送请求{“cmd”：“”，“content”：“”}，并得到反馈{“status”：“”，“content”：“”}
        :param dict_:
        :return:
        """
        s = socket()
        try:
            s.connect((FRAME_IP,FRAME_PORT))
        except Exception as e:
            print(e)
            return
        else:
            json_request = json.dumps(dict_)    #将字典转换为json格式
            s.send(json_request.encode())
            web_response = s.recv(1024*1024).decode()
            if not web_response:
                return
            return json.loads(web_response)     #将webframe反馈的json格式格式转换字典

    def server_forever(self):
        """
        监听是否有浏览器连接，若有则创建多线程处理c套接字的请求
        :return:
        """
        self.s.listen(5)
        print("listen from port",HTTP_PORT)
        while True:
            c,addr = self.s.accept()
            t = Thread(target=self.handle,args=(c,))
            t.setDaemon(True)
            t.start()

    def handle(self,connfd):
        """
        处理客户端请求，并向webframe发出请求{“cmd”：“”，“content”：“”}，并得到反馈{“status”：“”，“content”：“”}，处理逻辑功能
        :param connfd:
        :return:
        """
        request = connfd.recv(4096).decode()
        try:
            pattern =re.compile(r"(?P<cmd>([A-Z]+))\s+(?P<content>(/\S*))")
            cmd_content_dict = pattern.match(request).groupdict()
        except Exception:
            connfd.close()
            return
        else:
            print("connect from ",connfd.getpeername())
            response_web_dict = self.connect_web(cmd_content_dict)
            if response_web_dict:
                self.do_web_response(connfd,response_web_dict)

    def do_web_response(self,connfd,dict_):
        """
        处理webframe反馈的内容
        :param dict_:
        :return:
        """
        if dict_['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = dict_['content']
        elif dict_['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = dict_['content']
        elif dict_['status'] == '500':
            pass
        # 给浏览器发送数据
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())


if __name__ == '__main__':
    hs = HTTPServer()
    hs.server_forever()

