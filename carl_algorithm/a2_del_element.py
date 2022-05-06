# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_del_element.py
@Time: 2022-04-11 18:33
@Last_update: 2022-04-11 18:33
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def del_element(nums, target):
    """
    删除数组中目标元素
    使用双指针法
    1. 建立快慢指针并遍历快指针
    2. 如果不是同时指向的值为target，则把快指针的值赋给慢指针，并且慢指针+1
    """
    # 1. 建立快慢指针并遍历快指针
    slow_index = 0
    for fast_index in range(len(nums)):
        # 2. 如果不是同时指向的值为target，则把快指针的值赋给慢指针，并且慢指针+1
        if not (nums[fast_index] == target):
            nums[slow_index] = nums[fast_index]
            slow_index += 1

    return slow_index


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    nums = [3, 2, 2, 3]
    val = 3
    rst_index = del_element(nums, val)
    print(rst_index)
    print(nums[: rst_index])
