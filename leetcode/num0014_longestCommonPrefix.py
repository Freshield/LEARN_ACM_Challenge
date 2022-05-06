# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0014_longestCommonPrefix.py
@Time: 2020-05-25 10:07
@Last_update: 2020-05-25 10:07
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
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    解法：
    遍历水平扫描
    """
    def longestCommonPrefix(self, strs):
        """
        整体流程：
        1. 遍历最短的那个字符
        2. 比较字符，看是否都有
        """
        if len(strs) == 0:
            return ''
        # 1. 遍历最短的那个字符
        length_list = [(i, len(strs[i])) for i in range(len(strs))]
        length_list.sort(key=lambda x: x[1])
        min_str = strs[length_list[0][0]]

        # 2. 比较字符，看是否都有
        index = 0
        while index != len(min_str):
            for str in strs:
                if str[index] != min_str[index]:
                    return min_str[: index]

            index += 1

        if index == 0:
            return ''
        else:
            return min_str


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))