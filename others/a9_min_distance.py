# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a9_min_distance.py
@Time: 2020-04-24 21:34
@Last_update: 2020-04-24 21:34
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
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符
        替换一个字符
    解法：使用动态规划方法
    1. dp代表什么：dp[i, j]代表word1的第i位变为word2的第j为所需的最少步数
    2. dp的转换公式：
        i. 当word1的第i位等于word2的第j位的时候，也就是说这位不用变
        只需要看前边的就可以了，所以dp[i, j] = dp[i-1, j-1]

        当不相等时共有三种情况：
        ii. 如果选择插入则dp[i, j] = dp[i, j-1] + 1，因为插入的话插入
        的字符和word2的第j位相同，则只要看前边的就可以了
        iii. 如果选择删除则dp[i, j] = dp[i-1, j] + 1，因为删除的话
        word1的第i位就没有了，只需要比较i-1位和word2的j位即可
        iv. 如果选择替换则dp[i, j] = dp[i-1, j-1] + 1，因为替换的话
        word1的第i位就和word2的第j位相等了，继续比较之前的即可
    3. dp初始值：
        这里为了方便，给word1和word2多加上一个空字符的情况，
        所以dp[i, 0]和dp[0, j]就相当于word2为空和word1为空
        的情况，只需要一直插入或者一直删除即可
    4. 遍历方式：
        这里i的依赖方向为左边，j的依赖方向为上边，所有i，j都从小到大遍历即可
    5. 需要注意的：
        需要注意i和j的方向问题，列表索引哪个在前那个在后
    """
    def min_distance(self, word1, word2):
        """
        整体流程：
        1. 生成dp矩阵以及中间变量
        2. 遍历i，j
        3. 判断当前位置的值是否相同
        4. 取其他三种情况的最小值
        5. 返回最终结果
        """
        # 1. 生成dp矩阵以及中间变量
        m = len(word1)
        n = len(word2)
        dp = [[('unknown', (-1, -1), -1) for j in range(n)] for i in range(m)]
        for i in range(m):
            dp[i][0] = ('del', (i-1, 0), i)
        for j in range(n):
            dp[0][j] = ('insert', (0, j-1), j)
        dp[0][0] = ('begin', (0, 0), 0)

        # 2. 遍历i，j
        for j in range(1, n):
            for i in range(1, m):
                # 3. 判断当前位置的值是否相同
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = ('skip', (i-1, j-1), dp[i-1][j-1][2])
                # 4. 取其他三种情况的最小值
                else:
                    dp[i][j] = min(
                        ('replace', (i-1, j-1), dp[i-1][j-1][2] + 1),
                        ('del', (i, j-1), dp[i][j-1][2] + 1),
                        ('insert', (i-1, j), dp[i-1][j][2] + 1),
                        key=lambda x: x[2]
                    )

        return dp, dp[m-1][n-1][2]






if __name__ == '__main__':
    import numpy as np
    word1 = "horse"
    word2 = "ros"
    # word1 = "intention"
    # word2 = "execution"
    dp, min_step = Solution().min_distance(word1, word2)
    print(np.array(dp))
    print(min_step)