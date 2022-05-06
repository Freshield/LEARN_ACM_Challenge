# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0240_searchMatrix.py
@Time: 2020-05-23 10:47
@Last_update: 2020-05-23 10:47
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
    编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。
    解法：
    比较左下角的元素，如果比target大则证明最下边一行都比target大，
    如果比target小则证明最左边一列都比target小
    """
    def searchMatrix(self, matrix, target):
        """
        整体流程：
        1. 生成left和down两个坐标
        2. 找到左下角坐标，和target进行比较
        3. 结束条件：如果越界则返回false
        4. 如果相等则返回True
        5. 如果小于target则left右移
        6. 如果大于target则down上移
        """
        if len(matrix) == 0:
            return False

        # 1. 生成left和down两个坐标
        down = len(matrix) - 1
        left = 0
        matrix_length = len(matrix[0])

        # 2. 找到左下角坐标，和target进行比较
        while True:
            # 3. 结束条件：如果越界则返回false
            if (down < 0) or (left >= matrix_length):
                return False

            this_value = matrix[down][left]

            # 4. 如果相等则返回True
            if this_value == target:
                return True
            # 5. 如果小于target则left右移
            elif this_value < target:
                left += 1
            # 6. 如果大于target则down上移
            elif this_value > target:
                down -= 1


if __name__ == '__main__':
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]
    target = 5
    # target = 20
    print(matrix)
    print(Solution().searchMatrix(matrix, target))
