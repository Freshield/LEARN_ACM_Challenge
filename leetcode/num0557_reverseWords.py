# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0557_reverseWords.py
@Time: 2020-07-22 10:06
@Last_update: 2020-07-22 10:06
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
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
    解法：
    1. 利用分割字符串的方法
    2. 利用双指针的方法
    """
    def reverseWords(self, s):
        """
        整体流程：
        1. 进行特判
        2. 生成left, right双指针等参数变量，字符串最后加上空格
        3. 遍历字符
        4. 当遇到空格时更新left，right并复制中间反转字符
        5. 返回结果
        """
        # 1. 进行特判
        if len(s) <= 1:
            return s

        # 2. 生成left, right双指针等参数变量，字符串最后加上空格
        left = 0
        rst_list = []
        s += ' '

        # 3. 遍历字符
        for i in range(len(s)):
            # 4. 当遇到空格时更新left，right并复制中间反转字符
            if s[i] == ' ':
                rst_list.append(s[left: i][::-1])
                left = i+1

        # 5. 返回结果
        return ' '.join(rst_list)

    def reverseWords_split(self, s):
        return ' '.join([word[::-1] for word in s.split(' ')])


if __name__ == '__main__':
    words = "Let's take LeetCode contest"
    print(Solution().reverseWords(words))