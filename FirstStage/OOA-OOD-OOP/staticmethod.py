class Enemy:
    def __init__(self, name, blood, basic_attack_power, defensive_power):
        self.name = name
        self.blood = blood
        self.basic_attack_power = basic_attack_power
        self.defensive_power = defensive_power

    def __str__(self):
        return "%s-%d-%d-%d"%(self.name,self.blood,self.basic_attack_power,self.defensive_power)

    @staticmethod
    def find_name(target, name):
        for item in target:
            if item.name == name:
                item.print_info()

    @staticmethod
    def find_blood(target,blood):
        for item in target:
            if item.blood == blood:
                item.print_info()

    @staticmethod
    def average_attack_power(target):
        total_power = 0
        count = 0
        for item in target:
            count += 1
            total_power += item.basic_attack_power
        return total_power/count

    @staticmethod
    def fine_defensive_power(target,defensive_power1):
        for i in range(len(target)-1,-1,-1):
            if target[i].defensive_power < defensive_power1:
                target.remove(target[i])
        for item in target:
            item.print_info()

    @staticmethod
    def add_attack_power(target,power):
        for item in target:
            item.basic_attack_power += power
        for item in target:
            item.print_info()


enemy1 = Enemy("灭霸", 0, 95, 95)
print(enemy1)
enemy2 = Enemy("章鱼博士", 60, 30, 25)
enemy3 = Enemy("蜥蜴博士", 60, 30, 9)
enemy4 = Enemy("绿恶魔", 70, 50, 50)

