# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0062_uniquePaths.py
@Time: 2020-06-17 11:01
@Last_update: 2020-06-17 11:01
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
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？
    解法：
    使用动态规划
    1. dp的含义：dp[i, j]代表到i行j列的路径数
    2. dp的转换公式：dp[i, j] = dp[i-1, j] + dp[i, j-1]
    3. dp的初始化：dp[0, ...]只能一个一个走，递增，dp[..., 0]同样
    4. dp的遍历，i的依赖i-1，j的依赖j-1，从小到大比阿里你
    """
    def uniquePaths(self, m, n):
        """
        整体流程：
        1. 初始化dp矩阵并处理特殊情况
        2. 遍历i,j
        3. 根据dp更新矩阵
        """
        # 1. 初始化dp矩阵并处理特殊情况
        dp = dict()
        for i in range(m):
            dp[i, 0] = 1
        for j in range(n):
            dp[0, j] = 1

        # 2. 遍历i,j
        for i in range(1, m):
            for j in range(1, n):
                # 3. 根据dp更新矩阵
                dp[i, j] = dp[i-1, j] + dp[i, j-1]

        return dp[m-1, n-1]


if __name__ == '__main__':
    m = 3
    n = 2
    m = 7
    n = 3
    print(Solution().uniquePaths(m, n))