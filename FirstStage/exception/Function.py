list1 = [2, 3, 45, 54, 65, 67, 1]

"""
def select1(targit_list):
    for item in targit_list:
        if item % 2 == 0:
            return item


def select2(targit_list):
    for item in targit_list:
        if item > 10:
            return item


def select3(targit_list):
    for item in targit_list:
        if 10 < item < 50:
            return item
"""


def condition1(target):
    return target % 2 == 0


def condition2(target):
    return target > 10


def condition3(target):
    return 10 < target < 50


def select(target_list, condition):
    """
    通用查找方法
    :param target_list: 要操作的可迭代对象
    :param condition: 要调用的方法，返回值为bool类型
    :return: 满足条件的数据
    """
    for item in target_list:
        if condition(item):
            yield item


for i in select(list1,condition1):
    print(i)