# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a14_disorder_word_r.py
@Time: 2022-10-08 16:00
@Last_update: 2022-10-08 16:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def disorder_word(s, t):
    """
    判断两个字符串是否为异位词
    1. 生成所需的字典
    2. 遍历s，把相应的字母的频率加一
    3. 遍历t，把相应的字母的频率减一
    4. 看字典的所有value是否为0
    """
    # 1. 生成所需的字典
    freq_dict = dict()

    # 2. 遍历s，把相应的字母的频率加一
    for word in s:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    # 3. 遍历t，把相应的字母的频率减一
    for word in t:
        freq_dict[word] = freq_dict.get(word, 0) - 1

    # 4. 看字典的所有value是否为0
    for word, freq in freq_dict.items():
        if freq != 0:
            return False

    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(disorder_word(s, t))
