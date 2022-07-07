# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a153_01bag.py
@Time: 2022-10-30 17:44
@Last_update: 2022-10-30 17:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def bag01(W, N, weights, vals):
    """
    01背包问题，用动态规划
    状态，背包容量，物品个数。选择，取物品，不取物品。
    1. dp含义，dp[i][j]表示背包容量为j时，前i个物品的最大价值
    2. dp逻辑，dp[i][j]时在取第i个物品，和不取第i个物品中选择价值最大的可能。
    如果不选第i个物品，则最大价值为dp[i-1][j]也就是当前背包容量，前i-1个物品的最大价值。
    如果选第i个物品，那么当前肯定有vals[i]，同时背包容量为W-weights[i]，那么当前最大价值
    为dp[i-1][W-weights[i]]也就是前i-1个物品在剩下容量中最大的含量，所有公式如下
    dp[i][j] = max(dp[i-1][j], dp[i-1][W-weights[i]]
    3. dp启动，dp[i][0]都为0，也就是没有空间什么都放不了，dp[0][j]都为0，没有物品也都放不了
    4. dp遍历，i从小到大1-N，j从小到大1-W
    5. dp范例，
    """
    # 3. dp启动，dp[i][0]都为0，也就是没有空间什么都放不了，dp[0][j]都为0，没有物品也都放不了
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    # 加入虚拟物品，补齐遍历顺序
    weights = [0] + weights
    vals = [0] + vals
    # 4. dp遍历，i从小到大1-N，j从小到大1-W
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            # 如果放不下则只能不放
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + vals[i])

    return dp[-1][-1]


if __name__ == '__main__':
    W = 4
    N = 3
    weights = [1, 3, 4]
    vals = [15, 20, 30]
    print(bag01(W, N, weights, vals))
