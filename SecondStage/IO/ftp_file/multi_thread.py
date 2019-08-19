from test import *
from threading import Thread
import time

jobs = []

tm = time.time()
for i in range(10):
    t = Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
print("Thread cpu:",time.time() - tm)