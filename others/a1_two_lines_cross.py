#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_two_lines_cross.py
@Time: 2020-04-14 17:24
@Last_update: 2020-04-14 17:24
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def cube_inter(line1_pos, line2_pos):
    """
    判断线段组成的两个矩形是否相交
    整体流程：
    1. 得到两个矩形的左上角和右下角
    2. 判断两个右下角是否都在两个矩形左上角的右下方
    """
    (p0_x,p0_y), (p1_x,p1_y) = line1_pos
    (p2_x,p2_y), (p3_x,p3_y) = line2_pos

    # 1. 得到两个矩形的左上角和右下角
    left0_x = min(p0_x, p1_x)
    left0_y = min(p0_y, p1_y)
    rigth0_x = max(p0_x, p1_x)
    right0_y = max(p0_y, p1_y)

    left1_x = min(p2_x, p3_x)
    left1_y = min(p2_y, p3_y)
    right1_x = max(p2_x, p3_x)
    right1_y = max(p2_y, p3_y)

    # 2. 判断两个右下角是否都在两个矩形左上角的右下方
    if (min(rigth0_x, right1_x) >= max(left0_x, left1_x)) and \
            (min(right0_y, right1_y) >= max(left0_y, left1_y)):
        return True
    else:
        return False


def calc_cross(point0, point1, point2):
    """计算p0p1和p0p2的叉乘"""
    x0 = point1[0] - point0[0]
    y0 = point1[1] - point0[1]
    x1 = point2[0] - point0[0]
    y1 = point2[1] - point0[1]

    return x0 * y1 - x1 * y0


def cross_test(line1_pos, line2_pos):
    """
    测试跨立实验
    解法：
    如果两线段交叉则从线段1的一个点向线段2的两条线段和线段1计算叉乘符号应相反
    因为右边的向量叉乘左边的向量应该为负数
    整体流程：
    1. 构建向量p2p0,p2p1
    2. 计算两个叉乘结果的积看是否为负数
    """
    # 1. 构建向量p2p0,p2p1
    (p0_x, p0_y), (p1_x, p1_y) = line1_pos
    (p2_x, p2_y), (p3_x, p3_y) = line2_pos

    # 2. 计算两个叉乘结果的积看是否为负数
    # p2p0 x p2p3
    cross1 = calc_cross((p2_x,p2_y),(p0_x,p0_y),(p3_x,p3_y))
    # p2p1 x p2p3
    cross2 = calc_cross((p2_x,p2_y),(p1_x,p1_y),(p3_x,p3_y))

    if cross1 * cross2 <= 0:
        return True
    else:
        return False


def two_lines_cross(line1_pos, line2_pos):
    """
    判断两条线段是否相交
    解法：
    先通过判断线段矩形是否相交，如果相交再使用跨立实验
    整体流程：
    1. 判断矩形是否相交
    2. 使用跨立实验
    """
    if cube_inter(line1_pos, line2_pos):
        if cross_test(line1_pos, line2_pos) and cross_test(line2_pos, line1_pos):
            return True

    return False


if __name__ == '__main__':
    line1_pos = ((1,0),(0,1))
    line2_pos = ((3,0),(2,1))

    # line1_pos = ((0,0),(3,3))
    # line2_pos = ((2,0),(0,2))

    # line1_pos = ((1,0),(0,1))
    # line2_pos = ((1,1),(3,3))

    print(two_lines_cross(line1_pos, line2_pos))