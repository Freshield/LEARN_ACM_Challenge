#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_triangle.py
@Time: 2020-04-13 10:28
@Last_update: 2020-04-13 10:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def triangle(n, stick_list: list):
    """
    从n个棍子选3个组成周长尽可能长的三角形，如果无法组成三角形则输出0
    解法：
    能组成三角形则最长长度小其他两个之和
    整体流程：
    1. 对棍子排序
    2. 按照从大到小遍历棍子
    3. 如果可以组成则为最长
    4. 如果都不行，则返回0
    """
    # 1. 对棍子排序
    stick_list.sort(reverse=True)

    # 2. 按照从大到小遍历棍子
    max_length = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                if stick_list[a] < stick_list[b] + stick_list[c]:
                    # 3. 如果可以组成则为最长
                    max_length = stick_list[a] + stick_list[b] + stick_list[c]
                    return max_length

    # 4. 如果都不行，则返回0
    return max_length


if __name__ == '__main__':
    stick_list = [2,3,4,5,10]
    stick_list = [4,5,10,20]
    max_length = triangle(len(stick_list), stick_list)
    print(max_length)
