#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_ants.py
@Time: 2020-04-13 11:24
@Last_update: 2020-04-13 11:24
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def ants(L, n, ants_pos_list: list):
    """
    n只蚂蚁1cm/s爬行在Lcm的杆子上，相遇转头，到头掉下，计算全部落下的最长最短时间
    解法：
    因为蚂蚁不分个体，相遇相当于相互穿过，只需要计算距离最远和最近的即可
    整体流程：
    1. 遍历所有蚂蚁
    2. 计算最长和最短距离
    3. 返回最长最短距离
    """
    min_time = 0
    max_time = 0

    for pos in ants_pos_list:
        min_time = max(min_time, min(pos, L - pos))
        max_time = max(max_time, max(pos, L - pos))

    return min_time, max_time


if __name__ == '__main__':
    L = 10
    ants_pos_list = [2,6,7]

    min_time, max_time = ants(L, len(ants_pos_list), ants_pos_list)
    print(min_time)
    print(max_time)