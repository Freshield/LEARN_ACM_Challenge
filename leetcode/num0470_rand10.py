# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0470_rand10.py
@Time: 2020-07-15 10:42
@Last_update: 2020-07-15 10:42
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import random


# The rand7() API is already defined for you.
def rand7():
    return random.randint(1, 7)
# @return a random integer in the range 1 to 7


class Solution:
    """
    已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
    不要使用系统的 Math.random() 方法。
    解法：
    使用(rand7-1)*7+rand7的方法得到1-49
    对于1-40直接用对10取余+1
    对于41-49的数，使用(big49-40-1)*7+rand7的方法得到1-63
    对于1-60直接使用对10取余+1
    对于61-63的数，使用(big63-60-1)*7+rand7的方法得到1-21
    对于1-20直接使用对10取余+1
    对于21则放弃重新选择
    """
    def rand10(self):
        """
        整体流程：
        1. 得到1-40第一层
        2. 得到1-63第二层
        3. 得到1-21第三层
        """
        while True:
            # 1. 得到1-40第一层
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return 1 + (num % 10)

            # 2. 得到1-63第二层
            num = (num - 40 - 1) * 7 + rand7()
            if num <= 60:
                return 1 + (num % 10)

            # 3. 得到1-21第三层
            num = (num - 60 - 1) * 7 + rand7()
            if num <= 20:
                return 1 + (num % 10)


if __name__ == '__main__':
    print(Solution().rand10())