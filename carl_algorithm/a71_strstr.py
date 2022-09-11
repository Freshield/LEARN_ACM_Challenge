# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a71_strstr.py
@Time: 2022-10-09 10:47
@Last_update: 2022-10-09 10:47
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def get_next(needle):
    """
    获取next数组
    1. 初始化，生成j，next数组并遍历i
    2. 当i，j的值不同的时候，j要重复回到到next的j-1的数值位置，直到相等或者j为0
    3. 当i，j的值相同的时候，j加一，同时i对应的值为j的值
    """
    # 1. 初始化，生成j，next数组并遍历i
    next_list, j = [0] * len(needle), 0
    next_list[0] = j
    for i in range(1, len(needle)):
        # 2. 当i，j的值不同的时候，j要重复回到到next的j-1的数值位置，直到相等或者j为0
        while (j > 0) and (needle[i] != needle[j]):
            j = next_list[j - 1]
        # 3. 当i，j的值相同的时候，j加一，同时i对应的值为j的值
        if needle[i] == needle[j]:
            j += 1
        next_list[i] = j

    return next_list


def get_next_easy(needle):
    """
    使用双指针法
    1. 初始化next数组，left，right
    2. 遍历needle的区间
    3. 获取此区间前后缀最长长度
    """
    # 1. 初始化next数组，left，right
    next_list = [0] * len(needle)
    # 2. 遍历needle的区间
    for i in range(len(needle)):
        # 3. 获取此区间前后缀最长长度
        left, right, count = 0, i, 0
        # 奇数时共同的部分不算
        while left < right:
            if needle[left] != needle[right]:
                break
            next_list[i] += 1
            left += 1
            right -= 1

    return next_list


def strstr(haystack, needle):
    """
    获取匹配的最长子串位置
    1. 去除needle为空的情况
    2. 获取next数组，生成needle指针j
    3. 遍历haystack数组，生成haystack指针i
    4. 如果i，j指代的值不相等，则持续回退j到next[j-1]的位置，直到相等或者j为0
    5. 如果i，j指代的值相等，j加一
    6. 如果j等于needle的长度，则返回needle的开头
    """
    # 1. 去除needle为空的情况
    if needle == '':
        return 0
    # 2. 获取next数组，生成needle指针j
    next_list, j = get_next(needle), 0
    # 3. 遍历haystack数组，生成haystack指针i
    for i in range(len(haystack)):
        # 4. 如果i，j指代的值不相等，则持续回退j到next[j-1]的位置，直到相等或者j为0
        while (j > 0) and (haystack[i] != needle[j]):
            j = next_list[j - 1]
        # 5. 如果i，j指代的值相等，j加一
        if haystack[i] == needle[j]:
            j += 1
        # 6. 如果j等于needle的长度，则返回needle的开头
        if j == len(needle):
            return i - len(needle) + 1

    return -1


if __name__ == '__main__':
    haystack = "aabaabaaf"
    needle = "aabaaf"
    haystack = "sadbutsad"
    needle = "sad"
    print(strstr(haystack, needle))
