# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0037_solveSudoku.py
@Time: 2020-04-24 23:36
@Last_update: 2020-04-24 23:36
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
    编写一个程序，通过已填充的空格来解决数独问题。
    一个数独的解法需遵循如下规则：
    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    空白格用 '.' 表示。
    解法：
    使用回溯算法
    """
    def valid_val(self, board, i, j, val):
        """
        整体流程：
        1. 判断横向是否合法
        2. 判断纵向是否合法
        3. 判断3x3区域是否合法
        """
        for index in range(9):
            # 1. 判断横向是否合法
            if board[i][index] == val:
                return False
            # 2. 判断纵向是否合法
            elif board[index][j] == val:
                return False

        # 3. 判断3x3区域是否合法
        left_min = (j // 3) * 3
        up_min = (i // 3) * 3
        for left in range(left_min, left_min+3):
            for up in range(up_min, up_min+3):
                if board[up][left] == val:
                    return False

        return True

    def backtrack(self, board, i, j):
        """
        整体流程：
        1. 结束条件：i == 9时越界
        2. 变换行条件：j == 9时换行
        3. 跳过条件：当前位置已有数字
        4. 遍历数字：
        5. 判断是否合法
        6. 选择，递归，回溯
        """
        # 1. 结束条件：i == 9时越界
        if i == 9:
            return True

        # 2. 变换行条件：j == 9时换行
        if j == 9:
            return self.backtrack(board, i+1, 0)

        # 3. 跳过条件：当前位置已有数字
        if board[i][j] != '.':
            return self.backtrack(board, i, j+1)

        # 4. 遍历数字：
        for val in [str(i+1) for i in range(9)]:
            # 5. 判断是否合法
            if self.valid_val(board, i, j, val):
                # 6. 选择，递归，回溯
                board[i][j] = val
                if self.backtrack(board, i, j+1) is True:
                    return True
                board[i][j] = '.'

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        整体流程：
        1. 调用回溯算法
        """
        self.backtrack(board, 0, 0)



if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    for sub in board:
        print(sub)
    Solution().solveSudoku(board)
    print()
    for sub in board:
        print(sub)
