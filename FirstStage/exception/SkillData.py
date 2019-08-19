class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]

"""
#lamda的详细步骤

def condition1(target_skill_data, name):
    return target_skill_data.name == name


def condition2(target_skill_data, id):
    return target_skill_data.id == id


def condition3(target_skill_data, duration):
    return target_skill_data.duration > duration
"""

from common.mylisthelper import MyListHelper

my_list = MyListHelper()
re = my_list.select(list_skill, lambda target_skill_data, duration: target_skill_data.duration > duration, 5)

my_list = MyListHelper()
re2 = my_list.get_count(list_skill,lambda item:item.duration<5)



