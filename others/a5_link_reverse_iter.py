#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_link_reverse_iter.py
@Time: 2020-04-17 10:00
@Last_update: 2020-04-17 10:00
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


# def print_link_points(start_point: LinkPoint):
#     next_point = start_point
#     while True:
#         print(next_point)
#         next_point = next_point.next_point
#         if next_point is None:
#             break


def link_reverse_iter(this_point: LinkPoint, last_point: LinkPoint):
    """
    反转链表，递归
    解法：
    目的，反转节点
    结束条件，下一个节点为None
    等价条件，减小范围到下一个节点
    整体流程：
    1. 判别是否到最后一个节点，如果是则返回
    2. 反转单个节点
    3. 递归
    """
    # 1. 判别是否到最后一个节点，如果是则返回
    if this_point is None:
        return last_point

    # 2. 反转单个节点
    this_next_point = this_point.next_point
    this_point.next_point = last_point

    # 3. 递归
    return link_reverse_iter(this_next_point, this_point)


if __name__ == '__main__':
    last_point = None
    for i in range(10, -1, -1):
        this_point = LinkPoint(i, last_point)
        last_point = this_point


    # exit()

    print(last_point)
    print()
    start_point = link_reverse_iter(last_point, None)
    print(start_point)
