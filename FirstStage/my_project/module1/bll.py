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