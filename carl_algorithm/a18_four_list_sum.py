# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a18_four_list_sum.py
@Time: 2022-04-14 16:43
@Last_update: 2022-04-14 16:43
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def four_list_sum(A, B, C, D):
    """
    四个list数的和为0的数量
    1. 建立和的字典
    2. 遍历A, B，然后把相应和的次数存到字典
    3. 遍历C, D，然后找到相应和为零的数量加起来
    """
    # 1. 建立和的字典
    sum_dict = dict()
    # 2. 遍历A, B，然后把相应和的次数存到字典
    for a in A:
        for b in B:
            sum_dict[a+b] = sum_dict.get(a+b, 0) + 1

    # 3. 遍历C, D，然后找到相应和为零的数量加起来
    count = 0
    for c in C:
        for d in D:
            if -(c + d) in sum_dict:
                count += sum_dict[-(c+d)]

    return count


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(four_list_sum(A, B, C, D))
