# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a152_different_bst.py
@Time: 2022-10-30 16:50
@Last_update: 2022-10-30 16:50
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def different_bst(n):
    """
    求1-n为节点，组成的二叉搜索树有多少种，使用动态规划
    1. dp含义，dp[i]表示i个元素能组成的二叉树有多少种
    2. dp逻辑，从1-i遍历j，表示用j当根节点时候的搜索树数量，把结果累加
    其中，用j当根节点，因为二叉搜索树的特性，左子树会有j-1个节点，右子树会有i-j个节点，
    而两边的节点相互不影响，所有共有dp[j-1]*dp[i-j-1]种可能性，所以最终公式为
    dp[i] += dp[j-1] * dp[i-j]
    3. dp启动，dp[0]=1，因为空树只有一种情况，dp[1]=1
    4. dp遍历，i从小到大2-n，j从小到大1-i
    5. dp范例，[1, 1, 2, 5]
    """
    # 3. dp启动，dp[0]=1，因为空树只有一种情况，dp[1]=1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    # 4. dp遍历，i从小到大2-n，j从小到大1-i
    for i in range(2, n+1):
        for j in range(1, i+1):
            # 2. dp逻辑，dp[i] += dp[j-1] * dp[i-j]
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[-1]


if __name__ == '__main__':
    n = 5
    print(different_bst(n))