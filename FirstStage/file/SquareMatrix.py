def create_square_matrix(square_length):
    """
    创建一个方阵
    :param square_length: 方阵的长度
    :return: 返回一个列表
    """
    list2 = []
    for i in range(square_length):
        list1 = []
        for j in range(square_length * i + 1, square_length * (i + 1) + 1):
            if len(list1) < square_length:
                list1.append(j)
        list2.append(list1)
    print(list2)
    return list2


def square_matrix_transpose(list_target):
    """
    方阵转置函数
    :return:方阵转置之后的列表
    """
    for i in range(len(list_target)):
        for j in range(i + 1, len(list_target)):
            list_target[i][j], list_target[j][i] = list_target[j][i], list_target[i][j]


map1 = [
    [2, 0, 0, 4],
    [2, 2, 0, 4],
    [4, 4, 0, 2],
    [4, 2, 2, 4]
]
square_matrix_transpose(map1)
