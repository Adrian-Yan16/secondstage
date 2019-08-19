"""
属性

class Review:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name


r1 = Review("hello")
print(r1.name)
r1.name = "hi"
print(r1.name)
"""
"""
yield

class ListIterator:
    def __init__(self, list_):
        self.__list = list_
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__list) - 1:
            raise StopIteration
        temp = self.__list[self.__index]
        self.__index += 1
        return temp


class ListPrinciple:
    def __init__(self,list_):
        self.__list = list_

    def __iter__(self):
        li = ListIterator(self.__list)
        return li


list1 = [1,2,3,4,5]
lp = ListPrinciple(list1)
# li = lp.__iter__()
# while True:
#     try:
#         key = li.__next__()
#         print(key)
#     except StopIteration:
#         break
for i in ListPrinciple(list1):
    print(i)
"""


"""
字典推导式
dict1 = {"a":1,"b":2,"c":3}
dict2 = {value:key for key,value in dict1.items()}
for i in dict2.items():
    print(i)
"""

"""
快排

class QuickSort:
    @staticmethod
    def single(list_,left,right):
        temp = list_[left]
        while left < right:
            while list_[right] > temp and left < right:
                right -= 1
            list_[left] = list_[right]
            while list_[left] <= temp and left < right:
                left += 1
            list_[right] = list_[left]
            list_[left] = temp
        return left
    
    @staticmethod
    def quicksort(list_,left,right):
        if left < right:
            mid = QuickSort.single(list_,left,right)
            QuickSort.quicksort(list_,left,mid - 1)
            QuickSort.quicksort(list_,mid + 1,right)
"""
"""
二分法求整数的平方根（整数）
"""
class Dichotomy:
    @staticmethod
    def dichotomy(val):
        if val in (0,1):
            return val
        left = 1
        right = val
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if left == right - 1:
                return mid
            if mid ** 2 == val:
                return mid
            elif mid ** 2 > val:
                right = mid
            else:
                left = mid
        return mid



d = Dichotomy()
print(d.dichotomy(1))






















