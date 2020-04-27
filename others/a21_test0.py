#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a21_test0.py
@Time: 2020-04-26 12:44
@Last_update: 2020-04-26 12:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

def input_to_str():
    while True:
        try:
            test_str = ''
            people, op = list(map(int, input().split(' ')))
            test_str += '%d %d\n' % (people, op)
            val_list = input()
            test_str += val_list + '\n'
            for i in range(op):
                test_str += input() + '\n'
            test(test_str)
        except Exception as e:
            break



def test(input_str):
    """
    输入包括多组测试数据。
    每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
    学生ID编号从1编到N。
    第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
    接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
    当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。
    整体流程：
    1. 切分字符串，得到数据信息列表
    2. 生成数值列表
    3. 遍历操作列表进行操作
    """
    # 1. 切分字符串，得到数据信息列表
    str_list = [sub_str.strip() for sub_str in input_str.split('\n') if sub_str != '']

    # 2. 生成数值列表
    val_list = [int(i) for i in str_list[1].split(' ') if i != '']

    # 3. 遍历操作列表进行操作
    for i in range(2, len(str_list)):
        op_list = [j for j in str_list[i].split(' ') if j != '']
        if op_list[0] == 'U':
            index = int(op_list[1]) - 1
            val = int(op_list[2])
            val_list[index] = val
        elif op_list[0] == 'Q':
            index0 = int(op_list[1])
            index1 = int(op_list[2])
            if index1 < index0:
                index0, index1 = index1, index0
            index0 -= 1
            max_val = val_list[index0]
            for j in range(index0, index1):
                max_val = max_val if val_list[j] < max_val else val_list[j]
            print(max_val)


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        input_str = f.read()
    # input_str = input_to_str()
    test(input_str)