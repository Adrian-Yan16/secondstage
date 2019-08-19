import time
def time_record():
    id = 1
    while True:
        f = open("time_record.txt","rb+")
        for line in f:
            if not line:
                break
            id = int(line.split(".".encode())[0])+1
        time_record1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        f.write((str(id)+"."+time_record1+"\n").encode())
        f.flush()
        time.sleep(1)


time_record()