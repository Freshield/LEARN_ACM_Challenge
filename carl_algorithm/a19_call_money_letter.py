# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a19_call_money_letter.py
@Time: 2022-04-14 17:11
@Last_update: 2022-04-14 17:11
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
    赎金信，看word1可不可以完全有word2的字符来组成
    1. 建立word字典
    2. 遍历word2生成word字典
    3. 遍历word1
    4. 看当前字符是否在字典中且值不为零
    5. 否则的话把相应的值减一
    """
    # 1. 建立word字典
    word_dict = dict()
    # 2. 遍历word2生成word字典
    for word in word2:
        word_dict[word] = word_dict.get(word, 0) + 1

    # 3. 遍历word1
    for word in word1:
        # 4. 看当前字符是否在字典中且值不为零
        if (word not in word_dict) or (word_dict[word] == 0):
            return False

        # 5. 否则的话把相应的值减一
        word_dict[word] -= 1

    return True


if __name__ == '__main__':
    word1 = 'aa'
    word2 = 'aab'
    print(call_money_letter(word1, word2))
