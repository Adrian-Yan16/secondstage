list1 = [1,1.1,2.3,"lsd","sld",True,"34"]
generator_list = (item for item in list1 if type(item) == float)
for item in generator_list:
    print(item)

list2 = [item for item in list1 if type(item) == float]
print(list2)


def generator():
    for item in list1:
        if type(item) == float:
            yield item

re = generator()
for item in re:
    print(item)
