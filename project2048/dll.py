from model import *
from common.ListHelper import *
import random
import copy


class GameCoreController:
    def __init__(self):
        self.__map_user = [
            [2, 8, 4, 2],
            [8, 0, 8, 0],
            [0, 2, 0, 4],
            [2, 4, 4, 0]
        ]
        self.__list_empty_location = []

    @property
    def map_user(self):
        return self.__map_user

    def __zero_to_end(self, list_merge_target):
        """
        0元素移动到末尾
        :param list_merge_target: 要操作的列表
        :return:
        """
        i = 0
        while list_merge_target[i] != 0 and i < len(list_merge_target) - 1:
            i += 1
        for j in range(i + 1, len(list_merge_target)):
            if list_merge_target[j] != 0:
                list_merge_target[i], list_merge_target[j] = list_merge_target[j], list_merge_target[i]
                i += 1
                continue
        return list_merge_target

    def __zero_to_start(self, list_merge_target):
        """
        0元素移动到开头
        :param list_merge_target: 目标列表
        """
        self.__zero_to_end(list_merge_target)
        i = -1
        if list_merge_target[-1] != 0:
            return list_merge_target
        while list_merge_target[i] == 0 and i > -len(list_merge_target):
            for j in range(i - 1, -len(list_merge_target) - 1, -1):
                if list_merge_target[j] != 0:
                    list_merge_target[i], list_merge_target[j]\  
                    = list_merge_target[j], list_merge_target[i]
                    break
            i -= 1

        return list_merge_target

    def __combine_same_numbers(self, list_merge_target):
        """
        将相邻相同数字合并
        :param list_merge_target:
        """
        self.__zero_to_end(list_merge_target)
        for i in range(len(list_merge_target) - 1):
            if list_merge_target[i] == list_merge_target[i + 1]:
                list_merge_target[i] *= 2
                list_merge_target[i + 1] = 0
        self.__zero_to_end(list_merge_target)
        return list_merge_target

    def __move_left(self):
        """
        将map2向左移动，并且相同相邻的数相加
        """
        for item in self.__map_user:
            self.__combine_same_numbers(item)

    def __move_right(self):
        """
            将map2向左移动，并且相同相邻的数相加
        """
        self.__move_left()
        for item in self.__map_user:
            self.__zero_to_start(item)
    """
    def __move_up(self):
        '''
        向上移动
        :return: 移动后的列表
        '''
        ListHelper.square_matrix_transpose(self.map_user)
        self.__move_left()
        ListHelper.square_matrix_transpose(self.map_user)

    def __move_down(self):
        ListHelper.square_matrix_transpose(self.map_user)
        self.__move_right()
        ListHelper.square_matrix_transpose(self.map_user)
    """

    def __move_up_or_down(self,func_direction):
        """
        向上或向下移动
        :param func_direction: 函数类型，func_direction为self.__move_left时为向上移动，
                                        func_direction为self.__move_right时为向下移动
        """
        ListHelper.square_matrix_transpose(self.map_user)
        func_direction()
        ListHelper.square_matrix_transpose(self.map_user)

    def move(self, dir):
        """
            移动
        :param dir: 方向,DirectionModel类型
        """
        if dir == DirectionModel.UP:
            self.__move_up_or_down(self.__move_left)
        elif dir == DirectionModel.DOWN:
            self.__move_up_or_down(self.__move_right)
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    def generate_new_number(self):
        """
            在某一个空位置上随机生成新数字
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map_user[loc.r_index][loc.c_index] = self.__select_random_number()
        # 因为在该位置生成了新数字，所以该位置就不是空位置了．
        # self.__list_empty_location.remove(loc)

    def __select_random_number(self):
        """
        随机生成2或4，生成2的概率为90%
        :return: 2或4
        """
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        """
        获取所有"0"的位置并存入列表中
        """
        # 每次统计空位置，都先清空之前的数据，避免影响本次数据．
        self.__list_empty_location.clear()
        for r in range(len(self.__map_user)):
            for c in range(len(self.__map_user[r])):
                if self.__map_user[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def if_game_over(self):
        """
        判断游戏是否结束
        """
        map_copy = copy.deepcopy(self.map_user)
        self.__get_empty_location()
        if len(self.__list_empty_location) > 0:
            print("游戏未结束")
            return
        elif self.__adjacent_number_if_equal(map_copy):
            ListHelper.square_matrix_transpose(map_copy)
            if self.__adjacent_number_if_equal(map_copy):
                print("游戏结束")

    def __adjacent_number_if_equal(self, map_target):
        """
        判断相邻数字是否相等
        :param map_target: 需要判断的列表
        :return: 游戏未结束返回False，结束则返回True
        """
        for item in map_target:
            for i in range(len(item) - 1):
                if item[i] == item[i + 1]:
                    print("游戏未结束")
                    return False
        return True


# ___________________________________________


if __name__ == "__main__":
    controller = GameCoreController()
    controller.generate_new_number()
    controller.move(3)
    for item in controller.map_user:
        print(item)

