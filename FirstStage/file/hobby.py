"""
练习:在控制台中录入多个人的多个喜好,输入空字符停止.
例如:请输入姓名：
    请输入第1个喜好：
    请输入第2个喜好：
    ...
    请输入姓名：
    ...
   最后在控制台打印所有人的所有喜好.
[
    {“无忌”:[赵敏,周芷若,小赵]}
]
"""

# 方法一
#
#     {“无忌”:[赵敏,周芷若,小赵]}
#
dict_habit_all = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    list_habit = []
    # 将爱好存入一个列表
    i = 1
    while True:
        habit = input("请输入第%d个喜好：" % i)
        if habit == "":
            break
        list_habit.append(habit)
        i += 1
    # 将每个人及其爱好存入字典
    dict_habit_all[name] = list_habit
print(dict_habit_all)

# 方法二
# [
#     {“无忌”:{赵敏,周芷若,小赵}}
# ]

list_hobby = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    i = 1
    list_habit = []
    while True:
        habit = input("请输入第%d个喜好：" % i)
        if habit == "":
            break
        list_habit.append(habit)
        i += 1
    dict_hobby = {name: list_habit}
    # 字典嵌套到列表中
    list_hobby.append(dict_hobby)
for dict_hobby in list_hobby:
    print(dict_hobby)
dict_hobby = list_hobby[0]
print(dict_hobby)
