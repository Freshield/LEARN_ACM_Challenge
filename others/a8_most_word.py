#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a8_most_word.py
@Time: 2020-04-24 12:32
@Last_update: 2020-04-24 12:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def most_word(input_str, sensitive=False):
    """
    给定一个长度不限的字符串，请找出该字符串中出现次数最多的那个字符
    整体流程：
    1. 根据sensitive判断是否要转换字符
    2. 分解字符串并排序
    3. 遍历和最大值比较
    4. 返回最大值
    """
    # 1. 根据sensitive判断是否要转换字符
    if not sensitive:
        input_str = input_str.lower()
    # 2. 分解字符串并排序
    str_list = list(input_str)
    str_list.sort()
    max_val = (-1, -1)
    tmp_val = None
    # 3. 遍历和最大值比较
    for str in str_list:
        if tmp_val is None:
            tmp_val = (str, 1)
            continue

        if str == tmp_val[0]:
            tmp_val = (str, tmp_val[1]+1)
        else:
            max_val = tmp_val if tmp_val[1] > max_val[1] else max_val
            tmp_val = (str, 1)

    # 4. 返回最大值
    return max_val


if __name__ == '__main__':
    input_str = 'abcdABCdE'
    sensitive = True
    print(most_word(input_str, sensitive))