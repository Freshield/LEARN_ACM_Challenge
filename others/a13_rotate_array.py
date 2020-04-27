# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a13_rotate_array.py
@Time: 2020-04-25 18:24
@Last_update: 2020-04-25 18:24
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def rotate_once(input_array):
    """
    旋转一次矩阵
    整体流程：
    1. 生成返回的矩阵
    2. 遍历把原矩阵的位置的数值赋给新的矩阵
    3. 返回新矩阵
    """
    # 1. 生成返回的矩阵
    rst_array = [[-1 for _ in range(len(input_array))] for _ in range(len(input_array))]

    # 2. 遍历把原矩阵的位置的数值赋给新的矩阵
    for i in range(len(input_array)):
        for j in range(len(input_array)):
            rst_array[j][len(input_array)-i-1] = input_array[i][j]

    return rst_array


def rotate_array(input_array, times):
    """
    旋转矩阵
    整体流程：
    1. 得到需要的旋转次数
    2. 遍历调用旋转矩阵
    """
    # 1. 得到需要的旋转次数
    times = times % 4

    # 2. 遍历调用旋转矩阵
    for _ in range(times):
        input_array = rotate_once(input_array)

    return input_array


if __name__ == '__main__':
    input_array = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    times = 2
    rst_array = rotate_array(input_array, times)
    print(rst_array)