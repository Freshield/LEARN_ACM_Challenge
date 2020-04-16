#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_fence_repair.py
@Time: 2020-04-16 11:47
@Last_update: 2020-04-16 11:47
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def solve(l_list, n):
    """
    要将一块木板切为N块，每次切断木板时需要的开销为所切木板的长度，求切完所有木板的最小开销
    解法：
    用贪心算法，把问题反过来，把切割问题变成拼接问题，从最小的开始两两拼接直到全长
    整体流程：
    1. 对l_list排序，找出最小和次小
    2. 进行拼接，计算开销
    3. 更新l_list
    4. 结束条件l_list长度为1
    """
    cost = 0
    while True:
        # 1. 对l_list排序，找出最小和次小
        l_list.sort()
        min_0, min_1 = l_list[:2]

        # 2. 进行拼接，计算开销
        stitch = min_0 + min_1
        cost += stitch

        # 3. 更新l_list
        l_list = l_list[2:]
        l_list.append(stitch)

        # 4. 结束条件l_list长度为1
        if len(l_list) == 1:
            break

    return cost


if __name__ == '__main__':
    # l_list = [8, 5, 8]
    l_list = [1,2,3,4,5]
    print(solve(l_list, len(l_list)))