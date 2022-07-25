# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t2_testing.py
@Time: 2022-10-21 16:32
@Last_update: 2022-10-21 16:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def simu_square(n):
    """
    使用加减乘除模拟开方操作
    1. 处理特殊情况
    2. 创建左右值
    3. 遍历，迭代步数
    4. 获取中间值，得到中间值的平方
    5. 如果中间值的平方等于n则返回中间值
    6. 如果中间值的平方大于n，则右值等于中间值
    7. 否则左值等于中间值
    """
    # 1. 处理特殊情况
    if n <= 0:
        return 0
    # 2. 创建左右值
    mid = -1
    if n > 1:
        left, right = 0, n
    elif n == 1:
        return 1
    else:
        left, right = n, 1
    # 3. 遍历，迭代步数
    while left < right:
        # 4. 获取中间值，得到中间值的平方
        mid = (left + right) // 2
        mid_squa = mid ** 2
        # 5. 如果中间值的平方等于n则返回中间值
        if (mid_squa == n) or (mid == left) or (mid == right):
            return mid
        # 6. 如果中间值的平方大于n，则右值等于中间值
        if mid_squa > n:
            right = mid
        # 7. 否则左值等于中间值
        else:
            left = mid

    return mid


if __name__ == '__main__':
    n = 8
    a = 2.236
    print(n ** 0.5)
    steps = 50
    print(simu_square(n))


