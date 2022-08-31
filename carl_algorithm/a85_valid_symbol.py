# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a85_valid_symbol.py
@Time: 2022-10-10 13:46
@Last_update: 2022-10-10 13:46
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def valid_symbol(symbol_str):
    """
    判断括号是否正确
    1. 构建栈和对应列表
    2. 遍历symbol str如果是左边括号则放入栈右边
    3. 如果是右边括号
    4. 判断栈是否为空，如果为空则返回False
    5. 判断栈pop出来的是否相同，如果不同则返回False
    6. 最后看栈是否为空，不为空则返回Flase
    """
    # 1. 构建栈和对应列表
    stack = []
    symbol_dict = {
        '(': ')', '[': ']', '{': '}'
    }
    # 2. 遍历symbol str如果是左边括号则放入栈右边
    for symbol in symbol_str:
        if symbol in symbol_dict:
            stack.append(symbol_dict[symbol])
            continue
        # 3. 如果是右边括号
        # 4. 判断栈是否为空，如果为空则返回False
        if len(stack) == 0:
            return False
        # 5. 判断栈pop出来的是否相同，如果不同则返回False
        if symbol != stack.pop(-1):
            return False

    # 6. 最后看栈是否为空，不为空则返回Flase
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    symbol_str = '{([{}]))'
    print(valid_symbol(symbol_str))
