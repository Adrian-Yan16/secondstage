def verify_account(func):
    def wrapper(*args, **kwargs):
        front_time = time.time()
        result = func(*args, **kwargs)
        print("执行时间%.2fs"%(time.time()-front_time))
        return result
    return wrapper

import time

@verify_account
def fun01():
    time.sleep(2)
    print("f1执行完毕")

@verify_account
def fun02(a):
    time.sleep(1)
    print("f2执行完了，参数：",a)


fun01()
fun02(100)