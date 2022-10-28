# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a147_stock_max_profit.py
@Time: 2022-10-30 12:38
@Last_update: 2022-10-30 12:38
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def stock_max_profit(prices):
    """
    买卖股票的最佳时机，使用贪心法，找左边最小的价格和右边最高的价格
    1. 创建最小值和最大值profit
    2. 遍历所有的price
    3. 对比得到当前的最小值
    4. 计算当前的最大profit
    """
    # 1. 创建最小值和最大值profit
    min_price, max_profit = prices[0], 0
    # 2. 遍历所有的price
    for price in prices:
        # 3. 对比得到当前的最小值
        min_price = min(min_price, price)
        # 4. 计算当前的最大profit
        max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 5, 4, 3]
    print(stock_max_profit(prices))
