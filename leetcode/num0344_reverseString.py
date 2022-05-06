#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0344_reverseString.py
@Time: 2020-04-21 12:31
@Last_update: 2020-04-21 12:31
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
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
    不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
    你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
    解法：
    遍历判断是否到中间，然后调换数值
    """
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        整体流程：
        1. 遍历s
        2. 结束条件：s
        3. 交换数值
        """
        if len(s) == 0:
            return None
        # 1. 遍历s
        for i in range(len(s)//2 + 1):
            # 2. 结束条件：s
            if i > (len(s) - i - 1):
                break
            # 3. 交换数值
            tmp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = tmp


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    # s = ["H", "a", "n", "n", "a", "h"]
    # s = ['a']
    # s = []
    # for i in range(len(s)//2 + 1):
    #     if i > len(s)-i-1:
    #         break
    #     print(i)
    #     print(s[i])
    #     print(len(s)-i -1)
    #     print(s[len(s)-i-1])
    #     print()
    Solution().reverseString(s)
    print(s)