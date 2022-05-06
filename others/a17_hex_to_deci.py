# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a17_hex_to_deci.py
@Time: 2020-04-25 22:14
@Last_update: 2020-04-25 22:14
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution(object):
    """
    写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）
    输入描述:
    输入一个十六进制的数值字符串。
    输出描述:
    输出该数值的十进制字符串。
    """
    def hex_to_deci(self, hex_str):
        """
        整体流程：
        1. 构建对应字典
        2. 解析字符串
        3. 遍历叠加
        4. 返回结果
        """
        # 1. 构建对应字典
        hex_dict = {str(key): key for key in range(10)}
        hex_dict.update({chr(ord('A')+i): i+10 for i in range(6)})

        # 2. 解析字符串
        hex_str = hex_str.split('x')[-1]

        # 3. 遍历叠加
        sum_val = 0
        for num, index in enumerate(range(len(hex_str))):
            sum_val = sum_val * 16 + hex_dict[hex_str[index]]

        # 4. 返回结果
        return sum_val


def input_to_str():
    while True:
        try:
            input_str = input()
            print(Solution().hex_to_deci(input_str))
        except Exception as e:
            break


if __name__ == '__main__':
    a = '0x76E'
    print(Solution().hex_to_deci(a))
