def my_range(target_value):
    number = 0
    while number < target_value:
        yield number
        number += 1


for item in my_range(10):
    print(item)