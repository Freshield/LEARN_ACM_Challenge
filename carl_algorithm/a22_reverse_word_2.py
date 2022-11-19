# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a22_reverse_word_2.py
@Time: 2022-10-08 21:51
@Last_update: 2022-10-08 21:51
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def reverse_word_2(s, k):
    """
    翻转字符串每2k位，翻转前k个
    1. 生成起始的指针，index
    2. 遍历，条件为index<len(s)
    3. 让前k个翻转，k之后的不变
    4. 对index进行更新
    """
    # 1. 生成起始的指针，index
    index = 0
    # 2. 遍历，条件为index<len(s)
    while index < len(s):
        # 3. 让前k个翻转，k之后的不变
        s = s[0: index] + s[index: index+k][::-1] + s[index+k:]
        # 4. 对index进行更新
        index += 2 * k

    return s


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(reverse_word_2(s, k))
