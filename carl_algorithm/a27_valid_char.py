# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a27_valid_char.py
@Time: 2022-04-17 19:45
@Last_update: 2022-04-17 19:45
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def valid_char(word):
    """
    看字符中的符号是否对应
    使用栈，看出来的是否配对
    """
    char_dict = {'(': ')', '[': ']', '{': '}', '': ''}
    char_stack = []
    for char in word:
        # 如果是左边的则直接入栈
        if char in char_dict.keys():
            char_stack.append(char)
        # 否则看是否配对
        else:
            last_char = char_stack.pop() if len(char_stack) != 0 else ''
            # 如果不匹配则返回False
            if char != char_dict[last_char]:
                return False

    if len(char_stack) != 0:
        return False

    return True


if __name__ == '__main__':
    word = "()]"
    print(valid_char(word))
