# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a16_is_happy_num_r.py
@Time: 2022-10-08 16:29
@Last_update: 2022-10-08 16:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def is_happy_num(n):
    """
    判定是否为快乐数
    1. 构建sum set
    2. 无限循环计算sum
    3. 如果num为1，则返回true
    4. 否则看是否在sum set，如果在则返回false
    5. 进行sum set更新
    """
    # 1. 构建sum set
    sum_set = set()

    # 2. 无限循环计算sum
    while True:
        n = sum([int(word)**2 for word in str(n)])
        # 3. 如果num为1，则返回true
        if n == 1:
            return True
        # 4. 否则看是否在sum set，如果在则返回false
        elif n in sum_set:
            return False

        # 5. 进行sum set更新
        sum_set.add(n)


if __name__ == '__main__':
    num = 7
    print(is_happy_num(num))