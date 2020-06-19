# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0048_rotate.py
@Time: 2020-06-19 10:40
@Last_update: 2020-06-19 10:40
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
    给定一个 n × n 的二维矩阵表示一个图像。
    将图像顺时针旋转 90 度。
    说明：
    你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
    小心的使用一个暂存矩阵来进行转换
    """
    def rotate(self, matrix):
        """
        整体流程：
        1. 进行特例判断
        2. 计算要转换的次数
        3. 计算要选择的元素数量
        4. 进行转换
        """
        # 1. 进行特例判断
        if len(matrix) <= 1:
            return matrix

        # 2. 计算要转换的次数
        n = len(matrix)
        rotate_times = n // 2
        for i in range(rotate_times):
            # 3. 计算要选择的元素数量
            select_items = n - i * 2 - 1
            # 4. 进行转换
            for j in range(select_items):
                matrix[i][j + i], matrix[j+i][n-i-1], matrix[n-i-1][n-i-j-1], matrix[n-i-j-1][i] = (
                    matrix[n - i - j - 1][i], matrix[i][j + i], matrix[j+i][n-i-1], matrix[n-i-1][n-i-j-1]
                )


        return matrix


if __name__ == '__main__':
    n = 3
    n = 4
    n = 5
    matrix = [[i + j * n for i in range(1, n+1)] for j in range(n)]
    print(matrix)
    print(Solution().rotate(matrix))