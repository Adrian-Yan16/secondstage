class Enemy:
    def __init__(self, name, blood, basic_attack_power, defensive_power):
        self.name = name
        self.blood = blood
        self.basic_attack_power = basic_attack_power
        self.defensive_power = defensive_power

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.blood, self.basic_attack_power, self.defensive_power)


list1 = [
    Enemy("灭霸", 0, 130, 95),
    Enemy("章鱼博士", 60, 30, 25),
    Enemy("蜥蜴博士", 60, 30, 9),
    Enemy("绿恶魔", 70, 160, 50)
]

from common.ListHelper import *

select_enemy = ListHelper.find_single(list1, lambda item: item.name == "灭霸")
select_enemys = ListHelper.find_all(list1, lambda item: item.basic_attack_power > 5)
select_count = ListHelper.get_count(list1, lambda item: item.blood > 10)

re = ListHelper.target_if_in(list1, lambda item: item.basic_attack_power < 5 or item.defensive_power > 10)
re1 = ListHelper.target_if_in(list1, lambda item: item.name == "成昆")

sum_attack = ListHelper.sum_property(list1, lambda item: item.basic_attack_power)


all_name = ListHelper.all_property(list1, lambda item: item.name)
all_name_defensive = ListHelper.all_property(list1, lambda item: (item.name, item.defensive_power))

max_attack = ListHelper.max_property(list1, lambda item: item.basic_attack_power)


ListHelper.asceding_sort_property(list1,lambda item:item.basic_attack_power)


tuple1 = ([1,1,1],[2,2],[3,3,3,3],[4,4,4])
re2= ListHelper.max_length_property(tuple1,lambda item:len(item))
max(tuple1,key=lambda item:len(item))

re3 = ListHelper.all_property(list1,lambda item:(item.name,item.basic_attack_power,item.blood))
map(lambda item:(item.name,item.basic_attack_power,item.blood),list1)
ListHelper.find_all(list1,lambda item:item.basic_attack_power>100 and item.blood>0)


re4 = filter(lambda item:item.basic_attack_power>100 and item.blood > 0,list1)

ListHelper.desceding_sort_property(list1,lambda item:item.defensive_power)
re6 = sorted(list1,key=lambda item:item.defensive_power,reverse=True)

ListHelper.delete_property(list1, lambda item: item.basic_attack_power < 50)

