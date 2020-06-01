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
    解法：
    并查集，分为find和union两个部分，find部分就是查找公共祖先，同时做路径压缩
    union部分是集合部分，合并两个圈子，同时做按秩合并
    """
    def __init__(self):
        self.left_move = [1, 0, -1, 0]
        self.up_move = [0, 1, 0, -1]

        self.parent = dict()
        self.rank = dict()
        self.total_nums = -1

    def find(self, x):
        """
        查找自己的祖先
        """
        self.parent[x] = self.parent[x] if self.parent[x] == x else self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        """
        合并x,y
        """
        # 找到parent
        parent_x = self.find(x)
        parent_y = self.find(y)

        # 如果两个不同
        if parent_x != parent_y:
            # 保证x为秩大的那个
            if self.rank[parent_x] < self.rank[parent_y]:
                parent_x, parent_y = parent_y, parent_x

            # 合并
            self.parent[parent_y] = parent_x

            # 处理秩相同的时候
            if self.rank[parent_x] == self.rank[parent_y]:
                self.rank[parent_x] += 1

            # 减少数量
            self.total_nums -= 1

    def numIslands(self, grid):
        """
        使用并查集
        整体流程：
        1. 创建所有需要的队列
        2. 遍历岛屿
        3. 如果是‘1’则使用并查
        4. 返回总体数量
        """
        if len(grid) == 0:
            return 0

        # 1. 创建所有需要的队列
        up_length, left_length = len(grid), len(grid[0])
        self.parent = {(up, left): (up, left) for up in range(up_length) for left in range(left_length)}
        self.rank = {(up, left): 1 for up in range(up_length) for left in range(left_length)}
        self.total_nums = up_length * left_length

        # 2. 遍历岛屿
        for up in range(up_length):
            for left in range(left_length):
                # 3. 如果是‘1’则使用并查
                if grid[up][left] == '1':
                    # this_pos = up * left_length + left
                    for i in range(4):
                        move_up, move_left = self.up_move[i], self.left_move[i]
                        move_up = up + move_up
                        move_left = left + move_left
                        if (0 <= move_up < up_length) and (0 <= move_left < left_length) and (
                            grid[move_up][move_left] == '1'):
                            # move_pos = move_up * left_length + move_left
                            self.union((up, left), (move_up, move_left))
                else:
                    self.total_nums -= 1

        return self.total_nums

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

    def numIslands_dfs(self, grid):
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
    # grid = [
    #     ["1","1","1"],
    #     ["0","1","0"],
    #     ["1","1","1"]]
    print(Solution().numIslands(grid))