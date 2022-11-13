# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a156_strstr.py
@Time: 2022-11-01 20:35
@Last_update: 2022-11-01 20:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def strStr(haystack, needle):
    """
    对haystack和needle进行比较
    1. 创建指针i，res index
    2. 遍历，条件为i小于haystack的长度
    2. 遍历，条件为haystack[i]不等于needle[0]
    3. 记录res index,遍历needle
    4. 如果haystack[i]和needle[j]相同，则继续
    5. 否则跳出
    """
    # 1. 创建指针i，res index
    if (len(needle) == 0) or (len(haystack) == 0):
        return 0
    if len(needle) > len(haystack):
        return -1
    i, res_index = 0, 0

    # 2. 遍历，条件为i小于haystack的长度
    while i < len(haystack):
        # 2. 遍历，条件为haystack[i]不等于needle[0]
        while haystack[i] != needle[0]:
            i += 1
            if i >= len(haystack):
                return -1
        # 3. 记录res index,遍历needle
        res_index = i
        j = 0
        while (i < len(haystack)) and (j < len(needle)):
            # 4. 如果haystack[i]和needle[j]相同，则继续
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                continue
            else:
                i = res_index + 1
                break

        if j == len(needle):
            return res_index

    return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issipi"
    print(strStr(haystack, needle))
