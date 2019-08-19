class StaffManager:
    def __init__(self):
        self.__staff_list = []

    @property
    def geometric(self):
        return self.__staff_list

    def add_staff(self, staff):
        self.__staff_list.append(staff)

    def total_salary(self):
        total = 0
        for item in self.__staff_list:
            total += item.calculate_salary()
        return total


class Staff:
    def __init__(self, basic_salary, extraordinary_pay):
        self.basic_salary = basic_salary
        self.extraordinary_pay = extraordinary_pay

    def calculate_salary(self):
        raise NotImplementedError


class Programmer(Staff):
    def __init__(self, basic_salary, extraordinary_pay):
        super().__init__(basic_salary, extraordinary_pay)

    def calculate_salary(self):
        return self.basic_salary + self.extraordinary_pay


class Salesman(Staff):
    def __init__(self, basic_salary, extraordinary_pay):
        super().__init__(basic_salary, extraordinary_pay)

    def calculate_salary(self):
        return self.basic_salary + self.extraordinary_pay * 2


g1 = StaffManager()
c1 = Programmer(5000, 3000)
r1 = Salesman(4000, 2000)
g1.add_staff(c1)
g1.add_staff(r1)
print(g1.total_salary())

