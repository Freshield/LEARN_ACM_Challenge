# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a73_del_num.py
@Time: 2022-10-09 14:02
@Last_update: 2022-10-09 14:02
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def del_num(nums, target):
    """
    删除数组中的目标数字
    1. 创建left指针，遍历nums通过right指针
    2. 如果right指代的值不是target则复制right的值到left，且left加一
    3. 如果是，则跳过
    """
    # 1. 创建left指针，遍历nums通过right指针
    left = 0
    for right in range(len(nums)):
        # 2. 如果right指代的值不是target则复制right的值到left
        if nums[right] != target:
            nums[left] = nums[right]
            left += 1
        # 3. 如果是，则跳过

    return left


if __name__ == '__main__':
    nums = [2, 3, 3, 2]
    target = 3
    print(del_num(nums, target))
