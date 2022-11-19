# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a131_min_cost_climbing.py
@Time: 2022-10-20 19:24
@Last_update: 2022-10-20 19:24
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def min_cost_climbing(cost):
    """
    使用最小花费爬楼梯，使用动态规划
    1. dp矩阵含义，dp[i]表示第i阶台阶的最小花费
    2. dp矩阵递推公式，dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    3. dp初始化，dp[0]=cost[0]，dp[1]=cost[1]，由于cost会少一位，最后加个0cost为最终结果
    4. dp遍历方向，从小到大
    5. dp范例矩阵，[10, 15, 30, 15]
    """
    if len(cost) <= 1:
        return min(cost)
    # 3. dp初始化，dp[0]=cost[0]，dp[1]=cost[1]，由于cost会少一位，最后加个0cost为最终结果
    dp = [-1] * (len(cost) + 1)
    cost += [0]
    dp[0] = cost[0]
    dp[1] = cost[1]
    # 4. dp遍历方向，从小到大
    for i in range(2, len(dp)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    return dp[-1]


if __name__ == '__main__':
    cost = [10, 15, 20]
    print(min_cost_climbing(cost))
