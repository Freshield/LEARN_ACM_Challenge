#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a20_value_compute.py
@Time: 2020-04-26 10:43
@Last_update: 2020-04-26 10:43
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

op_dict = {
    '+': lambda x,y: x+y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
    '-': lambda x,y: x-y
}


def calculate(begin, end, input_str):
    """
    整体流程：
    1. 如果字符为-则放入负数
    2. 如果为数字值放入数字
    3. 如果为操作符则放入操作符
    4. 遍历得到结果
    """
    num_list = []
    op_list = []
    flag = 1
    # 1. 如果字符为-则放入负数
    index = begin
    while index < (end + 1):
        if input_str[index] == '-':
            if '0'<=input_str[index-1]<='9':
                op_list.append('-')
                index += 1
            else:
                flag = -1
                index += 1
        elif '0'<=input_str[index]<='9':
            if (index != 0) and ('0'<=input_str[index-1]<='9'):
                num_list[-1] = num_list[-1] * 10 + int(input_str[index])
            else:
                num_list.append(flag * int(input_str[index]))
                flag = 1
            index += 1
        else:
            op_list.append(input_str[index])
            index += 1

    # 处理乘法
    index = 0
    while True:
        if index == len(op_list):
            break

        if op_list[index] not in ['*', '/']:
            index += 1
            continue

        num_list[index] = op_dict[op_list[index]](num_list[index], num_list[index+1])
        num_list.pop(index+1)
        op_list.pop(index)

    for i in range(len(op_list)):
        num_list[0] = op_dict[op_list[i]](num_list[0], num_list[i+1])

    return num_list[0]


def value_compute(input_str):
    """
    功能：四则运算
    输入：strExpression：字符串格式的算术表达式，如: "3+2*{1+2*[-4/(8-6)+7]}"
    返回：算术表达式的计算结果
    约束：
    pucExpression字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。
    pucExpression算术表达式的有效性由调用者保证;
    整体流程：
    1. 替换所有特殊字符为()
    2. 使用栈找到左右括号的位置，然后计算括号内的值并替换字符串
    3. 计算最后所有位置
    """
    # 1. 替换所有特殊字符为()
    input_str = input_str.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')')

    # 2. 使用栈找到左右括号的位置，然后计算括号内的值并替换字符串
    index = 0
    begin_index = -1
    while True:
        if index == len(input_str):
            break

        if input_str[index] not in ['(', ')']:
            index += 1
            continue
        elif input_str[index] == '(':
            begin_index = index+1
            index += 1
        elif input_str[index] == ')':
            rst_val = calculate(begin_index, index-1, input_str)
            input_str = input_str[:begin_index-1] + str(int(rst_val)) + input_str[index+1:]
            index = 0
            begin_index = -1

    rst_val = calculate(0, len(input_str)-1, input_str)

    return rst_val


if __name__ == '__main__':
    input_str = '3+2*{1+2*[-4/(8-6)+7]}'
    # print(calculate(0, 7, '3+2*-4-7'))
    print(value_compute(input_str))