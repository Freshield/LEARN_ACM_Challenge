#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0005_longestPalindrome.py
@Time: 2020-04-17 14:18
@Last_update: 2020-04-17 14:18
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def is_valid_palindrome(test_str, begin, end):
    """查看当前区间的字符串是否为回文字符串"""
    while True:
        # 结束条件
        if end <= begin:
            break

        # 如果不相等则返回False
        if test_str[begin] != test_str[end]:
            return False
        else:
            begin += 1
            end -= 1

    return True


def longestPalindrome_force(test_str):
    """
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    解法：
    此为暴力解法，从头开始遍历字母，找到之后所有的回文子串，然后看哪个大
    整体流程：
    1. 如果字符串小于等于2直接返回
    2. 遍历s的所有字符
    3. 从s+1开始找s->s+n的区间有没有回文字串
    4. 找的时候只找比当前找到的大的回文字串
    """
    # 1. 如果字符串小于等于2直接返回
    str_size = len(test_str)
    if str_size <= 2:
        return test_str

    # 当前找到的最大回文长度
    max_len = 1
    rst_str = None
    # 2. 遍历s的所有字符
    for str_index in range(str_size-1):
        # 3. 从s+1开始找s->s+n的区间有没有回文字串
        for end_index in range(str_index+1, str_size):
            # 4. 找的时候只找比当前找到的大的回文字串
            if ((end_index - str_index + 1) > max_len) and is_valid_palindrome(test_str, str_index, end_index):
                rst_str = test_str[str_index: end_index+1]
                max_len = len(rst_str)

    return rst_str


if __name__ == '__main__':
    test_str0 = 'babadaaaaaaaaaaaaaaaaaaaa'
    test_str1 = 'cbbdaaaaaaaaaaaaaaaaaaaaa'

    print(longestPalindrome_force(test_str0))
    print(longestPalindrome_force(test_str1))