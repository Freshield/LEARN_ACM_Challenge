# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0012_intToRoman.py
@Time: 2020-06-09 11:03
@Last_update: 2020-06-09 11:03
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution:
    """
    给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
    解法：
    使用贪心算法， 直到不能再减为止
    """
    def __init__(self):
        self.roman_list = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

    def intToRoman(self, num):
        """
        整体流程：
        1. 生成返回字符
        2. 遍历roman_list
        3. 生成字符并减少数值
        4. 如果小于当前数值则跳出
        """
        # 1. 生成返回字符
        roman_str = ''

        # 2. 遍历roman_list
        for roman_tuple in self.roman_list:
            # 3. 生成字符并减少数值
            while True:
                # 4. 如果小于当前数值则跳出
                if num < roman_tuple[1]:
                    break

                roman_str += roman_tuple[0]
                num -= roman_tuple[1]

        return roman_str


if __name__ == '__main__':
    num = 3
    num = 58
    num = 1994
    print(Solution().intToRoman(num))