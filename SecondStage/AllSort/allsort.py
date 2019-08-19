def bubble_sort(list_):
    for i in range(len(list_) - 1):
        for j in range(len(list_) - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


def insert_sort(list_):
    for i in range(1, len(list_)):
        temp = list_[i]
        j = i - 1
        while j > -1 and temp < list_[j]:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = temp


def quick_insert_controller(list_, left, right):
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


def quick_insert(list_, left, right):
    if left < right:
        key = quick_insert_controller(list_, left,right)
        quick_insert(list_, left, key - 1)
        quick_insert(list_, key + 1, right)


list1 = [4,3,4,2,5,7,4,1,8]
quick_insert(list1, 0, len(list1) - 1)
print(list1)
