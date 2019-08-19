class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def age(self):
        return self.__hp

    @age.setter
    def age(self, hp):
        if 10 <= hp <= 50:
            self.__hp = hp
        else:
            raise ValueError("No")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, atk):
        if 10 <= atk <= 50:
            self.__atk = atk
        else:
            raise ValueError("No")


enemy1 = Enemy("小丑", 20, 20)
enemy1.hp = 30
enemy1.atk = 40
print(enemy1.hp)
print(enemy1.atk)
print(enemy1.__dict__)
