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
