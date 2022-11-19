# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a154_best_time_buy_stock.py
@Time: 2022-10-31 20:57
@Last_update: 2022-10-31 20:57
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def best_time_buy_stock(prices):
    """
    买卖股票最好时机，动态规划
    状态，有无股票，条件，买不买股票
    1. dp含义，dp[i][j]表示第i天最大利润，j为有无股票，0为无，1为有
    2. dp逻辑，dp[i][0]表示第i天手里没有股票，这个由两种条件构成，
    昨天没有股票，今天也没有股票也就是dp[i-1][0]，或者昨天有股票，今天卖了
    也就是dp[i-1][1]+prices[i]。dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])
    dp[i][1]表示第i天手里有股票，这个由两种条件构成，昨天有股票，今天继续持有，也就是dp[i-1][1]，
    另一种是昨天没有，今天买了，也就是dp[0]-prices[i]，这里用dp[0]是因为此条件只允许买卖一次
    dp[i][1]=max(dp[i-1][1], dp[0]-prices[i])
    3. dp启动，dp[0][0]=0最开始是没有欠款的，dp[0][1]=-prices[0]因为相当于最开始就买了股票
    4. dp遍历，i是从小到大1-prices的长度，j从小到大0，1
    5. dp范例，[0, -7] [0, -1]
    """
    # 3. dp启动，dp[0][0]=0最开始是没有欠款的，dp[0][1]=-prices[0]因为相当于最开始就买了股票
    dp = [[0, 0] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    # 4. dp遍历，i是从小到大1-prices的长度，j从小到大0，1
    for i in range(1, len(prices)):
        # 2. dp逻辑，dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])
        # dp[i][1]=max(dp[i-1][1], dp[0]-prices[i])
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[0][0] - prices[i])

    return dp[-1][0]


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(best_time_buy_stock(prices))
