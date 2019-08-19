class StaffIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


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

    def __iter__(self):
        si = StaffIterator(self.__staff_list)
        return si
        # for i in range(len(self.__staff_list)):
        #     yield self.__staff_list[i]


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


staff1 = Programmer(200,300)
staff2 = Salesman(2333,34)
stamana = StaffManager()
stamana.add_staff(staff1)
stamana.add_staff(staff2)
iterator = stamana.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key)
    except StopIteration:
        break