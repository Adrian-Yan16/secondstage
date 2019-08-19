class StudentModel:
    def __init__(self, id, name, age, score):
        """
        创建学生信息
        :param id:
        :param name:姓名，str类型
        :param age:年龄，int类型
        :param score:分数，int类型
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    """
    学生管理控制器
    """
    # 类变量，创建学生唯一标识符
    id = 0

    def __init__(self):
        """
        私有的学生列表
        """
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_infomation):
        """
        添加学生信息
        :param stu_infomation: 一个StudentModel类
        """
        stu_infomation.id = self.__create_id()
        self.__stu_list.append(stu_infomation)

    def __create_id(self):
        """
        创建id为该学生对象的唯一标识
        :return: 新增学生id
        """
        StudentManagerController.id += 1
        return StudentManagerController.id

    def remove_student(self, stu_id):
        """
        根据学生id删除学生
        :param stu_id: 给定的学生id
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, stu_info):
        """
        根据学生id修改学生信息
        :param stu_id: 目标学生的id
        :param name: 修改后的姓名
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def sort_student_by_score(self):
        """
        将学生按成绩由低到高进行排序
        :return:
        """
        for i in range(len(self.stu_list) - 1):
            k = i
            for j in range(i + 1, len(self.stu_list)):
                if self.stu_list[k].score > self.stu_list[j].score:
                    k = j
            if k != i:
                self.stu_list[i], self.stu_list[k] = self.stu_list[k], self.stu_list[i]
                self.stu_list[i].id, self.stu_list[k].id = self.stu_list[k].id, self.stu_list[i].id


class StudentManagerView:
    """
        学生管理器视图,负责处理界面逻辑.
    """

    def __init__(self):
        self.__controller = StudentManagerController()

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
            stu = StudentModel(name="", age=0, score=0, id=0)
            stu.name = input("请输入姓名:")
            if stu.name == "":
                break
            stu.age = int(input("请输入年龄:"))
            stu.score = int(input("请输入成绩:"))
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
        stu = StudentModel("", 0, 0, 0)
        stu.id = int(input("请输入id:"))
        stu.name = input("请输入姓名:")
        stu.age = int(input("请输入年龄:"))
        stu.score = int(input("请输入成绩:"))
        return stu

    def __sort_student_by_score(self):
        """
        将学生按成绩由低到高进行排序
        :return:
        """
        self.__controller.sort_student_by_score()


stu = StudentManagerView()
stu.main()
# for item in stu:
#     print(item.name,item.age,item.score)
