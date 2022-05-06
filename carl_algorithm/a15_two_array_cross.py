# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a15_two_array_cross.py
@Time: 2022-04-14 14:24
@Last_update: 2022-04-14 14:24
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def two_array_cross(nums1, nums2):
    """
    得到两个数组的交叉部分
    通过字典
    1. 遍历nums1得到所有的数值
    2. 遍历nums2，如果在nums1中的则放到共有部分中
    """
    # 1. 遍历nums1得到所有的数值
    dict1 = {key: True for key in nums1}
    # 2. 遍历nums2，如果在nums1中的则放到共有部分中
    cross = list({num for num in nums2 if num in dict1})

    return cross


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(two_array_cross(nums1, nums2))
