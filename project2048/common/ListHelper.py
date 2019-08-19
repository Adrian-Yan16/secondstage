"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法(例：Lambda_homework中查找攻击力>5的所有敌人类
                                                filter(lambda item:item.basic_attack_power>100 and item.blood > 0,list1)同样可以实现）
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, condition):
        """
        通用查找方法（单个条件）(例：Lambda_homework中查找姓名为“灭霸”的敌人类）
        :param target_list: 要操作的可迭代对象
        :param condition: 要调用的方法，返回值为bool类型
        :return: 满足条件的数据
        """
        for item in list_target:
            if condition(item):
                return item

    @staticmethod
    def get_count(list_target, func_condition):
        """
        通用查找满足条件的数量方法（例：Lambda_homework中查找血量>10的所有敌人的数量）
        :param list_target: 要操作的可迭代对象
        :param func_condition: 要调用的方法，返回值为bool类型
        :return: 满足条件的数量
        """
        count = 0
        for item in list_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def target_if_in(list_target, func_condition):
        """
        查找对象是否存在（例：Lambda_homework中查找攻击力<5或防御力>10（或其他）的敌人是否存在）
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件,函数类型
                   函数名(参数) --> bool
        :return:返回bool值
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum_property(list_target, func_property):
        """
        求某个属性的和（例：Lambda_homework中求出所有敌人类的总攻击力或其他）
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件,函数类型
                   函数名(参数) --> 返回值int/float类型
        :return:返回int类型
        """
        total_value = 0
        for item in list_target:
            total_value += func_property(item)
        return total_value

    @staticmethod
    def all_property(list_target, func_property):
        """
        通用筛选某几个属性（例：Lambda_homework中查找所有敌人类的姓名或（姓名，攻击力）（元组形式返回）
                                map(lambda item:(item.name,item.basic_attack_power),list1)同样可实现该功能）
        :param list_target:需要查找的列表
        :param func_condition:需要查找处理逻辑,函数类型
                   函数名(参数) --> 返回值int/str/元组/其他类型
        :return:返回bool值
        """
        for item in list_target:
            yield func_property(item)

    @staticmethod
    def max_property(list_target, func_property):
        """
        通用获取属性最大元素的方法（例：Lambda_homework中查找攻击力最大的敌人类）
        :param list_target:需要查找的列表
        :param func_condition:需要查找处理逻辑,函数类型
                   函数名(参数) --> 返回值int/float类型
        :return:返回属性最大的元素
        """
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_property(max_value)<func_property(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def min_property(list_target, func_property):
        """
        通用获取属性最小元素的方法（例：Lambda_homework中查找攻击力最小的敌人类）
        :param list_target:需要查找的列表
        :param func_condition:需要查找处理逻辑,函数类型
                   函数名(参数) --> 返回值int/float类型
        :return:返回属性最大的元素
        """
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_property(min_value) > func_property(list_target[i]):
                min_value = list_target[i]
        return min_value

    @staticmethod
    def asceding_sort_property(list_target, func_property):
        """
        通用属性升序排列，操作的是列表，不需返回值（例：Lambda_homework中将敌人类按攻击力升序排列
                                                        sorted(list1,key=lambda item:item.defensive_power)同样可以实现）
        :param list_target:需要查找的列表
        :param func_condition:需要查找处理逻辑,函数类型
                   函数名(参数) --> 返回值int/float类型
        """
        for i in range(len(list_target) - 1):
            k = i
            for j in range(i+1, len(list_target)):
                if func_property(list_target[k]) > func_property(list_target[j]):
                    k = j
            if k!=i:
                list_target[i], list_target[k] = list_target[k], list_target[i]

    @staticmethod
    def max_length_property(list_target,func_element):
        """
        找到可迭代对象中最长的元素（例：Lambda_homework中将元组中最长的列表筛选出来，
                                        max(tuple1,key=lambda item:len(item))同样可实现该功能）
        :param list_target: 需要查找的列表
        :param func_element: 需要查找处理逻辑,函数类型
                   函数名(参数) --> 返回值int类型
        :return: 迭代对象中最长的元素
        """
        max_length = list_target[0]
        for i in range(1,len(list_target)):
            if func_element(max_length)<func_element(list_target[i]):
                max_length = list_target[i]
        return max_length

    @staticmethod
    def desceding_sort_property(list_target, func_property):
        """
        通用属性降序排列，操作的是列表，不需返回值（例：Lambda_homework中将敌人类按攻击力降序排列
                                                        sorted(list1,key=lambda item:item.defensive_power,reverse=True)同样可以实现）
        :param list_target:需要查找的列表
        :param func_condition:需要查找处理逻辑,函数类型
                   函数名(参数) --> 返回值int/float类型
        """
        for i in range(len(list_target) - 1):
            k = i
            for j in range(i + 1, len(list_target)):
                if func_property(list_target[k]) < func_property(list_target[j]):
                    k = j
            if k != i:
                list_target[i], list_target[k] = list_target[k], list_target[i]

    @staticmethod
    def delete_property(list_target, func_element):
        """
        删除符合条件的元素，操作的是列表，不需返回值（例：Lambda_homework中删除攻击力小于50的敌人类）
        :param list_target: 需要查找的列表
        :param func_element: 需要查找处理逻辑,函数类型
                   函数名(参数) --> 返回值int类型
        """
        for i in range(len(list_target)-1,-1,-1):
            if func_element(list_target[i]):
                del list_target[i]

    @staticmethod
    def square_matrix_transpose(map_target):
        """
        方阵(二维列表）转置函数
        :return:方阵转置之后的列表
        """
        for i in range(len(map_target)):
            for j in range(i + 1, len(map_target)):
                map_target[i][j], map_target[j][i] = map_target[j][i], map_target[i][j]


if __name__ == "__main__":
    map_user = [
        [2, 8, 4, 2],
        [8, 2, 8, 4],
        [1, 2, 3, 4],
        [3, 5, 4, 6]
    ]
    ListHelper.square_matrix_transpose(map_user)
    print(map_user)

