class User:
    def __init__(self, name, attack_power, blood):
        self.name = name
        self.attack_power = attack_power
        self.blood = blood

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def attack(self, enemy):
        enemy.blood -= self.attack_power
        score = 0
        if enemy.blood <= 0:
            score += 1
            print("敌人死亡,你现在的分数为：", score)
        else:
            print("敌人还有%d的血量" % enemy.blood)


class Enemy:
    def __init__(self, name, attack_power, blood):
        self.name = name
        self.attack_power = attack_power
        self.blood = blood

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def attack(self, user):
        user.blood -= self.attack_power
        if user.blood <= 0:
            print("你已死亡,游戏结束")
        else:
            print("你还剩%d的血量"%user.blood)


user1 = User("蜘蛛侠",500,1000)
enemy1 = Enemy("绿恶魔",500,900)
print(user1.name)
user1.attack(enemy1)
enemy1.attack(user1)
user1.attack(enemy1)
enemy1.attack(user1)