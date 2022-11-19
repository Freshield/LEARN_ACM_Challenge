# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a72_duplicate_substr.py
@Time: 2022-10-09 11:32
@Last_update: 2022-10-09 11:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def duplicate_substr_easy(s):
    """
    暴力解决，如果有子串则s+s还会有s
    1. 构建s+s
    2. 去除两头的s的字符
    3. 看是否害有s
    """
    # 1. 构建s+s
    new_s = s + s
    # 2. 去除两头的s的字符
    new_s = new_s[1:-1]
    # 3. 看是否害有s
    return s in new_s


def get_next(needle):
    """
    获取前缀表
    1. 初始化，构建next_list，j为0，以及遍历needle的指针i
    2. 当i，j的数值不同时，重复回退j到next[j-1]，直到相等或者j为0
    3. 当i，j的数值相同是，j加一，next[i]的数值为j
    """
    # 1. 初始化，构建next_list，j为0，以及遍历needle的指针i
    next_list, j = [0] * len(needle), 0
    next_list[0] = j
    for i in range(1, len(needle)):
        # 2. 当i，j的数值不同时，重复回退j到next[j-1]，直到相等或者j为0
        while (j > 0) and (needle[i] != needle[j]):
            j = next_list[j - 1]
        # 3. 当i，j的数值相同是，j加一，next[i]的数值为j
        if needle[i] == needle[j]:
            j += 1
        next_list[i] = j

    return next_list


def duplicate_substr(s):
    """
    判断是否由重复子串构成
    1. 构建next列表
    2. 如果next[-1]不为0，且length-next[-1]可以被length整除，则表示由重复子串构成
    """
    # 1. 构建next列表
    next_list = get_next(s)
    # 2. 如果next[-1]不为0，且length-next[-1]可以被length整除，则表示由重复子串构成
    length, last_next = len(next_list), next_list[-1]
    if (next_list[-1] != 0) and (length % (length - last_next) == 0):
        return True
    return False


if __name__ == '__main__':
    s = 'abcabcabc'
    print(duplicate_substr(s))
