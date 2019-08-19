from multiprocessing import Process,Array

#通过共用内存的方式进行连接，一次只可传一个列表或字节串，且上一个值会被下一个值覆盖
a = Array("i",[1,2,3,4])
a1 = Array("i",5)#初始开辟五个整形空间，初始值为0，创建可迭代对象

def ar():
    for i in a:
        print(i)
    a[0] = 5


p1 = Process(target=ar)
p1.start()
p1.join()
for i in a:
    print(i)