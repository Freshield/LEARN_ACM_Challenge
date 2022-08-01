# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a129_fib_sequence.py
@Time: 2022-10-20 17:33
@Last_update: 2022-10-20 17:33
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def fib_sequence(n):
    """
    生成斐波那契数列，使用动态规划
    1. dp数组含义，dp[i]为fib第i个数的数值
    2. dp递推公式，dp[i]=dp[i-1]+dp[i-2]
    3. dp初始化，dp[0]=0，dp[1]=1
    4. dp遍历方向，从小到大
    5. dp数组举例，[0 1 1 2 3 5 8 13]
    """
    # 处理特殊情况
    if n <= 1:
        return n
    # 3. dp初始化，dp[0]=0，dp[1]=1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    # 4. dp遍历方向，从小到大
    for i in range(2, n+1):
        # 2. dp递推公式，dp[i]=dp[i-1]+dp[i-2]
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == '__main__':
    n = 4
    print(fib_sequence(n))
