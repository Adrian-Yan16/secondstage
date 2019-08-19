from module1 import bll, model


class StudentManagerView:
    """
        学生管理器视图,负责处理界面逻辑.
    """

    def __init__(self):
        self.__controller = bll.StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按成绩排列学生")

    def __select_menu_item(self):
        item = input("请您输入选项:")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_students()
        elif item == "4":
            self.__update_students()
        elif item == "5":
            self.__sort_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_students(self):
        # 调用逻辑控制类的add_student方法
        while True:
            stu = model.StudentModel(name="", age=0, score=0, id=0)
            stu.name = input("请输入姓名:")
            if stu.name == "":
                break
            stu.age = self.__input_error("年龄:")
            stu.score = self.__input_error("分数:")
            self.__controller.add_student(stu)

    def __output_students(self):
        """
        输出所有已有学生信息
        :return:
        """
        for item in self.__controller.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_students(self):
        """
        删除用户输入的序号的学生信息
        :return:
        """
        id = int(input("请输入学生id："))
        self.__controller.remove_student(id)

    def __update_students(self):
        """
        修改学生信息
        :return:
        """
        stu = self.__updating_student()
        self.__controller.update_student(stu)

    def __updating_student(self):
        """
        待修改的学生信息录入
        :return: 更改后的学生信息
        """
        stu = model.StudentModel("", 0, 0, 0)
        stu.id = self.__input_error("id")
        stu.name = input("请输入姓名:")
        stu.age = self.__input_error("年龄:")
        stu.score = self.__input_error("分数:")
        return stu

    def __sort_student_by_score(self):
        """
        将学生按成绩由低到高进行排序
        :return:
        """
        self.__controller.sort_student_by_score()

    def __input_error(self, input_value):
        while True:
            try:
                target_value = int(input("请输入" + input_value))
            except ValueError:
                print("请输入int类型值!!!")
                continue
            return target_value
