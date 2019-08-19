"""
将列表[“无忌”，“赵敏”，“周芷若”]
转换为字典{“无忌”：2，“赵敏”：2，“周芷若”：3}（值为字符串的长度）
"""

# list1 = ["无忌", "赵敏", "周芷若"]
# dict_people = {}
# for item in list1:
#     dict_people[item] = len(item)
# print(dict_people)
# #字典推导式
# dict_people1 = {item: len(item) for item in list1}
# print(dict_people1)


"""
将列表[“无忌”，“赵敏”，“周芷若”]及[101,102,103]
转换为字典{“无忌”：101，“赵敏”：102，“周芷若”：103}（值为字符串的长度）
"""
#
# list1 = ["无忌", "赵敏", "周芷若"]
# list2 = [101, 102, 103]
# dict_people = {}
# for i in range(3):
#     dict_people[list1[i]] = list2[i]


"""
通过值找键
"""

# 方案1（键值互换）
# dict_people = {'无忌': 101, '赵敏': 102, '周芷若': 103}
# dict_people_reverse = {value: key for key, value in dict_people.items()}
# print(dict_people_reverse)
# 缺点：若value重复则丢失数据

# 方案二
dict_people = {'无忌': 101, '赵敏': 101, '周芷若': 103}
# 验证值有几项是否重复
list_room = [(value, key) for key, value in dict_people.items()]
print(list_room)
