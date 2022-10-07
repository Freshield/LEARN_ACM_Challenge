# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_bisearch_r.py
@Time: 2022-08-30 23:34
@Last_update: 2022-08-30 23:34
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def bisearch(nums, target):
    """
    二分查找
    使用左闭右开区间
    整体流程：
    1. 定义左右指针，right为列表长度
    2. 因为是左闭右开，所以循环直到left < right
    3. 得到middle，如果等于target则返回
    4. 如果值比target大，则left为middle+1
    5. 如果值比target小，则right为middle
    """
    # 1. 定义左右指针，right为列表长度
    left, right = 0, len(nums)
    # 2. 因为是左闭右开，所以循环直到left < right
    while left < right:
        # 3. 得到middle，如果等于target则返回
        middle = (right + left) // 2
        value = nums[middle]
        if value == target:
            return middle
        # 4. 如果值比target大，则left为middle+1
        elif value > target:
            right = middle
        # 5. 如果值比target小，则right为middle
        else:
            left = middle + 1

    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(bisearch(nums, target))
