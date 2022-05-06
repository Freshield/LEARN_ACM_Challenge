#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0122_maxProfit.py
@Time: 2020-04-21 10:49
@Last_update: 2020-04-21 10:49
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
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    解法：
    使用动态规划
    1. dp的含义：dp[i][是否持有股]，dp代表当前的最大利润
    2. dp的关系公式：
        dp[i][0]代表当前不持有股，共有两种可能
            dp[i-1][0]之前也不持有股或者dp[i-1][1] + prices[i]之前持有股今天卖了
        dp[i][1]代表当前持有股，共有两种可能
            dp[i-1][1]之前就持有股或者dp[i-1][0] - prices[i]今天刚买的股
    3. dp的初始值
        dp[0][0] = 0
        dp[0][1] = -prices[0]代表到一天就买了
    4. dp遍历方式
        i依赖于左边，所以从小到大遍历
    """
    def maxProfit(self, prices):
        """
        整体流程：
        1. 生成dp矩阵等所需变量
        2. 生成初始值
        3. 遍历i
        4. 更新dp矩阵
        5. 返回最高价，注意要大于等于0
        """
        # 1. 生成dp矩阵等所需变量
        dp = np.zeros((len(prices), 2), dtype=np.int32)
        # 2. 生成初始值
        dp[0, 0] = 0
        dp[0, 1] = -prices[0]
        # 3. 遍历i
        for i in range(1, len(prices)):
            # 4. 更新dp矩阵
            dp[i, 0] = max(dp[i-1, 0], dp[i-1, 1] + prices[i])
            dp[i, 1] = max(dp[i-1, 1], dp[i-1, 0] - prices[i])

        # 5. 返回最高价，注意要大于等于0
        return max(dp[-1, 0], 0)


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    # prices = [1,2,3,4,5]
    # prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))