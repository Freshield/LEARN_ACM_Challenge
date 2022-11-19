# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a17_two_sum_r.py
@Time: 2022-10-08 16:54
@Last_update: 2022-10-08 16:54
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
    两数之和
    1. 构建所需的num字典
    2. 遍历nums
    3. 如果rev_num在num字典中则返回相应的index
    4. 否则把数值和index放到num字典中
    """
    # 1. 构建所需的num字典
    num_dict = dict()

    # 2. 遍历nums
    for index, num in enumerate(nums):
        # 3. 如果rev_num在num字典中则返回相应的index
        rev_num = target - num
        if rev_num in num_dict:
            return [index, num_dict[rev_num]]

        # 4. 否则把数值和index放到num字典中
        num_dict[num] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
