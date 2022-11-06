# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a160_peak_array.py
@Time: 2022-11-10 15:36
@Last_update: 2022-11-10 15:36
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def peak_array(array):
    """
    寻找山峰数组的山峰，使用二分查找，左闭右开区间
    1. 创建左右指针
    2. 遍历，条件为left小于right
    3. 获取mid位置
    4. 判断mid是否为山峰，如果是则返回
    5. 如果mid+1小于mid，表示现在在右区间，right更新为mid
    6. 否则在左区间，left更新为mid+1
    """
    # 1. 创建左右指针
    left, right = 1, len(array) - 1
    # 2. 遍历，条件为left小于right
    while left < right:
        # 3. 获取mid位置
        mid = (left + right) // 2
        # 4. 判断mid是否为山峰，如果是则返回
        if (array[mid - 1] < array[mid]) and (array[mid] > array[mid + 1]):
            return mid
        # 5. 如果mid+1小于mid，表示现在在右区间，right更新为mid
        if array[mid + 1] < array[mid]:
            right = mid
        # 6. 否则在左区间，left更新为mid+1
        else:
            left = mid + 1

    return None


if __name__ == '__main__':
    array = [0, 2, 1, 0]
    print(peak_array(array))
