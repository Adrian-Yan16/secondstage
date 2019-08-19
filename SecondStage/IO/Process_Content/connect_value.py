from multiprocessing import Process,Value
from random import randint

#通过共用内存的方式进行连接，一次只可传一个值，且上一个值会被下一个值覆盖
v = Value("i",5000)
def man():
    for i in range(30):
        v.value += randint(500,1000)

def girl():
    for i in range(30):
        v.value -= randint(200,500)

p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p2.join()

print(v.value)