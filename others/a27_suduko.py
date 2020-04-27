#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a27_suduko.py
@Time: 2020-04-26 15:25
@Last_update: 2020-04-26 15:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution(object):
    """
    数独是一个我们都非常熟悉的经典游戏，运用计算机我们可以很快地解开数独难题，
    现在有一些简单的数独题目，请编写一个程序求解。
    解法：
    使用回溯算法，求解所有位置
    """
    target_str = '0'

    def is_valid(self, input_str_list, i, j, val):
        """
        看当前位置放这个val是否可以
        整体流程：
        1. 看横行
        2. 看竖行
        3. 看3x3的区域
        """
        # 1. 看横行
        for index in range(len(input_str_list)):
            if input_str_list[i][index] == val:
                return False
        # 2. 看竖行
        for index in range(len(input_str_list)):
            if input_str_list[index][j] == val:
                return False
        # 3. 看3x3的区域
        left_min = (j // 3) * 3
        up_min = (i // 3) * 3
        for left in range(left_min, left_min+3):
            for up in range(up_min, up_min+3):
                if input_str_list[up][left] == val:
                    return False

        return True

    def backtrack(self, input_str_list, i, j):
        """
        回溯部分
        整体流程：
        1. 如果i越界则返回True
        2. 如果当前不为target_str继续递归
        3. 遍历数值
        4. 看数值是否符合
        5. 选择，递归，回溯
        6. 如果j越界则回行
        7. 如果返回True则返回True
        """
        # 1. 如果i越界则返回True
        if i == len(input_str_list):
            return True
        if j == len(input_str_list):
            return self.backtrack(input_str_list, i+1, 0)
        # 2. 如果当前不为target_str继续递归
        if input_str_list[i][j] != self.target_str:
            return self.backtrack(input_str_list, i, j+1)

        # 3. 遍历数值
        for val in range(1, 10):
            # 4. 看数值是否符合
            if self.is_valid(input_str_list, i, j, str(val)):
                # 5. 选择，递归，回溯
                input_str_list[i][j] = str(val)
                if self.backtrack(input_str_list, i, j+1):
                    return True
                input_str_list[i][j] = self.target_str

    def suduko(self, input_str_list):
        """
        整体流程：
        1. 调用递归程序
        """
        self.backtrack(input_str_list, 0, 0)


def input_to_str():
    while True:
        try:
            input_str = ''
            for i in range(9):
                input_str += input()+'\n'
            input_str_list = [[i for i in sub_str.split(' ') if i != ''] for sub_str in input_str.split('\n') if sub_str != '']
            Solution().suduko(input_str_list)
            for i in range(len(input_str_list)):
                print(' '.join(input_str_list[i]))
        except Exception as e:
            break


if __name__ == '__main__':
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    with open('test.txt', 'r') as f:
        board = f.read()
    board = [[i.strip() for i in sub_str.split(' ') if i != ''] for sub_str in board.split('\n') if sub_str != '']
    for sub_board in board:
        print(sub_board)
    print()
    Solution().suduko(board)
    for i in range(len(board)):
        print(' '.join(board[i]))