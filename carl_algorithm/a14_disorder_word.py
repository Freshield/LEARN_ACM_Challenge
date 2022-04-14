# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a14_disorder_word.py
@Time: 2022-04-14 14:10
@Last_update: 2022-04-14 14:10
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def disorder_word(word1, word2):
    """
    判断两个此是否为有效字母异位词
    1. 遍历word1，计算词频
    2. 遍历word2，计算词频
    3. 看词频字典是否相同
    """
    # 1. 遍历word1，计算词频
    dict1, dict2 = dict(), dict()
    for word in word1:
        dict1[word] = dict1.get(word, 0) + 1
    # 2. 遍历word2，计算词频
    for word in word2:
        dict2[word] = dict2.get(word, 0) + 1

    return dict1 == dict2


if __name__ == '__main__':
    word1 = 'asdfghj'
    word2 = 'adsfghj'
    print(disorder_word(word1, word2))
