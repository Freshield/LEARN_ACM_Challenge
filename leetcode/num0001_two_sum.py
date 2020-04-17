#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0001_two_sum.py
@Time: 2020-04-17 12:13
@Last_update: 2020-04-17 12:13
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def twoSum(nums: list, target: int):
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    解法：
    对每个num要寻找target - num，使用字典来存储已经遍历过的数字这样来进行提速
    整体流程：
    1. 遍历nums
    2. 如果能在字典找到target - num则返回
    3. 存索引和值到字典
    """
    value_dict = dict()
    # 1. 遍历nums
    for index, num in enumerate(nums):
        # 2. 如果能在字典找到target - num则返回
        if value_dict.get(target - num, None) is not None:
            return [value_dict[target - num], index]

        value_dict[num] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))