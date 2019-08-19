# from gevent import monkey
# import gevent
# monkey.patch_socket()
from socket import *
from select import *


class HTTPServer:
    def __init__(self, ADDR=("127.0.0.1", 24016), DIR=None):
        self.ADDR = ADDR
        self.DIR = DIR

    def request(self, fd, c, addr, ep):
        data = c.recv(1024).decode()
        if not data:
            print("disconnect from:", addr)
            ep.unregister(c)
            del fd[c.fileno()]
            c.close()
            return
        # 如果是"/"，就返回index.html,否则返回404
        s = data.split(" ")
        if s[1] == "/" or s[1][-5:] == ".html":
            self.get_html(c, s)
        else:
            self.get_data(c)

    def get_html(self, c, s):
        if s[1] == "/":
            filename = self.DIR + "index.html"
        else:
            filename = self.DIR + s[1]
            try:
                f = open(filename)
            except Exception:
                c.send(b"Sorry")
                return
        f = open(filename)
        file = f.read()
        c.send(("""HTTP/1.1 200 OK\n\n%s""" % file).encode())

    def get_data(self, c):
        request = """HTTP/1.1 200 OK\n\n"""
        request += "<h1>waiting for 3.0</h1>"
        c.send(request.encode())

    def create_socket(self):
        s = socket()
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind(ADDR)
        s.listen(3)
        print("listen from %s" % self.ADDR[1])
        self.monitor(s)

    def monitor(self, s):
        # 创建fileno-->object的字典
        fd = {s.fileno(): s}
        # 创建epoll对象
        ep = epoll()
        # 将s加入监听
        ep.register(s, EPOLLIN | EPOLLERR)
        while True:
            events = ep.poll()
            for fn, event in events:
                if fn == s.fileno():
                    c, addr = s.accept()
                    print("connect from:", addr)
                    fd[c.fileno()] = c
                    ep.register(c, EPOLLERR | EPOLLIN)
                    # gevent.spawn(self.request,c,addr)
                elif event & EPOLLIN:
                    self.request(fd, fd[fn], fd[fn].getpeername(), ep)

    def server_forever(self):
        self.create_socket()


if __name__ == '__main__':
    ADDR = ("0.0.0.0", 24016)
    DIR = "./static/"
    h = HTTPServer(ADDR, DIR)
    h.server_forever()
