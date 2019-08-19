"""
在控制台中循环录入字符串，打印所有不重复的字符

"""
# set1 = set()
# while True:
#     str1 = input("请输入字符串：")
#     if str1 == "":
#         break
#
#     set1.add(str1)
# print(set1)

"""
练习2
    经理:曹操，孙权，刘备
    技术：曹操，刘备，张飞，关羽
    （1）是经理也是技术
    （2）是经理，不是技术
    （3）是技术不是经理
    （4）张飞是经理吗
    （5）身兼一职的都有谁
    （6）经理和技术共多少人
    
"""

set1 = {"曹操","孙权","刘备"}
set2 = {"曹操","刘备","张飞","关羽"}
print("是经理也是技术:",set2&set1)
print("是经理，不是技术",set1-set2)
print("是技术不是经理",set2-set1)
list1 = list(set1)
if "张飞" in list1:
    print("张飞是经理")
else:
    print("张飞不是经理")
print("身兼一职的都有谁",set1^set2)
print("经理和技术共多少人",len(set1|set2))