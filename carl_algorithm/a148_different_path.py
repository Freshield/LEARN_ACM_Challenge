# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a148_different_path.py
@Time: 2022-10-30 14:14
@Last_update: 2022-10-30 14:14
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def different_path(m, n):
    """
    不同路径，使用动态规划
    1. dp含义，dp[i][j]表示第i行第j列的路径数，n为j，m为i
    2. dp公式，dp[i][j] = dp[i-1][j] + dp[i][j-1]，因为只能从这两边过来
    3. dp启动，dp[i][0]都为1，dp[0][j]都为1，因为只有一条线的可能性
    4. dp方向，i从小到大，j从小到大，总体从左上到右下
    5. dp范例，1 1 1 1，1 2 3 4， 1 3 6 10
    """
    # 3. dp启动，dp[i][0]都为1，dp[0][j]都为1，因为只有一条线的可能性
    dp = [[-1] * n for _ in range(m)]
    for j in range(n):
        dp[0][j] = 1
    for i in range(m):
        dp[i][0] = 1
    # 4. dp方向，i从小到大，j从小到大，总体从左上到右下
    for i in range(1, m):
        for j in range(1, n):
            # 2. dp公式，dp[i][j] = dp[i-1][j] + dp[i][j-1]，因为只能从这两边过来
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


if __name__ == '__main__':
    m = 3
    n = 7
    print(different_path(m, n))
