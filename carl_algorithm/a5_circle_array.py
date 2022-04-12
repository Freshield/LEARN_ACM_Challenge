# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_circle_array.py
@Time: 2022-04-12 14:21
@Last_update: 2022-04-12 14:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def circle_array(n):
    """
    螺旋矩阵
    注意边界条件，为左闭右开
    1. 设定起始xy指针，遍历xy指针，数值参数，遍历次数，边长
    2. 开始遍历loop次
    3. 开始遍历左到右
    4. 开始遍历上到下
    5. 开始遍历右到左
    6. 开始遍历下到上
    7. 判断是否增加中心点数值
    """
    # 1. 设定起始xy指针，遍历xy指针，数值参数，遍历次数，边长
    begin_x, begin_y = 0, 0
    count = 1
    length = n - 1
    loop = n // 2
    array = [[0] * n for _ in range(n)]
    # 2. 开始遍历loop次
    for _ in range(loop):
        this_x, this_y = begin_x, begin_y
        # 3. 开始遍历左到右
        for _ in range(length):
            array[this_y][this_x] = count
            this_x += 1
            count += 1

        # 4. 开始遍历上到下
        for _ in range(length):
            array[this_y][this_x] = count
            this_y += 1
            count += 1

        # 5. 开始遍历右到左
        for _ in range(length):
            array[this_y][this_x] = count
            this_x -= 1
            count += 1

        # 6. 开始遍历下到上
        for _ in range(length):
            array[this_y][this_x] = count
            this_y -= 1
            count += 1

        length -= 2
        begin_x += 1
        begin_y += 1

    # 7. 判断是否增加中心点数值
    if n % 2 != 0:
        array[n//2][n//2] = count

    return array


if __name__ == '__main__':
    n = 2
    n = 6
    print(circle_array(n))
