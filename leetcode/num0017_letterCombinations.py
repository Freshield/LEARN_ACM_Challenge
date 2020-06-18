# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0017_letterCombinations.py
@Time: 2020-06-18 10:40
@Last_update: 2020-06-18 10:40
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
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母
    解法：
    使用回溯算法, 添加，递归，回溯
    """
    def __init__(self):
        self.num_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.rst_list = []

    def letterCombinations(self, digits=None, nums_list=[], words=''):
        """
        整体流程：
        1. 生成字符串列表
        2. 回溯递归
        """
        # 1. 生成字符串列表
        if digits is not None:
            if len(digits) == 0:
                return []
            for num in digits:
                nums_list.append(self.num_dict[num])

        # 2. 回溯递归
        if len(nums_list) == 0:
            self.rst_list.append(words)
            return self.rst_list

        for word in nums_list[0]:
            # 添加
            words += word
            # 递归
            self.letterCombinations(nums_list=nums_list[1:], words=words)
            # 回溯
            words = words[:-1]

        return self.rst_list


if __name__ == '__main__':
    digits = "2"
    print(Solution().letterCombinations(digits))