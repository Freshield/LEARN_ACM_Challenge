#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0043_multiply.py
@Time: 2020-04-22 14:27
@Last_update: 2020-04-22 14:27
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
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
    解法：
    使用竖式乘法，不过不是每次计算都加一次sum，而是按位数记录，
    重点是num1的i位和num2的j为相加只影响结尾的第i,j和i,j+1位
    """
    def multiply(self, num1, num2):
        """
        整体流程：
        1. 生成返回的矩阵
        2. 遍历i,j从后边反向遍历
        3. 存储到res相应的位置
        """
        if (num1 == '0') or (num2 == '0'):
            return '0'
        # 1. 生成返回的矩阵
        res = [0] * (len(num1) + len(num2) + 1)
        # 2. 遍历i,j从后边反向遍历
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i, p1 in enumerate(num1):
            for j, p2 in enumerate(num2):
                mul = (ord(p1)-ord('0')) * (ord(p2)-ord('0'))
                sum = mul + res[i+j]
                res[i+j] = sum % 10
                res[i+j+1] += sum // 10

        return ''.join([str(res[i]) for i in range(len(res)-1, -1, -1)]).lstrip('0')


if __name__ == '__main__':
    num1 = "2"
    num2 = "3"
    # num1 = "123"
    # num2 = "456"
    print(Solution().multiply(num1, num2))