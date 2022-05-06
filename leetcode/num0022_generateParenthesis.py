# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0022_generateParenthesis.py
@Time: 2020-06-09 10:31
@Last_update: 2020-06-09 10:31
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
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    解法：
    1. 使用dfs，生成深度树
    2. 使用动态规划
        1. dp的含义：dp[n]表示括号数为n时的组合
        2. dp的转移方程：当第n个括号时，一共有两种可能
            在括号中间，或者在括号右侧
            dp[n] = (dp[i])dp[j]，其中i+j=n-1
            i从0 - n-1，j从n-1 - 0
        3. dp的初始化：
        dp[0] = ''
        dp[1] = '()'
        4. dp的遍历方向：
        n依赖于n-1，所以遍历方向从小到大

    """
    def __init__(self):
        self.parenthesis_list = []

    def generateParenthesis(self, n):
        """
        使用动态规划：
        1. 处理特殊情况
        2. 生成dp矩阵
        3. 初始化dp矩阵
        4. 从小到大遍历n
        5. 遍历i，j
        6. 遍历i，j中的组合
        7. 返回最终的矩阵
        """
        # 1. 处理特殊情况
        if n == 0:
            return []

        # 2. 生成dp矩阵
        dp = [[] for _ in range(n+1)]

        # 3. 初始化dp矩阵
        dp[0] = ['']
        dp[1] = ['()']

        # 4. 从小到大遍历n
        for index in range(2, n+1):
            # 5. 遍历i，j
            for i in range(index):
                j = index - 1 - i
                # 6. 遍历i，j中的组合
                for i_val in dp[i]:
                    for j_val in dp[j]:
                        dp[index].append(f'({i_val}){j_val}')

        return dp[n]


    def generateParenthesis_dfs(self, n, word='', left=0, right=0):
        """
        使用dfs来进行深度有线搜索
        整体流程：
        1. 如果left = right = n则存储
        2. 如果right > left 则剪枝返回
        3. 添加左括号
        4. 添加右括号
        """
        if n == 0:
            return self.parenthesis_list

        # 1. 如果left = right = n则存储
        if left == right == n:
            self.parenthesis_list.append(word)
        # 2. 如果right > left 则剪枝返回
        elif right > left:
            pass
        elif (left > n) or (right > n):
            pass
        else:
            # 3. 添加左括号
            self.generateParenthesis(n, word+'(', left+1, right)
            # 4. 添加右括号
            self.generateParenthesis(n, word+')', left, right+1)

        return self.parenthesis_list


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))