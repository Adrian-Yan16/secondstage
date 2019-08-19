"""
ftp文件传输 客户端
"""

from socket import *
import sys, time

# 全局变量
ADDR = ("127.0.0.1", 24016)


class FTPClient:
    """
    文件查看，下载，上传，退出
    """

    def __init__(self, socket):
        self.socket = socket

    def file_list(self):
        self.socket.send("L".encode())
        data = self.socket.recv(1024).decode()
        if data == "OK":
            filelist = self.socket.recv(4096).decode()
            print(filelist)

    def file_quit(self):
        self.socket.send(b"Q")
        self.socket.close()
        sys.exit("退出客户端")

    def file_download(self):
        self.socket.send("G".encode())
        file_name = input("请输入要下载的文件名：")
        self.socket.send(file_name.encode())
        data = self.socket.recv(1024).decode()
        if data == "OK":
            file_path = input("请输入要保存的文件路径：")
            print("文件传输中...")
            f = open(file_path+file_name, "wb")
            while True:
                content = self.socket.recv(1024)
                if content == b"##":
                    break
                f.write(content)
            print("文件传输完成")
        else:
            print(data)

    def file_upload(self):
        self.socket.send("P".encode())
        file_name = input("请输入待上传的文件名：")
        self.socket.send(file_name.encode())
        data = self.socket.recv(1024).decode()
        if data == "OK":
            file_path = input("请输入待上传的文件路径：")
            print("文件传输中...")
            try:
                f = open(file_path + file_name, "rb")
            except Exception:
                print("文件不存在")
                return
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.socket.send("##".encode())
                    break
                self.socket.send(data)
            print("文件传输完成")
        else:
            print(data)


# 连接服务器
def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    fc = FTPClient(s)
    while True:
        commond = input("请输入操作指令,L-请求文件列表,Q-退出,G-下载文件,P-上传文件")
        if commond == "L":
            fc.file_list()
        elif commond == "Q":
            fc.file_quit()
        elif commond == "G":
            fc.file_download()
        elif commond == "P":
            fc.file_upload()
        else:
            print("请输入正确的指令")


if __name__ == '__main__':
    main()
