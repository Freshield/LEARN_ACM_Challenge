# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0054_spiralOrder.py
@Time: 2020-04-23 22:56
@Last_update: 2020-04-23 22:56
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution:
    """
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
    解法：
    把上下左右的步数变成行走列表，同时把已经走过的步数放到set中
    """
    def spiralOrder(self, matrix):
        """
        整体流程：
        1. 生成中间需要的变量和步数列表
        2. 遍历矩阵
        3. 把得到的数值放到返回矩阵中
        """
        if len(matrix) == 0:
            return matrix

        # 1. 生成中间需要的变量和步数列表
        step_x = [1, 0, -1, 0]
        step_y = [0, 1, 0, -1]
        step_index = 0
        step_set = set()
        m = len(matrix)
        n = len(matrix[0])
        x_pos = 0
        y_pos = 0
        rst_list = []

        # 2. 遍历矩阵
        while len(rst_list) != m * n:
            if (x_pos == n) or (y_pos == m) or (x_pos < 0) or (y_pos < 0) or ((x_pos, y_pos) in step_set):
                x_pos -= step_x[step_index]
                y_pos -= step_y[step_index]
                step_index = (step_index + 1) % 4
                x_pos += step_x[step_index]
                y_pos += step_y[step_index]
            else:
                rst_list.append(matrix[y_pos][x_pos])
                step_set.add((x_pos, y_pos))
                x_pos = x_pos + step_x[step_index]
                y_pos = y_pos + step_y[step_index]

        return rst_list



if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    print(Solution().spiralOrder(matrix))