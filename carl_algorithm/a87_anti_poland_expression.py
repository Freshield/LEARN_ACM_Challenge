# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a87_anti_poland_expression.py
@Time: 2022-10-11 11:40
@Last_update: 2022-10-11 11:40
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def anti_poland_expression(express_list):
    """
    逆波兰表达式
    1. 生成所需的栈，和操作符字典
    2. 遍历表达式列表
    3. 如果不是操作符则放到栈里
    4. 如果是操作符则把出栈两个，然后得到结果再放到栈中
    """
    # 1. 生成所需的栈，和操作符字典
    stack = []
    op_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
    }
    # 2. 遍历表达式列表
    for exp_str in express_list:
        exp_str = exp_str.strip()
        # 3. 如果不是操作符则放到栈里
        if exp_str not in op_dict:
            stack.append(int(exp_str))
            continue
        # 4. 如果是操作符则把出栈两个，然后得到结果再放到栈中
        y = stack.pop(-1)
        x = stack.pop(-1)
        res = op_dict[exp_str](x, y)
        stack.append(res)

    return stack.pop(-1)


if __name__ == '__main__':
    express_list = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(anti_poland_expression(express_list))

