# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a23_replace_space.py
@Time: 2022-04-15 19:22
@Last_update: 2022-04-15 19:22
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def replace_replace(word):
    """
    替换word中的空格为%20
    """
    return ''.join([sub if sub != ' ' else '%20' for sub in word])


if __name__ == '__main__':
    word = 'We are happy'
    print(replace_replace(word))
