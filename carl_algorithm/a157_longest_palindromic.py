# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a157_longest_palindromic.py
@Time: 2022-11-03 15:25
@Last_update: 2022-11-03 15:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def longest_palindromic(s):
    """
    最长回文子串，用动态规划
    1. 状态，子串的位置，条件，是否新加入的字符为回文
    2. dp含义，dp[i][j]，为第i到第j的字符的最长回文子串，左闭右闭
    3. dp逻辑，dp[i][j]如果要是回文串，则dp[i+1][j-1]为回文串且s[i]==s[j]
    dp[i][j]=dp[i+1][j-1]+2，否则为dp[i+1][j-1]
    4. dp初始化，dp[i][j]相等的地方都为1，i<j的地方都为-1因为不合法，
    dp[i][i+1]如果两个相等都为2
    5. dp遍历，dp[i][j]依赖于dp[i+1][j-1]也就是依赖为左下，所以需要倒序，从右下向左上
    i从大到小字符长度到2，j从小到大i+2到字符长度
    6. dp范例
    """
    # 4. dp初始化，dp[i][j]相等的地方都为1，i<j的地方都为-1因为不合法，
    # dp[i][i+1]如果两个相等都为2
    dp = [[False] * len(s) for _ in range(len(s))]
    max_len = 1
    begin = 0
    for i in range(len(s)):
        dp[i][i] = True
        if (i + 1) < len(s):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if max_len == 1:
                    max_len = 2
                    begin = i

    # 5. dp遍历，dp[i][j]依赖于dp[i+1][j-1]也就是依赖为左下，所以需要倒序，从右下向左上
    #     i从大到小字符长度到2，j从小到大i+2到字符长度
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 2, len(s)):
            # 3. dp逻辑，dp[i][j]如果要是回文串，则dp[i+1][j-1]为回文串且s[i]==s[j]
            #     dp[i][j]=dp[i+1][j-1]+2，否则为dp[i+1][j-1]
            if (dp[i + 1][j - 1]) and (s[i] == s[j]):
                dp[i][j] = True
                this_len = j + 1 - i
                if this_len > max_len:
                    max_len = this_len
                    begin = i

    return s[begin: begin+max_len]


if __name__ == '__main__':
    s = 'babad'
    print(longest_palindromic(s))
