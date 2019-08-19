list1 = [1,2,3]
a = 0

def b():
    list1 = []
    list1.append(0)
    a = 100
    return list1

b()
print(list1)
print(b())