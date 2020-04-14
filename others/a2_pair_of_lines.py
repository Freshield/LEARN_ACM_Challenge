# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_pair_of_lines.py
@Time: 2020-04-14 22:11
@Last_update: 2020-04-14 22:11
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_line_ab(point1: Point, point2: Point):
    """
    两点确定一条直线
    y = ax + b
    y1 = ax1 + b
    y2 = ax2 + b
    a = (y2-y1)/(x2-x1)
    b = y1 - ax1
    """
    a = (point2.y - point1.y) / (point2.x - point1.x) if point2.x != point1.x else None
    b = point1.y - a * point1.x if a is not None else point2.x

    return a, b


def is_point_at_line(a, b, point):
    """
    判断点是否在线上
    y = ax + b
    由于误差这里可能不相等，所有引入误差值
    """
    if a is not None:
        diff = abs(point.y - a * point.x + b)
        return diff < 1e-8
    else:
        return point.x == b


def is_any_other_point_at_line(a, b, point_list):
    """
    判断是否还有点在线上
    """
    for point in point_list:
        if is_point_at_line(a, b, point):
            return True

    return False


def get_line1(a, b, point_list):
    """
    找到第二条直线
    整体流程：
    1. 遍历point_list找到不在线上的两个点
    2. 如果找不到2个则返回None, None，代表只有一个点或者没有点不在线上，判别成功
    3. 根据两个点生成line2
    """
    line1_point_list = []
    # 1. 遍历point_list找到不在线上的两个点
    for point in point_list:
        if not is_point_at_line(a, b, point):
            line1_point_list.append(point)

        if len(line1_point_list) == 2:
            break

    # 2. 如果找不到2个则返回None, None，代表只有一个点或者没有点不在线上，判别成功
    if len(line1_point_list) < 2:
        return None, None

    # 3. 根据两个点生成line2
    point0, point1 = line1_point_list
    a1, b1 = get_line_ab(point0, point1)

    return a1, b1


def is_point_at_one_of_two_lines(point, a0, b0, a1, b1):
    """判断一个点是否在两条线其中一条线"""
    return is_point_at_line(a0, b0, point) or is_point_at_line(a1, b1, point)


def pair_of_lines(point_list):
    """
    给出一些点，判断是否可以画出两条直线穿过所有的点
    解法：
    首先选出3个点，共有三条线的可能，确定了一条线后，再找第二条线，然后看是否都在这两条线上
    整体流程：
    1. 得到前3个点
    2. 遍历三种情况
    3. 遍历其他点看是否还有共线的点，如果有则证明当前点为一条线也就是那条至少包含3个点的线
    4. 找到两个不在线的点，确定第二条线
    5. 看所有的点在不在这两条线上
    """
    point0, point1, point2 = point_list[:3]

    # 2. 遍历三种情况
    for po, p1, p2 in ((point0, point1, point2), (point0, point2, point1),
                   (point1, point2, point0)):
        a0, b0 = get_line_ab(po, p1)
        # 3. 遍历其他点看是否还有共线的点，如果有则证明当前点为一条线也就是那条至少包含3个点的线
        if not is_any_other_point_at_line(a0, b0, [p2] + point_list[3:]):
            continue

        # 4. 找到两个不在线的点，确定第二条线
        a1, b1 = get_line1(a0, b0, [p2] + point_list[3:])

        if (a1 is None) and (b1 is None):
            return True

        # 5. 看所有的点在不在这两条线上
        for point in point_list:
            if not is_point_at_one_of_two_lines(point, a0, b0, a1, b1):
                continue

        return True

    return False


if __name__ == '__main__':
    # point_list = [
    #     Point(0, 0), Point(0, 1), Point(1, 1),
    #     Point(1, -1), Point(2, 2)]

    point_list = [
        Point(0, 0), Point(1, 0), Point(1, 1),
        Point(2, 1), Point(2, 3)
    ]
    print(pair_of_lines(point_list))