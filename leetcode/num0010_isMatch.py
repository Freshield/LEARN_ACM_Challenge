# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0010_isMatch.py
@Time: 2020-05-22 10:56
@Last_update: 2020-05-22 10:56
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
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
    说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
    解法：
    使用记忆化递归
    处理‘.’：判定是否相同或者是.
    处理'*'：两种情况，一种是继续往后匹配，另一种是0次匹配也就是不匹配，如果一直往后匹配，跳过匹配的词后就相当于0次匹配
    记忆化：构建字典，存储结果
    """
    def __init__(self):
        self.memo = dict()
    
    def isMatch(self, s, p, i=0, j=0):
        """
        整体流程：
        1. 处理特殊情况
        2. 如果有结果则返回
        3. 匹配当前字符
        4. 处理*的情况：长度大于1，尝试两种选择的结果
        5. 如果不是*的情况，则递归下一个字串
        """
        # 1. 处理特殊情况
        if len(p) == 0:
            return len(s) == 0

        if j == len(p):
            return i == len(s)

        # 2. 如果有结果则返回
        if (i, j) in self.memo:
            return self.memo[i, j]

        # 3. 匹配当前字符
        char_match = (i != len(s)) and (p[j] in (s[i], '.'))

        # 4. 处理*的情况：长度大于1，尝试两种选择的结果
        if (j < (len(p) - 1)) and (p[j+1] == '*'):
            zero_type = self.isMatch(s, p, i, j+2)
            choose_type = char_match and self.isMatch(s, p, i+1, j)
            self.memo[i, j] = zero_type or choose_type
        # 5. 如果不是*的情况，则递归下一个字串
        else:
            self.memo[i, j] = char_match and self.isMatch(s, p, i+1, j+1)

        return self.memo[i, j]

    def isMatch_rec(self, s, p):
        """
        整体流程：
        1. 处理特殊情况
        2. 匹配当前字符
        3. 处理*的情况：长度大于1，尝试两种选择的结果
        4. 如果不是*的情况，则递归下一个字串
        """
        # 1. 处理特殊情况
        if len(p) == 0:
            return len(s) == 0
        if len(s) == 0:
            return (len(p) == 2) and (p[1] == '*')

        # 2. 匹配当前字符
        char_match = p[0] in (s[0], '.')

        # 3. 处理*的情况：长度大于1，尝试两种选择的结果
        if (len(p) > 1) and (p[1] == '*'):
            zero_res = self.isMatch_rec(s, p[2:])
            choose_res = self.isMatch_rec(s[1:], p) and char_match
            return zero_res or choose_res
        # 4. 如果不是*的情况，则递归下一个字串
        else:
            return char_match and self.isMatch_rec(s[1:], p[1:])


if __name__ == '__main__':
    s = "aa"
    p = "a*"
    # s = ''
    # p = ''
    # s = "ab"
    # p = ".*"
    # s = "aab"
    # p = "c*a*b"
    # s = "mississippi"
    # p = "mis*is*p*."
    # s = "aaaaaaaaaaaaab"
    # p = "a*a*a*a*a*a*a*a*a*a*a*a*b"
    # s = ""
    # p = "c*c*"
    print(Solution().isMatch(s, p))