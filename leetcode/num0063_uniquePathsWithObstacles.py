# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0063_uniquePathsWithObstacles.py
@Time: 2020-07-13 10:19
@Last_update: 2020-07-13 10:19
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
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    解法：
    使用dp动态规划
    1. dp的含义：dp[i][j]代表第i行j列的路径数
    2. dp的状态方程：
        a. 如果num[i][j]为1则dp[i][j]为0
        b. 否则dp[i][j] = dp[i-1][j] + dp[i][j-1]
    3. dp的初始化：dp[0][...] = 1, 直到遇到1
                 dp[...][0] = 1, 直到遇到1
                 其他初始化为0
    4. 遍历方向：i，j的依赖方向向左向上，所以从小到大遍历
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        整体流程：
        1. 进行特判
        2. 初始化dp矩阵等变量
        3. 遍历矩阵
        4. 进行状态更新
        5. 返回最后的路径结果
        """
        # 1. 进行特判
        if len(obstacleGrid) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 2. 初始化dp矩阵等变量
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break

        # 3. 遍历矩阵
        for i in range(1, m):
            for j in range(1, n):
                # 4. 进行状态更新
                if obstacleGrid[i][j] == 1:
                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # 5. 返回最后的路径结果
        return dp[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [
        [0,0,0,1],
        [0,1,0,1],
        [0,0,0,0]
    ]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))