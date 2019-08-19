from multiprocessing import Process
import os


def front_part():
    f = open("time_record.txt", "r")
    size = os.path.getsize("time_record.txt")
    mid = size // 2
    f_front = open("time_record_front","w")
    f.seek(0)
    front_part_content = f.read(mid)
    f_front.write(front_part_content)
    f_front.close()


def last_part():
    f = open("time_record.txt", "r")
    size = os.path.getsize("time_record.txt")
    mid = size // 2
    f_last = open("time_record_last","w")
    f.seek(mid+1)
    front_part_content = f.read()
    f_last.write(front_part_content)
    f_last.close()


process1 = Process(target=front_part,args=())
process1.start()
last_part()
process1.join()