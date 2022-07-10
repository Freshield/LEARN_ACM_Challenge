# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a150_integer_split_max.py
@Time: 2022-10-30 15:58
@Last_update: 2022-10-30 15:58
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def integer_split_max(n):
    """
    整数分拆至少两个后，最大的乘积，使用动态规划
    1. dp含义，dp[i]为分拆数字i后，最大的乘积
    2. dp逻辑，因为dp[i]必须至少分拆为两个，所以这里从2遍历到i-1的j，因为dp[1]没有意义
    dp[i]有两个来源，j*(i-j)和dp[j]*(i-j)，这是因为dp[j]表示必须拆分后的最大乘积
    而j为不拆分的值，有可能不拆分的数值会更大，所以这里需要取两种方式的最大值
    dp[i] = max(j, dp[j]) * (i - j)，同时，由于会遍历j次，所以还要和以及遍历的值进行比较
    所以最终为dp[i] = max(dp[i], max(j, dp[j]) * (i - j))
    3. dp初始化，dp[2] = 1
    4. dp遍历，i从小到大3-n，j从小到大2-i-1
    5. dp范例，[1, 2, 4]
    """
    # 3. dp初始化，dp[2] = 1
    dp = [-1] * (n + 1)
    dp[2] = 1
    # 4. dp遍历，i从小到大3-n，j从小到大2-i-1
    for i in range(3, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], max(j, dp[j]) * (i - j))

    return dp[-1]


if __name__ == '__main__':
    n = 10
    print(integer_split_max(n))
