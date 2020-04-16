#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_sarumans_army.py
@Time: 2020-04-16 11:02
@Last_update: 2020-04-16 11:02
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def solve(point_list, R, n):
    """
    直线上有N个点，从这个N各个点选若干个点加标记，让所有点距离R内都有标记点，至少要有多少个标记点
    解法：
    使用贪心算法，从第一个点开始找到R内最后一个点打上标记，再算标记点外第一个点继续
    整体流程：
    1. 找到起始点右边R距离内最后一个点
    2. 打上标记
    3. 找到标记点右边R距离外第一个点设为起始点
    4. 结束条件如果R距离外没有点了则表明已经全部找完
    """
    start_point_index = 0
    mark_count = 0
    mark_index = -1
    while True:
        # 1. 找到起始点右边R距离内最后一个点
        for i in range(start_point_index, n):
            # 这样给每个点都更新的原因是有可能R范围内只有自己，要给自己打标记
            if point_list[i] <= (point_list[start_point_index] + R):
                mark_index = i
            else:
                break

        # 2. 打上标记
        mark_count += 1

        # 为了判别是否还有R距离外的值
        start_point_index = mark_index
        # 3. 找到标记点右边R距离外第一个点设为起始点
        for i in range(mark_index, n):
            if point_list[i] > (point_list[mark_index] + R):
                start_point_index = i
                break

        # 4. 结束条件如果R距离外没有点了则表明已经全部找完
        if start_point_index == mark_index:
            break

    return mark_count


if __name__ == '__main__':
    n = 6
    R = 10
    point_list = [1,7,15,20,30,50]
    print(solve(point_list, R, n))