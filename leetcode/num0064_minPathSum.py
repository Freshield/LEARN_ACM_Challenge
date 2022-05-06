# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0064_minPathSum.py
@Time: 2020-06-23 11:02
@Last_update: 2020-06-23 11:02
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
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。
    解法：
    使用动态规划：
    1. dp的含义：dp[i][j]代表dp第i行第j列的最小路径和
    2. dp的转换公式：dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    3. dp的初始化：dp[i][...]和dp[...][j]是为单方向，一直累加即可
    4. dp的遍历方向：i,j依赖为左和上，从小到大遍历即可
    """
    def minPathSum(self, grid):
        """
        整体流程：
        1. 生成dp矩阵，处理特殊情况
        2. 初始化dp矩阵的相关值
        3. 遍历i,j进行dp矩阵更新
        """
        n = len(grid)
        if n == 0:
            return 0

        m = len(grid[0])
        # 1. 生成dp矩阵，处理特殊情况
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]

        # 2. 初始化dp矩阵的相关值
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, m):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        # 3. 遍历i,j进行dp矩阵更新
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


if __name__ == '__main__':
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(Solution().minPathSum(grid))