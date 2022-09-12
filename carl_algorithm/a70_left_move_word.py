# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a70_left_move_word.py
@Time: 2022-10-09 09:38
@Last_update: 2022-10-09 09:38
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def left_move_word(s, k):
    """
    左旋字符，使用先倒序局部，再倒序整体
    1. 对左边进行倒序
    2. 对右边进行倒序
    3. 整体倒序
    """
    # 1. 对左边进行倒序
    left = s[:k][::-1]
    # 2. 对右边进行倒序
    right = s[k:][::-1]
    # 3. 整体倒序
    return (left + right)[::-1]


if __name__ == '__main__':
    s = 'helloworld'
    k = 5
    print(left_move_word(s, k))
