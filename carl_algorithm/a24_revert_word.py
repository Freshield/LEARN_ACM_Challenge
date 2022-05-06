# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a24_revert_word.py
@Time: 2022-04-15 19:38
@Last_update: 2022-04-15 19:38
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def revert_word(word):
    """
    反转字符串
    使用双指针
    1. 使用双指针，去除开头和中间多余的空格
    2. 使用双指针来反转字符串
    3. 使用双指针来反转每个字符
    """
    # 1. 使用双指针，去除开头和中间多余的空格
    left_index, right_index = 0, len(word) - 1
    word_list = []
    # 去除开头结尾的空格
    while (left_index <= right_index) and (word[left_index] == ' '):
        left_index += 1
    while (left_index <= right_index) and (word[right_index] == ' '):
        right_index -= 1
    # 去除中间的空格
    for i in range(left_index, right_index + 1):
        # 如果不是空格则放入
        if word[i] != ' ':
            word_list.append(word[i])
        # 如果是空格，但是前一个值不是空格则放入
        elif word_list[-1] != ' ':
            word_list.append(word[i])

    # 2. 使用双指针来反转字符串
    left_index, right_index = 0, len(word_list) - 1
    while left_index <= right_index:
        word_list[left_index], word_list[right_index] = word_list[right_index], word_list[left_index]
        left_index += 1
        right_index -= 1

    # 3. 使用双指针来反转每个字符
    left_index, right_index = 0, 0
    while left_index < len(word_list):
        # 找到空格
        while (right_index != len(word_list)) and (word_list[right_index] != ' '):
            right_index += 1
        next_index = right_index + 1
        right_index -= 1
        # 翻转
        while left_index <= right_index:
            word_list[left_index], word_list[right_index] = word_list[right_index], word_list[left_index]
            left_index += 1
            right_index -= 1

        left_index = right_index = next_index

    return ''.join(word_list)


if __name__ == '__main__':
    word = ' the sky  is blue '
    print(revert_word(word))
