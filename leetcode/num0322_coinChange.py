#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0322_coinChange.py
@Time: 2020-04-27 12:52
@Last_update: 2020-04-27 12:52
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
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
    如果没有任何一种硬币组合能组成总金额，返回 -1。
    解法：
    使用动态规划
    1. dp的意义：dp[i]代表amount为i时的最少硬币数
    2. dp的选择项：
        i. 对于不同面额的硬币，dp[i]=dp[i-coin] + 1，其中i-coin要大于等于0
    3. dp的转换公式：
        dp[i] = min(dp[i]，dp[i-coin] + 1)
    4. dp的初始值：
        dp[0] = 0
        dp[i] = -1，i<0
    5. dp的遍历方式：
        i的依赖向左，所以i从小到大遍历
    """
    def coinChange(self, coins, amount):
        """
        整体流程：
        1. 构建dp矩阵
        2. 生成dp矩阵的初始值
        3. 遍历amount的数值
        4. 遍历硬币的数值
        5. 更新dp矩阵的值
        6. 返回最终的结果
        """
        if (amount == 0) or (len(coins) == 0):
            return 0
        # 1. 构建dp矩阵
        dp = [float('inf') for i in range(amount+1)]
        # 2. 生成dp矩阵的初始值
        dp[0] = 0
        # 3. 遍历amount的数值
        for i in range(1, amount+1):
            # 4. 遍历硬币的数值
            for coin in coins:
                # 5. 更新dp矩阵的值
                if (i - coin) < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[i] if dp[i] != float('inf') else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    coins = [2]
    amount = 3
    print(Solution().coinChange(coins, amount))
