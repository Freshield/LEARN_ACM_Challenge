# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a130_climb_stairs.py
@Time: 2022-10-20 17:44
@Last_update: 2022-10-20 17:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def climb_stairs(n):
    """
    爬楼梯，使用动态规划
    1. dp数组含义，dp[i]表示第i个楼梯的方法数
    2. dp递归公式，dp[i] = dp[i-1] + dp[i-2]
    3. dp初始化，dp[1] = 1，dp[2] = 2
    4. dp遍历方向，从小到大
    5. dp数组例子，[1 2 3 5 8]
    """
    # 处理空的情况
    if n <= 2:
        return n
    # 3. dp初始化，dp[1] = 1，dp[2] = 2
    dp = [-1] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    # 4. dp遍历方向，从小到大
    for i in range(3, n + 1):
        # 2. dp递归公式，dp[i] = dp[i-1] + dp[i-2]
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == '__main__':
    n = 5
    print(climb_stairs(n))
