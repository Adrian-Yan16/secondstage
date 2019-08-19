"""
存储全国各个城市的景区及美食（不用键盘录入），在控制台显示
北京：
    景区：故宫，天安门，天坛
    美食：烤鸭，炸酱面，豆汁，卤煮
四川：
    景区；九寨沟，峨眉山，春熙路
    美食：火锅，串串香，兔头

"""

dict_city_character = {"北京":
                           [{"景区": ["故宫", "天安门", "天坛"]},
                            {"美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]}],
                       "四川":
                           [{"景区": ["九寨沟", "峨眉山", "春熙路"]},
                            {"美食": ["火锅", "串串香", "兔头"]}]}
# 北京及四川逐一遍历
for city, characters in dict_city_character.items():
    print("%s\n" % city)
    # 遍历列表
    for character in characters:
        # 遍历列表中元素即景区和美食
        for scenic_region_food, scenic_spot_food in character.items():
            print("\t%s:\n" % scenic_region_food)
            print("\t\t", scenic_spot_food)
