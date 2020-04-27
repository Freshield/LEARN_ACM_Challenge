#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a26_unique_str.py
@Time: 2020-04-26 15:19
@Last_update: 2020-04-26 15:19
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
    输入一个字符串，求出该字符串包含的字符集合
    每组数据输入一个字符串，字符串最大长度为100，且只包含字母，不可能为空串，区分大小写。
    每组数据一行，按字符串原有的字符顺序，输出字符集合，即重复出现并靠后的字母不输出。
    """
    def unique_str(self, input_str):
        """
        整体流程：
        1. 生成字符字典
        2. 遍历字符串，看是否在字典
        3. 放到返回字符串中
        """
        # 1. 生成字符字典
        str_dict = dict()
        rst_str = ''

        # 2. 遍历字符串，看是否在字典
        for word in input_str:
            if word not in str_dict:
                str_dict[word] = 1
                # 3. 放到返回字符串中
                rst_str += word

        return rst_str


def input_to_str():
    while True:
        try:
            input_str = input_str()
            rst_str = Solution().unique_str(input_str)
            print(rst_str)
        except Exception as e:
            break


if __name__ == '__main__':
    input_str = 'abcqweracb'
    print(Solution().unique_str(input_str))