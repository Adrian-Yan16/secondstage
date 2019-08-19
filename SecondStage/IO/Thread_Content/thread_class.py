"""
自定义线程类示例
"""

from threading import Thread

# 自定义线程类
class ThreadClass(Thread):
    # 重写父类init
    def __init__(self,*args):
        super().__init__()  # 加载父类init
        self.attr = args[0]

    # 假设需要很多步骤完成功能
    def f1(self):
        print("step 1")
    def f2(self):
        print("step 2")
    # 重写run 逻辑调用
    def run(self):
        self.f1()
        self.f2()


t = ThreadClass('abc')
t.start() # 自动运行run
t.join()


