def search(list_, key):
    low, high = 0, len(list_)-1
    while low <= high:
        mid = (low + high) // 2
        if key > list_[mid]:
            low = mid + 1
        elif key < list_[mid]:
            high = mid - 1
        else:
            return mid


list1 = [1, 2, 3, 4, 5, 6]
print(search(list1, 6))
