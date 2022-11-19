# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a149_different_path_2.py
@Time: 2022-10-30 14:39
@Last_update: 2022-10-30 14:39
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def different_path_2(grid_list):
    """
    有障碍的不同路径，使用动态规划
    1. dp含义，dp[i][j]表示第i行，第j列的路径数量，m为i，n为j
    2. dp公式，如果grid[i][j]不为1，dp[i][j] = dp[i-1][j] + dp[i][j-1]，因为只能从这两个方向获取
    3. dp启动，dp[i][0]在遇到grid为1的格子前都是1，dp[0][j]在遇到grid为1的格子前都是1
    4. dp遍历，i从小到大遍历1-m，j从小到大遍历1-n，前提是grid对应格子为0
    5. dp范例，[1, 1, 1] [1, 0, 1] [1, 1, 2]
    """
    # 3. dp启动，dp[i][0]在遇到grid为1的格子前都是1，dp[0][j]在遇到grid为1的格子前都是1
    m, n = len(grid_list), len(grid_list[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if grid_list[i][0] == 1:
            break
        dp[i][0] = 1
    for j in range(n):
        if grid_list[0][j] == 1:
            break
        dp[0][j] = 1
    # 4. dp遍历，i从小到大遍历1-m，j从小到大遍历1-n，前提是grid对应格子为0
    for i in range(1, m):
        for j in range(1, n):
            if grid_list[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


if __name__ == '__main__':
    grid_list = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(different_path_2(grid_list))
