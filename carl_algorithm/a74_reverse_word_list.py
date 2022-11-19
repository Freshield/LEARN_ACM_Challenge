# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a74_reverse_word_list.py
@Time: 2022-10-09 14:10
@Last_update: 2022-10-09 14:10
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def reverse_word_list(word_list):
    """
    翻转字符串
    1. 创建需要的left，right指针
    2. 遍历，条件为left<right
    3. 交换左右指针的值
    4. 更新left，right
    """
    # 1. 创建需要的left，right指针
    left, right = 0, len(word_list) - 1
    #2. 遍历，条件为left<right
    while left < right:
        # 3. 交换左右指针的值
        word_list[left], word_list[right] = word_list[right], word_list[left]
        # 4. 更新left，right
        left += 1
        right -= 1

    return word_list


if __name__ == '__main__':
    word_list = list('hello')
    print(reverse_word_list(word_list))
