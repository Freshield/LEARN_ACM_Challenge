#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0050_myPow.py
@Time: 2020-04-21 14:17
@Last_update: 2020-04-21 14:17
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
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
    解法：
    进行递归，并且只循环n//2次因为
    2**10 = 4 ** 5 = 16 ** 2 * 4
    如果n为偶数则为tmp = tmp**2, n//=2, 如果n为奇数，tmp = tmp**2, n//2再乘tmp
    """
    def pow_iter(self, x, n):
        """
        递归计算x**n
        1. 判别结束情况
        2. 判别n的情况
        """
        # 1. 判别结束情况
        if n == 1:
            return x

        # 2. 判别n的情况
        if n % 2 == 0:
            return self.pow_iter(x*x, n//2)
        else:
            return x * self.pow_iter(x*x, n//2)

    def myPow(self, x, n):
        """
        整体流程：
        1. 处理极值
        2. 初始化相关变量
        3. 调用pow_iter
        4. 得到最终的结果
        """
        # 1. 处理极值
        if x in (0, 1):
            return x
        if n == 0:
            return 1

        # 2. 初始化相关变量
        x = x if n > 0 else 1/x
        n = abs(n)

        # 3. 调用pow_iter
        rst = self.pow_iter(x, n)

        # 4. 得到最终的结果
        return rst


if __name__ == '__main__':
    # x = 2.00000
    # n = 10
    # x = 2.10000
    # n = 3
    # x = 2.00000
    # n = -2
    x = 2
    n = 4
    x = -13.62608
    n = 3
    print(x < 0 and n % 2 != 0)
    print((x < 0) and (n % 2 != 0))
    print(Solution().myPow(x, n))