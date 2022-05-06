#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_coin_count.py
@Time: 2020-04-16 10:21
@Last_update: 2020-04-16 10:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def solve(coin_num_list, A, coin_value_list=[1,5,10,50,100,500]):
    """
    1,5,10,50,100,500的硬币各相应的数量，组成A元最少需要多少硬币
    解法：
    贪心算法，用更多的大额硬币支付
    整体流程：
    1. 从最大的硬币开始遍历
    2. 得到当前可以使用的最多硬币
    3. 减小A增加硬币继续
    """
    total_coin_used = 0
    # 1. 从最大的硬币开始遍历
    for i in range(len(coin_num_list)-1, -1, -1):
        # 2. 得到当前可以使用的最多硬币
        coin_used = min(coin_num_list[i], A // coin_value_list[i])
        # 3. 减小A增加硬币继续
        A -= coin_used * coin_value_list[i]
        total_coin_used += coin_used

        if A == 0:
            break

    return total_coin_used


if __name__ == '__main__':
    coin_num_list = [3, 2, 1, 3, 0, 2]
    A = 620
    print(solve(coin_num_list, A))