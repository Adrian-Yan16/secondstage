from common.ListHelper import *
from model import *
import random


class StarDisappearController:
    """
        消灭星星

    """

    def __init__(self):
        self.__list_target = [
            ["#", "*", "#", "*"],
            ["*", "#", "*", "#"],
            ["#", "*", "#", "*"],
            ["*", "#", "*", "#"]
        ]

    @property
    def list_target(self):
        return self.__list_target

    def __combine_same_stars(self, one_dimensional_list):
        """
        将一维列表中相邻连续的星星消除
        :return: 返回消除星星后的列表
        """
        if one_dimensional_list.count("*") < 2:
            return one_dimensional_list
        k, j = self.__judge_stars_position(one_dimensional_list)
        if j - k < 2:
            return one_dimensional_list
        else:
            for num in range(k, j):
                one_dimensional_list[num] = 0
            return one_dimensional_list

    def __judge_stars_position(self, one_dimensional_list):
        """
        判断一维列表中第一个星星和相邻连续的最后一颗星星的索引
        :param one_dimensional_list:
        :return:
        """
        k = self.__find_target_index( -1, one_dimensional_list,
                                     lambda item: one_dimensional_list[item] != "*")
        j = self.__find_target_index( k, one_dimensional_list,
                                     lambda item: one_dimensional_list[item] == "*" or one_dimensional_list[item] == 0)
        if j == 1:
            if one_dimensional_list[j+1] == "*":
                k = j+1
                j = self.__find_target_index( k, one_dimensional_list,
                                     lambda item: one_dimensional_list[item] == "*" or one_dimensional_list[item] == 0)
        return k, j

    def __find_target_index(self, k, one_dimensional_list, func_condition):
        """
        查找列表中星星的索引位置
        :param k: 查找的起始位置
        :param one_dimensional_list: 一维列表
        :param func_condition:函数类型
        :return:查找到的索引值
        """
        j = 0
        for j in range(k + 1, len(one_dimensional_list)):
            if func_condition(j):
                j += 1
            else:
                break
        return j

    def __combine_all_adjacent_star(self):
        """
        删除二维列表中所有相邻的星星，第一次执行是将各行相邻的星星消除，第二次是将各列相邻的星星消除
        """
        self.__combine_stars_transpose()
        self.__combine_stars_transpose()

    def __combine_stars_transpose(self):
        self.__combine_every_line_same_star()
        ListHelper.square_matrix_transpose(self.__list_target)

    def __combine_every_line_same_star(self):
        for item_list in self.__list_target:
            self.__combine_same_stars(item_list)

    def __change_position_right_single(self, one_dimensional_list, location):
        """
        将一维列表中指定位置的字符与后一个字符交换
        :param location: 指定的位置
        """
        self.__combine_same_stars(one_dimensional_list)
        self.__judge_if_can_move(one_dimensional_list, location)
        if location >= len(one_dimensional_list):
            print("超出范围！！！输入值要小于", len(one_dimensional_list))
        else:
            one_dimensional_list[location - 1], one_dimensional_list[location] = one_dimensional_list[location], \
                                                                                 one_dimensional_list[location - 1]
            self.__combine_same_stars(one_dimensional_list)
        return one_dimensional_list

    def __judge_if_can_move(self, one_dimensional_list, location):
        """
        判断用户指定的位置及方向是否可以移动
        :param one_dimensional_list: 要操作的一维列表
        :param location: 用户指定的位置在一维列表中的索引
        :return:
        """
        if one_dimensional_list[location - 1] == 0:
            print("方向错误，不可进行移动")
            return one_dimensional_list

    def __change_position_left_single(self, one_dimensional_list, location):
        """
        将一维列表中指定位置的字符向左交换
        :param list_merge_target: 要操作的列表
        :param location:该字符的列数
        :return: 操作后的列表
        """
        self.__judge_if_can_move(one_dimensional_list, location)
        if location <= 1:
            print("超出范围！！！输入值要大于1")

        else:
            location = len(one_dimensional_list) - location + 1
            list_merge_target1 = one_dimensional_list[::-1]
            self.__change_position_right_single(list_merge_target1, location)
            list_merge_target2 = list_merge_target1[::-1]
            list_merge_target = list_merge_target2[:]
            return list_merge_target

    def __change_position_up_down(self, func_sub, location_x, location_y):
        """
        将指定位置“#”或“*”进行上下移动
        :param func_sub: 函数类型，若为self.__change_position_right_single,表示下移
                                若为self.__change_position_left_single,表示上移
        :param location_x: 指定数据的行数
        :param location_y: 指定数据的列数
        """
        ListHelper.square_matrix_transpose(self.__list_target)
        self.__list_target[location_y - 1] = func_sub(self.__list_target[location_y - 1], location_x)
        ListHelper.square_matrix_transpose(self.__list_target)
        self.__combine_all_adjacent_star()
        self.__fill_gaps_and_generate_new()

    def __change_position_left_right(self, func_sub, location_x, location_y):
        """
        将指定位置“#”或“*”进行左右移动
        :param func_sub: 函数类型，若为self.__change_position_right_single,表示右移
                                若为self.__change_position_left_single,表示左移
        :param location_x: 指定数据的行数
        :param location_y: 指定数据的列数
        """
        self.__list_target[location_x - 1] = func_sub(self.__list_target[location_x - 1], location_y)
        self.__combine_all_adjacent_star()
        self.__fill_gaps_and_generate_new()

    def __fill_gaps_and_generate_new(self):
        """
        将二维列表中的空位置有上面的字符填充，并在空位置随机生成新的字符
        """
        fill_gap = FillGapsAndGenerateStar()
        fill_gap.fill_in_gaps_downward(self.list_target)
        fill_gap.generate_in_empty(self.list_target)

    def change_position(self, dir, location_x, location_y):
        """
        移动
        :param dir: 方向
        :param location_x: 要移动的位置的行数
        :param location_y: 要移动的位置的列数
        """
        if dir == StarDisappearModel.UP:
            self.__change_position_up_down(self.__change_position_left_single, location_x, location_y)
        elif dir == StarDisappearModel.DOWN:
            self.__change_position_up_down(self.__change_position_right_single, location_x, location_y)
        elif dir == StarDisappearModel.LEFT:
            self.__change_position_left_right(self.__change_position_left_single, location_x, location_y)
        elif dir == StarDisappearModel.RIGHT:
            self.__change_position_left_right(self.__change_position_right_single, location_x, location_y)

    def is_game_over(self):
        """
        判断游戏是否结束
        :return: 结束返回true，未结束返回false
        """
        star_count = 0
        for item in self.list_target:
            for temp in item:
                if star_count < 2:
                    if temp == "*":
                        star_count += 1
                else:
                    return False
        return True


class FillGapsAndGenerateStar:
    @staticmethod
    def fill_in_gaps_downward(map_list):
        """
        将二维列表中的空位置有上面的字符填充
        :param map_list: 二维列表
        :return: 改变位置后的列表
        """
        ListHelper.square_matrix_transpose(map_list)
        for item in map_list:
            ListHelper.zero_to_start(item)
        ListHelper.square_matrix_transpose(map_list)

    @staticmethod
    def generate_in_empty(list_):
        """
        在空位置随机生成新的字符
        :param list_: 列表
        :return:
        """
        empty_location_list = ListHelper.get_empty_location(list_)
        for i in range(len(empty_location_list)):
            random_str = random.choice("#" "*")
            index_r, index_c = empty_location_list[i]
            list_[index_r][index_c] = random_str



        # ------------------------------------------------------------------


if __name__ == "__main__":
    re = StarDisappearController()
    for item in re.list_target:
        print(item)
    print("------------------------------------------------------------------")
    re.change_position(1, 1, 4)
    for item in re.list_target:
        print(item)
    print("------------------------------------------------------------------")
    re.change_position(3, 4, 1)
    for item in re.list_target:
        print(item)
    if re.is_game_over():
        print("游戏结束")
    else:
        print("游戏未结束")

