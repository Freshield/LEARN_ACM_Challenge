# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a22_reverse_word.py
@Time: 2022-04-15 19:02
@Last_update: 2022-04-15 19:02
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def reverse_word(word):
    """
    反转字符
    使用双指针方法来进行字符的翻转
    1. 建立左右指针
    2. 遍历左右指针直到左指针大于右指针
    3. 翻转相应的字符
    """
    # 1. 建立左右指针
    left_index, right_index = 0, len(word) - 1
    # 2. 遍历左右指针直到左指针大于右指针
    while left_index <= right_index:
        # 3. 翻转相应的字符
        word[left_index], word[right_index] = word[right_index], word[left_index]
        left_index += 1
        right_index -= 1


if __name__ == '__main__':
    word = list('helloo')
    reverse_word(word)
    print(word)

