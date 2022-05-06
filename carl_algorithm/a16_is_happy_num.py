# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a16_is_happy_num.py
@Time: 2022-04-14 14:41
@Last_update: 2022-04-14 14:41
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def is_happy_num(num):
    """
    判断是否为快乐数
    1. 建立sum字典和sum数
    2. 开始循环直到sum为1或者sum在字典中
    3. 把num变成str
    4. 遍历num重新计算sum
    5. 如果sum在字典中则返回False
    """
    # 1. 建立sum字典和sum数
    sum_dict, sum_value = dict(), 0
    # 2. 开始循环直到sum为1或者sum在字典中
    while not (sum_value == 1):
        # 3. 把num变成str
        num = str(num)
        # 4. 遍历num重新计算sum
        sum_value = 0
        for sub_str in num:
            sum_value += int(sub_str) ** 2

        if sum_value in sum_dict:
            return False
        num = sum_value
        sum_dict[sum_value] = True

    return True


if __name__ == '__main__':
    num = 19
    print(is_happy_num(num))
