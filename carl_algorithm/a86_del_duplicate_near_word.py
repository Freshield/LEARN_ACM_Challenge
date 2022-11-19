# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a86_del_duplicate_near_word.py
@Time: 2022-10-10 13:55
@Last_update: 2022-10-10 13:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def del_duplicate_near_word(s):
    """
    删除相邻的同样字符
    1. 创建所需的栈
    2. 遍历字符串
    3. 如果当前字符和最后一个字符相同则消除
    4. 不同则放入
    5. 最终返回所有的字符串
    """
    # 1. 创建所需的栈
    stack = []
    # 2. 遍历字符串
    for word in s:
        # 3. 如果当前字符和最后一个字符相同则消除
        if (len(stack) != 0) and (stack[-1] == word):
            stack.pop(-1)
        # 4. 不同则放入
        else:
            stack.append(word)

    return ''.join(stack)


if __name__ == '__main__':
    s = 'abbaca'
    print(del_duplicate_near_word(s))
