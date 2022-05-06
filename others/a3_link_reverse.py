#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_link_reverse.py
@Time: 2020-04-15 10:12
@Last_update: 2020-04-15 10:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class LinkPoint(object):
    def __init__(self, value, next_point):
        self.value = value
        self.next_point = next_point

    def __str__(self):
        return '%s, %s' % (str(self.value), str(self.next_point))


def print_link_points(start_point: LinkPoint):
    next_point = start_point
    while True:
        print(next_point.value)
        next_point = next_point.next_point
        if next_point is None:
            break


def link_reverse(start_point: LinkPoint):
    """
    让链表反转
    解法：
    创造一个tmp_point
    整体流程：
    1. 得到下一个连接点
    2. 更改当前的连接点
    3. 更新上一个连接点
    4. 更新当前连接点
    5. 终止条件为下一个连接点为None
    """
    last_point = None
    this_point = start_point
    next_point = LinkPoint(-1, this_point.next_point)
    while True:
        # 1. 得到下一个连接点
        next_point.next_point = this_point.next_point
        # 2. 更改当前的连接点
        this_point.next_point = last_point
        # 3. 更新上一个连接点
        last_point = this_point
        # 4. 更新当前连接点
        this_point = next_point.next_point
        # 5. 终止条件为下一个连接点为None
        if this_point is None:
            break

    return last_point


if __name__ == '__main__':
    last_point = None
    for i in range(10, -1, -1):
        this_point = LinkPoint(i, last_point)
        # print(this_point.value)
        last_point = this_point

    # exit()

    print_link_points(last_point)
    print()
    start_point = link_reverse(last_point)
    print_link_points(start_point)