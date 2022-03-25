# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a17_two_sum.py
@Time: 2022-04-14 16:19
@Last_update: 2022-04-14 16:19
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def two_sum(nums, target):
    """
    计算两数之后
    转换为看有没有找到target-num的问题
    1. 创建num的字典
    2. 遍历nums
    3. 如果target-num在字典中则返回相应位置
    4. 否则把值和位置放到字典中
    """
    # 1. 创建num的字典
    num_dict = dict()
    # 2. 遍历nums
    for index, num in enumerate(nums):
        # 3. 如果target-num在字典中则返回相应位置
        if (target-num) in num_dict:
            return num_dict[target-num], index

        # 4. 否则把值和位置放到字典中
        num_dict[num] = index

    return -1, -1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
