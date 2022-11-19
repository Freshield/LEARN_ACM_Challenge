# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a15_two_array_cross_r.py
@Time: 2022-10-08 16:19
@Last_update: 2022-10-08 16:19
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
    获取两个数据的交集
    使用集合的交并方法
    """
    return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]

    print(two_array_cross(nums1, nums2))
