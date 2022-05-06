# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0415_addStrings.py
@Time: 2020-07-21 10:36
@Last_update: 2020-07-21 10:36
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
    给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
    解法：
    正常的加法流程
    """
    def addStrings(self, num1, num2):
        """
        整体流程：
        1. 进行特判
        2. 生成指针等中间变量
        3. 遍历指针，结束条件为都指针都小于0
        4. 得到当前的字符值
        5. 进行加法
        6. 更新carry和结果
        7. 返回最终结果，注意carry的状态
        """
        # 1. 进行特判
        if (len(num1) == 0) or (len(num2) == 0):
            return num1 if len(num2) == 0 else num2

        # 2. 生成指针等中间变量
        point1 = len(num1) - 1
        point2 = len(num2) - 1
        carry = 0
        rst_str = ''

        # 3. 遍历指针，结束条件为都指针都小于0
        while (point1 >= 0) or (point2 >= 0):
            # 4. 得到当前的字符值
            value1 = ord(num1[point1]) - ord('0') if point1 >= 0 else 0
            value2 = ord(num2[point2]) - ord('0') if point2 >= 0 else 0

            # 5. 进行加法
            sum = value1 + value2 + carry

            # 6. 更新carry和结果
            carry, rst_value = divmod(sum, 10)
            rst_str += str(rst_value)

            point1 -= 1
            point2 -= 1

        # 7. 返回最终结果，注意carry的状态
        if carry != 0:
            rst_str = rst_str + str(carry)

        return rst_str[::-1]


if __name__ == '__main__':
    num1 = '123'
    num2 = '123456'
    num1 = '1'
    num2 = '9'
    print(Solution().addStrings(num1, num2))