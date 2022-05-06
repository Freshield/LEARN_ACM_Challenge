# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0151_reverseWords.py
@Time: 2020-07-07 10:10
@Last_update: 2020-07-07 10:10
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
    给定一个字符串，逐个翻转字符串中的每个单词。
    解法：
    一. 使用语言特性
    二. 使用队列
    """
    def reverseWords(self, s):
        """
        整体流程：
        0. 进行特判
        1. 生成暂存列表以及队列等中间变量
        2. 遍历s
        3. 如果是空格且暂存队列为空则跳过
        4. 如果不是空格则加到暂存队列
        5. 如果是空格且暂存队列不为空则生成字母放到队列中
        6. 把队列反序连接
        """
        # 0. 进行特判
        if s is None or len(s) == 0:
            return s

        # 1. 生成暂存列表以及队列等中间变量
        tmp_list, queue = [], []

        # 2. 遍历s
        s += ' '
        for str in s:
            # 3. 如果是空格且暂存队列为空则跳过
            if (str == ' ') and (len(tmp_list) == 0):
                continue
            # 5. 如果是空格且暂存队列不为空则生成字母放到队列中
            elif (str == ' ') and (len(tmp_list) != 0):
                tmp_str = ''.join(tmp_list)
                queue.append(tmp_str)
                tmp_list = []
            # 4. 如果不是空格则加到暂存队列
            else:
                tmp_list.append(str)

        # 6. 把队列反序连接
        return ' '.join(reversed(queue))

    def reverseWords_lang(self, s):
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    word = "the sky is blue"
    # word = "  hello world!  "
    print(Solution().reverseWords(word))