from socket import *

s = socket()
ADDR = ("127.0.0.1",24016)
s.connect(ADDR)

request = """GET /concurrent.html HTTP/1.1"""
s.send(request.encode())
while True:
    data= s.recv(1024)
    print(data.decode())

