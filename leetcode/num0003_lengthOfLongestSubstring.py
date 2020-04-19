# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0003_lengthOfLongestSubstring.py
@Time: 2020-04-18 16:28
@Last_update: 2020-04-18 16:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def lengthOfLongestSubstring(test_str):
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    解法：
    使用滑动窗口的方法，从最左开始遍历，构建一个当前所有字符的字典，
    如果当前字典没有这个字符，则右边索引向前，字典添加这个字符，
    计算当前长度看是否为最长，如果是则更新
    如果当前字典有这个字符，则右边索引向前，从左边索引位置开始遍历去除，
    直到去除了相同的字符，同时每次去除时要更新字典
    结束条件：右边索引越界，所以直接遍历右边索引即可
    整体流程：
    1. 生成所需的中间变量
    2. 初始化条件
    3. 遍历右边索引
    4. 如果当前字典没有这个字符，更新字典，则判别长度看是否更新
    5. 如果当前字典有这个字符，则从左边索引位置开始遍历去除直到去除了当前的字符
    """
    # 1. 生成所需的中间变量
    max_len = 1
    best_left = 0
    best_right = 0
    str_dict = {test_str[0]: 1}
    # 2. 初始化条件
    left = 0
    # 3. 遍历右边索引
    for right in range(1, len(test_str)):
        right_char = test_str[right]
        # 4. 如果当前字典没有这个字符，更新字典，则判别长度看是否更新
        if str_dict.get(right_char, 0) == 0:
            str_dict[right_char] = 1
            length = right - left + 1
            if length > max_len:
                max_len = length
                best_left = left
                best_right = right
        # 5. 如果当前字典有这个字符，则从左边索引位置开始遍历去除直到去除了当前的字符
        else:
            while True:
                left_char = test_str[left]
                if left_char != right_char:
                    str_dict[left_char] = 0
                    left += 1
                else:
                    left += 1
                    break

    return test_str[best_left: best_right+1]





if __name__ == '__main__':
    test_str0 = 'abcabcbb'
    test_str1 = 'bbbbb'
    test_str2 = 'pwwkew'

    print(lengthOfLongestSubstring(test_str0))
    print(lengthOfLongestSubstring(test_str1))
    print(lengthOfLongestSubstring(test_str2))
