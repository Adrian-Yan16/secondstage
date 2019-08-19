# """
# 将列表的索引与值取出，并以元组的形式返回
# """
# def my_enumerate(target_list):
#     number = 0
#     while number < len(target_list):
#         yield (number,target_list[number])
#         number +=1
#
#
# list1 = [0,1,2,3,4]
# for item in my_enumerate(list1):
#     print(item)

"""
将多个可迭代对象的元素一一对应的存入元组中
"""
def my_zip(*args):
    for i in range(len(args[0])):
        zip_list = []
        for item in args:
            try:
                zip_list.append(item[i])
            except IndexError:
                del zip_list
                return
        yield tuple(zip_list)


list1 = [1,2,3,4,5,6,7]
list2 = [4,5,6,7]
list3 = [1,2,3]
for item in my_zip(list1,list2,list3):
    print(item)