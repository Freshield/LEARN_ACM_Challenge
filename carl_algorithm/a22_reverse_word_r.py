# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a22_reverse_word_r.py
@Time: 2022-10-08 21:39
@Last_update: 2022-10-08 21:39
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def reverse_word(word_list):
    """
    翻转字符串，使用双指针
    1. 创建left，right指针
    2. 遍历left，right，条件为left<right
    3. 对left，right所指代的字符进行翻转
    4. 更新left，right
    """
    # 1. 创建left，right指针
    left, right = 0, len(word_list)-1

    # 2. 遍历left，right，条件为left<right
    while left < right:
        # 3. 对left，right所指代的字符进行翻转
        word_list[left], word_list[right] = word_list[right], word_list[left]
        # 4. 更新left，right
        left += 1
        right -= 1

    return word_list


if __name__ == '__main__':
    word_list = [word for word in 'hello']
    print(reverse_word(word_list))
