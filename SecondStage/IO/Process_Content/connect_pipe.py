from multiprocessing import Process,Pipe

#通过管道方式通信，
fd1,fd2 = Pipe()

def app1():
    print("app1 请求登录")
    fd1.send("请求授权")
    data = fd1.recv()
    if data:
        print("登录成功:",data)


def app2():
    data = fd2.recv()
    print(data)
    fd2.send(("name","password"))


p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()
