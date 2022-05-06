# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_bisearch.py
@Time: 2022-04-10 22:43
@Last_update: 2022-04-10 22:43
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def bisearch(search_list, target):
    """
    二分查找
    注意区间，左闭右闭
    1. 设定左右指针
    2. 循环遍历
    3. 得到中间位置
    4. 如果中间位置相等则返回
    5. 如果中间位置小于target则设定为右区间
    6. 否则设定为左区间
    """
    # 1. 设定左右指针
    left, right = 0, len(search_list)
    # 2. 循环遍历
    while left <= right:
        # 3. 得到中间位置
        mid = (right - left) // 2 + left
        # 4. 如果中间位置相等则返回
        if search_list[mid] == target:
            return mid
        # 5. 如果中间位置小于target则设定为右区间
        elif search_list[mid] < target:
            left = mid + 1
        # 6. 否则设定为左区间
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(bisearch(nums, target))

