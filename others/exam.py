# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: exam.py
@Time: 2020-04-26 21:34
@Last_update: 2020-04-26 21:34
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution(object):
    """
    统计不同字符的个数
    """
    def statistics_word_num(self, input_str):
        """
        整体流程：
        1. 生成字符串集合set
        2. 遍历字符串放到集合set中
        3. 统计set中的个数
        """
        # 1. 生成字符串集合set
        word_set = set()
        # 2. 遍历字符串放到集合set中
        for i in input_str:
            # 在ascii码内
            if 0<=ord(i)<=127:
                word_set.add(i)
        # 3. 统计set中的个数
        word_count = len(word_set)

        return word_count


def input_to_str():
    while True:
        try:
            input_str = input()
            rst_count = Solution().statistics_word_num(input_str)
            print(rst_count)
        except Exception as e:
            break



if __name__ == '__main__':
    input_str = 'aabbccdd'
    input_str = 'abcd'
    input_str = 'abcdee'
    input_str = '435'
    print(Solution().statistics_word_num(input_str))