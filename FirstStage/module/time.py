import time


def calculate_day(year, month, day):
    birth_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_day = time.time() - time.mktime(birth_time)
    return int(life_day/60/60//24)


re = calculate_day(2019, 5, 23)
print(re)
