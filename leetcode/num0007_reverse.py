# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0007_reverse.py
@Time: 2020-04-20 21:45
@Last_update: 2020-04-20 21:45
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
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
    解法：
    用log得到位数，然后用除数和余数
    """
    INT_MAX = (1 << 31) - 1
    INT_MIN = -(1 << 31)

    def reverse(self, x):
        """
        整体流程：
        1. 得到x的符号
        2. 遍历，继续条件x != 0
        3. 保存余数和除数迭代
        4. 最后乘上符号
        5. 判断是否越界
        """
        # 1. 得到x的符号
        sign = 1 if x > 0 else -1

        x = abs(x)
        reverse_x = 0
        # 2. 遍历，结束条件x != 0
        while x != 0:
            # 3. 保存余数和除数迭代
            last = x % 10
            reverse_x = reverse_x * 10 + last
            x = x // 10

        # 4. 最后乘上符号
        reverse_x *= sign

        # 5. 判断是否越界
        if self.INT_MIN <= reverse_x <= self.INT_MAX:
            return reverse_x
        else:
            return 0


if __name__ == '__main__':
    x = 123
    # x = -123
    # x = 120
    print(Solution().reverse(x))