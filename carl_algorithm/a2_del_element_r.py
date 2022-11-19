# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_del_element_r.py
@Time: 2022-08-31 12:20
@Last_update: 2022-08-31 12:20
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def del_element(nums, val):
    """
    删除指定的元素并返回新数组长度
    使用双指针法，慢指针指向目标值，快指针指向非目标值
    整体流程：
    1. 生成快慢指针等变量
    2. 遍历直到快指针越界
    3. 如果快指针指向的值不是target 则拷贝到慢指针 快慢都加一
    4. 如果快指针指向是target 则只快指针加一
    """
    # 1. 生成快慢指针等变量
    slow = 0
    # 2. 遍历直到快指针越界
    for fast in range(len(nums)):
        # 3. 如果快指针指向的值不是target 则拷贝到慢指针 快慢都加一
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        # 4. 如果快指针指向是target 则只快指针加一

    return slow


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(del_element(nums, val))

