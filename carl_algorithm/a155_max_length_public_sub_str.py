# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a155_max_length_public_sub_str.py
@Time: 2022-11-01 19:59
@Last_update: 2022-11-01 19:59
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def max_length_public_sub_str(text1, text2):
    """
    最长公共子序列，使用动态规划
    状态，两个字符的索引位置，条件，当前字符是否相同
    1. dp含义，dp[i][j]表示1-i的text1，1-i的text2，位置的最长公共子序列
    2. dp逻辑，dp[i][j]由两种可能性组成，
    如果text1[i]==text2[j]，那么已经匹配，dp[i][j]=1+dp[i-1][j-1]
    否则，dp[i][j]为dp[i-1][j]或dp[i][j-1]的最长公共子序列
    3. dp启动，补齐text1，text2开头特殊字符，用于处理索引问题
    dp[0][j]，dp[i][0]都为0，因为0字符匹配都为0
    4. dp遍历，i由小到大1-i，j由小到大1-j
    5. dp范例，
    """
    # 3. dp启动，补齐text1，text2开头特殊字符，用于处理索引问题
    #     dp[0][j]，dp[i][0]都为0，因为0字符匹配都为0
    text1 = '!' + text1
    text2 = '!' + text2
    dp = [[0] * (len(text2)) for _ in range(len(text1))]
    # 4. dp遍历，i由小到大1-i，j由小到大1-j
    for i in range(1, len(text1)):
        for j in range(1, len(text2)):
            # 2. dp逻辑，dp[i][j]=1+dp[i-1][j-1]
            # dp[i][j]为dp[i-1][j]或dp[i][j-1]的最长公共子序列
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
                continue
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


if __name__ == '__main__':
    text1 = 'abcde'
    text2 = 'ace'
    print(max_length_public_sub_str(text1, text2))
