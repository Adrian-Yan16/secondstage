class User:
    def __init__(self, name, attack_power, blood):
        self.name = name
        self.attack_power = attack_power
        self.blood = blood

    def __str__(self):
        return ("姓名:%s，攻击力:%d，血量:%d" % (self.name, self.attack_power, self.blood))

    def __repr__(self):
        return ('User("%s",%d,%d)' % (self.name, self.attack_power, self.blood))


u1 = User("灭霸", 2000, 5500)
u2 = str(u1)
print(u2)
u4 = repr(u1)
print(u4)
u3 = eval(repr(u1))
u3.name = "绿恶魔"
print(u3)
