# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0121_maxProfit.py
@Time: 2020-04-20 22:23
@Last_update: 2020-04-20 22:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np


class Solution:
    """
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），
    设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。
    """

    def maxProfit_dp(self, prices):
        """
        使用动态规划的方法
        解法：
        1. dp代表什么，dp[i][是否持股][卖出次数]代表当前最大的profit
        2. dp转换关系：
            dp[i][0][0]代表没有买卖，没有持股，所以为0
            dp[i][1][0]代表没有买卖，但是没有卖出过，有可能有两种情况
                dp[i-1][1][0]之前就有持股或者dp[i-1][0][0] - prices[i]之前没有持股刚买
            dp[i][1][1]代表买过一次，又持股了，这里只允许卖一次，所以这些值都为-1e6
            dp[i][0][1]代表没有持股，卖出一次，有可能有两种情况
                dp[i-1][0][1]之前就已经卖出或者dp[i-1][1][0] + prices[i]之前有持股刚卖

            dp[i][0][0] = 0
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])
            dp[i][1][1] = -1e6
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0] + prices[i])
        3. 初始化条件：
            dp[0][0][0] = 0
            dp[0][0][1] = -1e6因为不可能第一次时就已经卖出过
            dp[0][1][0] = -prices[0]代表第一开始就买入
        4. 如何遍历：
            i的依赖方向向左，所以从小到达遍历
        整体流程：
        1. 生成dp矩阵等中间需要的变量
        2. 生成初始化数值
        3. 遍历i
        4. 更新dp的数值
        5. 返回最终的结果
        """
        # 1. 生成dp矩阵等中间需要的变量
        dp = np.zeros((len(prices), 2, 2), dtype=np.int32)
        # 2. 生成初始化数值
        dp[:, 0, 0] = 0
        dp[0, 0, 1] = -1e6
        dp[0, 1, 0] = -prices[0]
        dp[:, 1, 1] = -1e6
        print(dp)
        # 3. 遍历i
        for i in range(1, len(prices)):
            # 4. 更新dp的数值
            dp[i, 1, 0] = max(dp[i-1, 1, 0], dp[i-1, 0, 0] - prices[i])
            dp[i, 0, 1] = max(dp[i-1, 0, 1], dp[i-1, 1, 0] + prices[i])
            print(i)
            print(dp)
            print()

        # 5. 返回最终的结果
        return max(dp[len(prices)-1, 0, 1], 0)

    def maxProfit(self, prices):
        """
        整体流程：
        1. 生成相关变量
        2. 计算最小值
        3. 计算和最小值的差
        4. 看是否更新最大收益
        """
        # 1. 生成相关变量
        min_val = None
        max_profit = 0

        # 2. 计算最小值
        for price in prices:
            # 2. 计算最小值
            min_val = price if (min_val is None) or (price < min_val) else min_val
            # 3. 计算和最小值的差
            profit = price - min_val
            # 4. 看是否更新最大收益
            max_profit = max_profit if profit < max_profit else profit

        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
    print(Solution().maxProfit_dp(prices))