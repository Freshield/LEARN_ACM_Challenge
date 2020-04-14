#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_fib.py
@Time: 2020-04-14 10:48
@Last_update: 2020-04-14 10:48
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def fib(n, calced_list=None):
    """
    斐波那切数列
    解法：
    a0=0, a1=1, an=an-1 + an-2
    整体流程：
    1. 结束条件为n小于等于1
    2. 如果要计算的值在calced_list则直接返回
    3. 否则递归
    """
    calced_list = [-1] * (n+1) if calced_list is None else calced_list
    # 1. 结束条件为n小于等于1
    if n <= 1:
        return n
    elif calced_list[n] != -1:
        return calced_list[n]
    else:
        return fib(n-1, calced_list) + fib(n-2, calced_list)


if __name__ == '__main__':
    print(fib())