from dll import StarDisappearController
from model import *
import os
class StarDisappearView:
    def __init__(self):
        self.__dict_dir = {
            "w":StarDisappearModel.UP,
            "s":StarDisappearModel.DOWN,
            "a":StarDisappearModel.LEFT,
            "f":StarDisappearModel.RIGHT
        }
        self.__controller = StarDisappearController()

    def main(self):
        self.__draw_map()
        self.__update()

    def move_user(self,dir,location_x,location_y):
        self.__controller.change_position(dir,location_x,location_y)

    def __draw_map(self):
        # #清空控制台
        # os.system("clear")
        for line in self.__controller.list_target:
            for item in line:
                print(item,end = " ")
            print()

    def __update(self):
        # 循环
        while True:
            # 判断玩家的输入　--> 移动地图
            self.__move_map_for_input()
            # 绘制界面
            self.__draw_map()
            # 游戏结束判断 --> 提示
            if self.__controller.is_game_over():
                print("游戏结束")
                break

    def __move_map_for_input(self):
        dir = input("请输入方向(wsas)")
        location_x, location_y = eval(input("请输入要移动的位置"))
        dict_dir = {
            "w":StarDisappearModel.UP,
            "s":StarDisappearModel.DOWN,
            "a":StarDisappearModel.LEFT,
            "d":StarDisappearModel.RIGHT,
        }
        if dir in dict_dir:
            self.__controller.change_position(dict_dir[dir],int(location_x),int(location_y))


if __name__ == "__main__":
    view = StarDisappearView()
    view.main()



