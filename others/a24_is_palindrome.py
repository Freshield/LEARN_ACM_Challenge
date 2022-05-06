#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a24_is_palindrome.py
@Time: 2020-04-26 14:28
@Last_update: 2020-04-26 14:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def is_palindrome(input_str):
    """
    判断输出字符是否是回文
    整体流程：
    1. 找到中心位置
    2. 使用双指针来判定是否相等
    """
    # 1. 找到中心位置
    if len(input_str) % 2 == 0:
        left = (len(input_str) // 2) - 1
        right = left + 1
    else:
        left = len(input_str) // 2
        right = len(input_str) // 2

    # 2. 使用双指针来判定是否相等
    while True:
        if input_str[left] != input_str[right]:
            return False

        left -= 1
        right += 1

        if (left < 0) or (right == len(input_str)):
            break

    return True


if __name__ == '__main__':
    input_str = '1211'
    print(is_palindrome(input_str))