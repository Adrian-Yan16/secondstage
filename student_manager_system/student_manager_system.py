"""
    student_manager_system.py
    学生管理器系统

    项目计划:一.
            数据模型类：StudentModel
            逻辑控制类：StudentManagerController
                数据：学生列表 __stu_list
                行为：获取列表 stu_list,
                     添加学生 add_student
		            编号逻辑:自增的整数
	       二.在界面视图类中输出学生__output_students.
"""


class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0):
        """
            创建学生对象
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = None
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    """
        学生管理控制器,负责处理对学生列表的逻辑操作.
    """

    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_target):
        """
            添加学生
        :param stu_target: 需要添加的学生对象
        """
        stu_target.id = self.__generate_id()
        self.__stu_list.append(stu_target)

    def __generate_id(self):
        # 类名.类变量  增加1
        StudentManagerController.__init_id += 1
        # 返回类变量
        return StudentManagerController.__init_id

# -------------------
# 测试添加学生
# c = StudentManagerController()
# m = StudentModel("张无忌",28,100)
# c.add_student(m)
# c.add_student(StudentModel("赵敏",28,100))
#
# for item in c.stu_list:
#     print(item.name,item.id)

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

    def __select_menu_item(self):
        item = input("请您输入选项:")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            pass
        elif item == "4":
            pass

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_students(self):
        # 调用逻辑控制类的add_student方法
        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名:")
            if stu.name == "":
                break
            stu.age = int(input("请输入年龄:"))
            stu.score = int(input("请输入成绩:"))
            self.__controller.add_student(stu)

    def __output_students(self):
        for item in self.__controller.stu_list:
            print(item.id,item.name,item.age,item.score)

# 程序入口
view = StudentManagerView()#
view.main()























