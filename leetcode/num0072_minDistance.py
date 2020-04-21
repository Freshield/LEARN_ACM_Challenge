#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0072_minDistance.py
@Time: 2020-04-21 16:38
@Last_update: 2020-04-21 16:38
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
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符
        替换一个字符
    解法：使用递归或者DP
    如果使用递归注意边界条件
    1. dp代表什么：dp[i, j]代表word1[0:i]变为word2[0:j]所需要的操作数
    2. dp的转换公式：
        如果word1[i]等于word2[j]，代表这步不需要操作，只看前边就好，dp[i,j] = dp[i-1, j-1]
        不相等的话就要比较三种操作：
            替换：替换的话相当于把word1[i]替换为word2[j]，只需要看前边就好，所以dp[i, j] = dp[i-1, j-1] + 1，加一是代表替换操作
            删除：删除的话把word1[i]删除了，所以继续前边比较，dp[i, j] = dp[i-1, j] + 1
            添加：添加的话相当于word1[i]后边添加了和word2[j]一样的字符，所以再继续和word2前一个比较，dp[i, j] = dp[i, j-1] + 1
    3. dp初始值：
        为了方便，在dp多加以为空字符，这样方便边界条件，字符比较的时候需要减1操作
        dp[0, j] = 0,1,...,j-1相当于word1为空字符变为word2那么一直加就好了
        dp[i, 0] = 0,1,...,i-1相当于word2为空字符word1只需要一直减就好了
    4. dp遍历方式：
        i的依赖为向左，j的依赖为向上，所以都从小到大遍历
    """
    def minDistance(self, word1, word2):
        """
        整体流程：
        1. 生成dp矩阵以及需要的变量
        2. 对dp矩阵初始化
        3. 遍历i, j
        4. 如果字符相同的情况
        5. 如果字符不同的情况
        """
        # 1. 生成dp矩阵以及需要的变量
        dp = np.zeros((len(word1)+1, len(word2)+1), dtype=int)

        # 2. 对dp矩阵初始化
        dp[0, :] = list(range(len(word2)+1))
        dp[:, 0] = list(range(len(word1)+1))

        # 3. 遍历i, j
        for i in range(1, dp.shape[0]):
            for j in range(1, dp.shape[-1]):
                # 4. 如果字符相同的情况
                if word1[i-1] == word2[j-1]:
                    dp[i, j] = dp[i-1, j-1]
                # 5. 如果字符不同的情况
                else:
                    dp[i, j] = min(
                        dp[i-1, j-1] + 1,
                        dp[i-1, j] + 1,
                        dp[i, j-1] + 1
                    )

        return int(dp[-1, -1])


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    # word1 = "intention"
    # word2 = "execution"
    print(Solution().minDistance(word1, word2))