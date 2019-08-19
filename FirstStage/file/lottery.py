"""
(1)随机产生一注彩票（7个数），前6个数不可重复（1-33），蓝球（1-16）
(2)提示：
        输入第一个号码：
        输入第二个号码：
        号码不在范围内
        号码已重复
        输入蓝球号码：
"""


# 随机产生彩票
import random

list_lottery = []
i = 0
# 6个不重复的红球及一个蓝球
while i < 6:
    random_number = random.randint(1, 33)
    # 若数字不重复，则存储
    if random_number not in list_lottery:
        list_lottery.append(random_number)
    else:
        i -= 1
    i += 1
random_number2 = random.randint(1, 16)
list_lottery.append(random_number2)

# 用户输入红球彩票数值
user_list_lottery = []
i = 0
# 用户输入6个红球的数及一个蓝球的数
while i < 6:
    user_number = int(input('输入第%d注红球数字：' % (i + 1)))
    if user_number not in range(1, 33):
        print('号码不在范围内')
        continue
    if user_number not in user_list_lottery:
        user_list_lottery.append(user_number)
        i += 1
    else:
        print('号码重复！！！')

# 用户输入蓝球数值
blue_number = int(input('请输入蓝球数值（1-16）：'))
user_list_lottery.append(blue_number)
print('彩票结果为：', list_lottery)
print('你的号码为：', user_list_lottery)

# 用户的彩票与实际彩票比较
count = 0
i = 0
while i < 7:
    if list_lottery[i] == user_list_lottery[i]:
        count += 1
    i += 1
print('你中了%d注' % count)
