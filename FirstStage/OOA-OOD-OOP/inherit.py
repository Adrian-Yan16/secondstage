"""
老张开车去东北
"""
class Vehical:
    def transport(self, position):
        pass


class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehical, position):
        vehical.transport(position)


class Car(Vehical):
    def transport(self, position):
        print("开车去", position)


class Airplane(Vehical):
    def transport(self, position):
        print("坐飞机去", position)

car = Car()
air = Airplane()
per = Person("老张")
per.go_to(car, "东北")
per.go_to(air, "东北")
