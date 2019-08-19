file_name1 = input("请输入文件名：")
try:
    f1 = open(file_name1,"rb+")
except:
    raise FileNotFoundError
file_name2 = input("重命名文件的名字：")
f2 = open(file_name2,"wb+")
for line in f1:
    if not line:
        break
    f2.write(line)
f1.close()
f2.close()