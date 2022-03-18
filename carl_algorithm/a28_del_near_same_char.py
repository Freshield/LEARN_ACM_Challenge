# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a28_del_near_same_char.py
@Time: 2022-04-18 16:02
@Last_update: 2022-04-18 16:02
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def del_near_same_char(word):
    """
    删除临近的相同字符
    使用栈的方式进行，如果栈顶和放入的一致则删除
    """
    stack = ['']
    for char in word:
        if char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()

    return ''.join(stack)


if __name__ == '__main__':
    word = "abbaca"
    print(del_near_same_char(word))
