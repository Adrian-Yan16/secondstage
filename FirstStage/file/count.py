"""
计算一个字符串中的字符以及出现的次数
逐一判断字符出现的次数
如果统计过则增加1，没统计过则等于1

"""
# 方法一
# str_count = "aalkjoiwerkelk"
# list_new = []
#
# #将不重复的字符存入列表中
# for str_item in str_count:
#     if str_item not in list_new:
#         list_new.append(str_item)
# #将列表中字符与字符串中字符比较，并统计
# for list_item in list_new:
#     str_item_count = 0
#     for str_item in str_count:
#         if list_item == str_item:
#             str_item_count += 1
#
#     print("%s出现了%d次" %(list_item,str_item_count))

# 方法二

# str_count = "aalkjoiwerkelk"
# dict_count = {}
# for item in str_count:
#     if item not in dict_count:
#         dict_count[item] = 1
#     else:
#         dict_count[item] += 1
# print(dict_count)


def count_string_element(string_user):
    """
    数字符串中各字符的个数
    :param string_user: 用户提供的字符串
    :return: 返回一个字典
    """
    dict_count = {}
    for item in string_user:
        if item not in dict_count:
            dict_count[item] = 1
        else:
            dict_count[item] += 1
    return dict_count


print(count_string_element("sldjf"))