"""
ftp文件传输 服务器
"""

from socket import *
from threading import Thread
import sys, os, time

# 全局变量
ADDR = ("127.0.0.1", 24016)

FTP = "/home/tarena/FTP/"

print("waiting for connecting...")


class FTPServer(Thread):
    """
    文件查看，下载，上传，退出
    """

    def __init__(self, connfd):
        self.connfd = connfd
        self.__files = os.listdir(FTP)
        super().__init__()

    # 循环接收消息
    def run(self):
        while True:
            commond = self.connfd.recv(1024).decode()
            if not commond or commond == "Q":
                return
            elif commond == "L":
                self.file_list()
            elif commond == "G":
                self.file_download()
            else:
                self.file_upload()

    def file_list(self):
        if not self.__files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        filelist = ""
        for file in self.__files:
            if file[0] != "." and os.path.isfile(FTP + file):#如果该文件是隐藏文件或文件夹，则退出
                filelist += file + "\n"#以\n分割
        self.connfd.send(filelist.encode())

    def file_download(self):
        file_name = self.connfd.recv(1024).decode()
        if file_name not in self.__files:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"OK")
            f = open(FTP + file_name, "rb")
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(1)
                    self.connfd.send("##".encode())#此时，表示文件传输完成
                    break
                self.connfd.send(data)

    def file_upload(self):
        file_name = self.connfd.recv(1024).decode()
        if file_name in self.__files:
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send("OK".encode())
            f = open(FTP + file_name, "wb")
            while True:
                content = self.connfd.recv(1024)
                if content == b"##":
                    break
                f.write(content)


# 连接客户端,
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    while True:
        try:
            c, addr = s.accept()
            print("connect from:", addr)
        except KeyboardInterrupt:
            sys.exit("退出服务器")
        except Exception as e:
            print(e)
            continue
        t = FTPServer(c)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
