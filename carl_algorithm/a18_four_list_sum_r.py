# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a18_four_list_sum_r.py
@Time: 2022-10-08 17:21
@Last_update: 2022-10-08 17:21
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
    计算四数之和
    主要方法的目的是把O**4的复杂度降低到O**2，把四数之和变为两数之和
    1. 生成sum字典以及count
    2. 遍历A，B中的所有组合，把结果放到sum字典中计数
    3. 遍历C，D中的所有组合，看-sum是否在sum中，如果在则把相应的结果累加上
    """
    # 1. 生成sum字典以及count
    sum_dict, count = dict(), 0

    # 2. 遍历A，B中的所有组合，把结果放到sum字典中计数
    for a in A:
        for b in B:
            sum = a + b
            sum_dict[sum] = sum_dict.get(sum, 0) + 1

    # 3. 遍历C，D中的所有组合，看-sum是否在sum中，如果在则把相应的结果累加上
    for c in C:
        for d in D:
            sum = c + d
            if -sum in sum_dict:
                count += sum_dict[-sum]

    return count


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(four_list_sum(A, B, C, D))
