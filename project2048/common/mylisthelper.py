class MyListHelper:
    @staticmethod
    def select(target_skill_data, condition):
        """
        通用查找方法
        :param target_list: 要操作的可迭代对象
        :param condition: 要调用的方法，返回值为bool类型
        :param target_value:要查找的事物
        :return: 满足条件的数据
        """
        for item in target_skill_data:
            if condition(item):
                return item

    @staticmethod
    def get_count(target_skill, func_condition):
        """
        通用查找满足条件的数量方法
        :param target_skill: 要操作的可迭代对象
        :param func_condition: 要调用的方法，返回值为bool类型
        :return: 满足条件的数量
        """
        count = 0
        for item in target_skill:
            if func_condition(item):
                count += 1
        return count


