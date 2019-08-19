def EvenNumber(target_list):
    number = 0
    while number < len(target_list):
        if target_list[number] % 2 == 0:
            yield target_list[number]
            number += 1
        else:
            number += 1


list1 = [1,2,3,4,6,8,5]
for item in EvenNumber(list1):
    print(item)
print("-------------------")
g = (item for item in list1 if item % 2 == 0)
for i in g:
    print(i)