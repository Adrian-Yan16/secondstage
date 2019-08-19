# f = open("dict.txt")
# word = input("要查找的单词")
# for line in f:
#     character = line.split(" ")[0]
#     if character>word:
#         print("未找到")
#         break
#     if character == word:
#         print(line)
#         break
# f.close()
f = open("text.txt","wb")
f.write("hello ".encode())
f.write("world".encode())
f.close()



