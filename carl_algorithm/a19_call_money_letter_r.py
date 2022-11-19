# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a19_call_money_letter_r.py
@Time: 2022-10-08 17:55
@Last_update: 2022-10-08 17:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def call_money_letter(word1, word2):
    """
    赎金信，看word1是否可以用word2来构建
    1. 构建需要用的字符字典
    2. 遍历word2，把相应的字符加入
    3. 遍历word1，如果相应的字符不在，或者字频为0则返回false
    4. 否则相应的字频减一
    """
    # 1. 构建需要用的字符字典
    word_dict = dict()

    # 2. 遍历word2，把相应的字符加入
    for word in word2:
        word_dict[word] = word_dict.get(word, 0) + 1

    # 3. 遍历word1，如果相应的字符不在，或者字频为0则返回false
    for word in word1:
        if word_dict.get(word, 0) == 0:
            return False

        # 4. 否则相应的字频减一
        word_dict[word] -= 1

    return True


if __name__ == '__main__':
    word1 = 'aa'
    word2 = 'aab'
    print(call_money_letter(word1, word2))
