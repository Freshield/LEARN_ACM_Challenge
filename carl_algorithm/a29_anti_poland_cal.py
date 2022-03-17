# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a29_anti_poland_cal.py
@Time: 2022-04-18 16:11
@Last_update: 2022-04-18 16:11
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def anti_poland_cal(_cal_list):
    """
    计算给出的逆波兰计算式
    使用栈，如果遇到计算符号则弹出进行计算
    """
    stack = []
    for word in _cal_list:
        if word in ['+', '-', '*', '/']:
            value2 = stack.pop()
            value1 = stack.pop()
            word = eval(f'{value1} {word} {value2}')

        stack.append(int(word))

    return stack.pop()


if __name__ == '__main__':
    cal_list = ["2", "1", "+", "3", "*"]
    print(anti_poland_cal(cal_list))
