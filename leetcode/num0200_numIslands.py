# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0200_numIslands.py
@Time: 2020-05-27 10:38
@Last_update: 2020-05-27 10:38
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
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
    """
    def __init__(self):
        self.left_move = [1, 0, -1, 0]
        self.up_move = [0, 1, 0, -1]

    def dfs(self, grid, left, up):
        """
        整体流程：
        1. 遍历move
        2. 如果位置是1则继续dfs
        """
        # 1. 遍历move
        for i in range(len(self.left_move)):
            this_left = left + self.left_move[i]
            this_up = up + self.up_move[i]
            if (0 <= this_left < len(grid[0])) and (0 <= this_up < len(grid)):
                # 2. 如果位置是1则继续dfs
                if grid[this_up][this_left] == '1':
                    grid[this_up][this_left] = '0'
                    self.dfs(grid, this_left, this_up)

    def numIslands(self, grid):
        """
        整体流程：
        1. 遍历grid
        2. 如果是0则跳过
        3. 如果是1则调用dfs
        4. 计数
        """
        if len(grid) == 0:
            return 0

        count = 0
        # 1. 遍历grid
        for up in range(len(grid)):
            for left in range(len(grid[0])):
                # 2. 如果是0则跳过
                if grid[up][left] == '0':
                    continue

                grid[up][left] = '0'
                self.dfs(grid, left, up)
                count += 1

        return count


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0']]
    grid = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]
    print(Solution().numIslands(grid))