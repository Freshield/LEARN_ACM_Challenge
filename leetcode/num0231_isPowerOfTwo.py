# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0231_isPowerOfTwo.py
@Time: 2020-06-08 10:09
@Last_update: 2020-06-08 10:09
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
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
    解法：
    1. 辨别是否二进制只有一个1
    2. 如果是2的幂，则x & (-x) = x
    3. 如果是2的幂，则x & (x - 1) = 0
    """
    def isPowerOfTwo(self, n):
        if n == 0:
            return False

        return n & (-n) == n


    def isPowerOfTwo_bin(self, n):
        if '-' in str(bin(n)):
            return False

        bin_str = str(bin(n)).split('b')[-1]

        if bin_str[0] != '1':
            return False

        for i in range(1, len(bin_str)):
            if bin_str[i] != '0':
                return False

        return True


if __name__ == '__main__':
    print(bin(-16))
    exit()
    print(Solution().isPowerOfTwo(1))