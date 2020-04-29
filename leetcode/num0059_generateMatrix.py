# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0059_generateMatrix.py
@Time: 2020-05-03 10:34
@Last_update: 2020-05-03 10:34
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
    给定一个正整数 n，生成一个包含 1 到 n2 所有元素，
    且元素按顺时针顺序螺旋排列的正方形矩阵。
    解法：
    使用坐标指针方法生成正常的螺旋矩阵的方法
    """
    def generateMatrix(self, n):
        """
        整体流程：
        1. 生成返回矩阵和坐标指针等变量
        2. 遍历n**2次
        3. 移动指针
        4. 更改坐标条件为越界或已经有值
        5. 返回返回矩阵
        """
        if n == 1:
            return [[1]]
        # 1. 生成返回矩阵和坐标指针等变量
        rst_list = [[None for _ in range(n)] for _ in range(n)]
        move_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        move_index = 0
        left_pos = 0
        up_pos = 0

        # 2. 遍历n**2次
        for i in range(n**2):
            rst_list[up_pos][left_pos] = i+1
            # 3. 移动指针
            move_pos = move_list[move_index % 4]
            left_pos += move_pos[0]
            up_pos += move_pos[1]
            # 4. 更改坐标条件为越界或已经有值
            if (0 <= left_pos < n) and (0 <= up_pos < n) and \
                    (rst_list[up_pos][left_pos] is None):
                continue
            else:
                left_pos -= move_pos[0]
                up_pos -= move_pos[1]
                move_index += 1
                move_pos = move_list[move_index % 4]
                left_pos += move_pos[0]
                up_pos += move_pos[1]

        return rst_list


if __name__ == '__main__':
    n = 3
    matrix = Solution().generateMatrix(n)
    list(map(print, matrix))