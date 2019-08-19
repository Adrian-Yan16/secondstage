"""
在控制台输入端口，返回他的地址，如果输入错误，提示
"""
import re

class Port:
    def __init__(self,port):
        self.__port = port

    def __get_file(self):
        f = open("./exc.txt")
        data = f.read()
        return data

    def get_addr(self):
        strobj = self.__get_file()
        pottern = re.compile(r"\n\n(\S+)")
        port_list = pottern.findall(strobj)
        if self.__port in port_list:
            pottern_port = re.compile(r"%s(.+\n)+"%self.__port)
            matobj = pottern_port.search(strobj).group()
            addr_list = re.findall(r" address is (.+)",matobj)
            print(addr_list)
        else:
            print("端口输入错误！！！")


if __name__ == '__main__':
    while True:
        port = input("请输入端口名：")
        p = Port(port)
        p.get_addr()

