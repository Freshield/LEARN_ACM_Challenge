#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0005_longestPalindrome.py
@Time: 2020-04-17 14:18
@Last_update: 2020-04-17 14:18
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np


def is_valid_palindrome(test_str, begin, end):
    """查看当前区间的字符串是否为回文字符串"""
    while True:
        # 结束条件
        if end <= begin:
            break

        # 如果不相等则返回False
        if test_str[begin] != test_str[end]:
            return False
        else:
            begin += 1
            end -= 1

    return True


def longestPalindrome_force(test_str):
    """
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    解法：
    此为暴力解法，从头开始遍历字母，找到之后所有的回文子串，然后看哪个大
    整体流程：
    1. 如果字符串小于等于2直接返回
    2. 遍历s的所有字符
    3. 从s+1开始找s->s+n的区间有没有回文字串
    4. 找的时候只找比当前找到的大的回文字串
    """
    # 1. 如果字符串小于等于2直接返回
    str_size = len(test_str)
    if str_size <= 2:
        return test_str

    # 当前找到的最大回文长度
    max_len = 1
    rst_str = None
    # 2. 遍历s的所有字符
    for str_index in range(str_size-1):
        # 3. 从s+1开始找s->s+n的区间有没有回文字串
        for end_index in range(str_index+1, str_size):
            # 4. 找的时候只找比当前找到的大的回文字串
            if ((end_index - str_index + 1) > max_len) and is_valid_palindrome(test_str, str_index, end_index):
                rst_str = test_str[str_index: end_index+1]
                max_len = len(rst_str)

    return rst_str


def longestPalindrome_dp(test_str):
    """
    使用动态规划的方法来进行回文子串选择
    解法：
    用dp方法主要在于最内部的遍历时如何对字串是回文的判定进行优化
    1. dp表示什么：dp[i, j]表示test_str[i:j]是否有回文字串
    2. dp关联条件：
        i. 如果si != sj则回文失败
        ii. 如果j - i < 3则为回文，因为一个字符或者两个字符肯定是回文
        iii. 如果si == sj, 则dp[i, j] = dp[i+1, j-1]
    3. dp初始条件：dp[i, i]都为True，因为标识为一个字符
    4. dp如何遍历：设置的dp矩阵为(i,j)矩阵，大小为(N, N)N为字符串长度
        j是依赖于上方的数据，i是依赖于右方的数据，
        所以我们的遍历j需要从小到大，i需要从大到小
    整体流程：
    1. 判别test_str长度是否小于3
    2. 构建dp矩阵以及其他中间变量，初始化dp
    3. 遍历i也就是left
    4. 遍历j也就是right
    5. 根据条件来进行判断
    6. 返回最长回文长度
    """
    # 1. 判别test_str长度是否小于3
    str_size = len(test_str)
    if str_size < 3:
        return test_str

    # 2. 构建dp矩阵以及其他中间变量
    dp = np.ones((str_size, str_size), dtype=np.int8) * -1
    for i in range(str_size):
        dp[i, i] = True
    max_len = 1
    max_left = -1
    max_right = -1

    # 3. 遍历i也就是left
    for left in range(str_size-2, -1, -1):
        # 4. 遍历j也就是right
        for right in range(left+1, str_size):
            # print('left', left)
            # print('right', right)
            # 5. 根据条件来进行判断
            if right - left + 1 < 3:
                # print('s0')
                dp[left, right] = 1
            elif test_str[left] != test_str[right]:
                # print('s1')
                dp[left, right] = 0
            else:
                # print('s2')
                dp[left, right] = dp[left + 1, right - 1]

            if dp[left, right] == 1:
                if (right - left + 1) > max_len:
                    max_len = right - left + 1
                    max_left = left
                    max_right = right

            # print()


    # 6. 返回最长回文长度
    # print(max_left)
    # print(max_right)
    # print(dp)
    return test_str[max_left: max_right+1]


def cal_spread(test_str, center_left, center_right):
    """
    计算center为中心扩散出来的最长回文索引
    中止条件：
        center_left<0, center_right>len(test_str)-1,
        test_str[center_left] != test_str[center_right]
    """
    while True:
        if (center_left < 1) or (center_right > len(test_str) - 2):
            break
        elif test_str[center_left-1] != test_str[center_right+1]:
            break

        center_left -= 1
        center_right += 1

    return center_left, center_right



def longestPalindrome_spread(test_str):
    """
    利用中心扩散的方法来进行
    解法：
    通过遍历位置寻找中心点，然后从中心往两边扩散的方法找最长回文
    1. 如何遍历：中心点有两种，分别是单独的中心点以及相邻的中心点，
        遍历应该从1到N-1
    2. 查找条件：si == sj
    整体流程：
    1. 判断字符串长度是否小于3
    2. 准备相应的中间变量
    3. 遍历center位置
    4. 得到odd，spread的索引，计算长度
    5. 如果center+1和center相等计算even的spread索引，计算长度
    6. 进行比较得到最大序列
    7. 返回最大序列
    """
    # 1. 判断字符串长度是否小于3
    str_size = len(test_str)
    if str_size < 2:
        return test_str

    # 2. 准备相应的中间变量
    max_len = 0
    max_left = -1
    max_right = -1

    # 3. 遍历center位置
    for center in range(str_size):
        # 4. 得到odd，spread的索引，计算长度
        odd_left, odd_right = cal_spread(test_str, center, center)
        odd_len = odd_right - odd_left + 1
        # 5. 如果center+1和center相等计算even的spread索引，计算长度
        even_left = 0
        even_right = -1
        if (center != str_size - 1) and (test_str[center] == test_str[center+1]):
            even_left, even_right = cal_spread(test_str, center, center+1)
        even_len = even_right - even_left + 1

        # 6. 进行比较得到最大序列
        if (odd_len >= even_len) and (odd_len > max_len):
            max_len = odd_len
            max_left = odd_left
            max_right = odd_right
        elif even_len > max_len:
            max_len = even_len
            max_left = even_left
            max_right = even_right

    # 7. 返回最大序列
    return test_str[max_left: max_right+1]



if __name__ == '__main__':
    test_str0 = 'babad'
    test_str1 = 'cbbda'
    test_str2 = 'ac'

    # print(longestPalindrome_force(test_str0))
    # print(longestPalindrome_force(test_str1))
    # print(longestPalindrome_dp(test_str0))
    # print(longestPalindrome_dp(test_str1))
    # print(longestPalindrome_spread(test_str0))
    # print(longestPalindrome_spread(test_str1))
    print(longestPalindrome_spread(test_str2))