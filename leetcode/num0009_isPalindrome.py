# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0009_isPalindrome.py
@Time: 2020-04-19 21:49
@Last_update: 2020-04-19 21:49
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import math


class Solution:
    """
    判断一个整数是否是回文数。
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    """
    def isPalindrome(self, x):
        """
        直接用数学的方法计算
        解法：
        通过log可以得到当前的数字的位数，然后遍历数字
        注意：这里只需要遍历一般的次数即可
        然后构建一个x的相反的数字，不断的把x的数移动过来，
        最后进行判断即可
        整体流程：
        1. 通过log得到位数
        2. 遍历x
        3. 得到reverse_x
        4. 进行比较
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False

        # 1. 通过log得到位数
        x_nums = int(math.log(x, 10))

        # 2. 遍历x
        resverse_x = 0
        for i in range(x_nums//2 + 1):
            last_num = x % 10
            resverse_x = resverse_x * 10 + last_num
            x = x // 10

        # 4. 进行比较
        if (resverse_x == x) or (resverse_x//10 == x):
            return True
        else:
            return False

    def isPalindrome_str(self, x):
        """
        使用字符来看是否为回文
        1. 如果开头为-则返回False
        2. 根据数字的位数来调用判断回文的函数
        """
        test_str = str(x)

        # 1. 如果开头为-则返回False
        if test_str[0] == '-':
            return False

        # 2. 根据数字的位数来调用判断回文的函数
        if len(test_str) % 2 == 0:
            return self.is_palindrome(test_str, len(test_str)//2 - 1, len(test_str)//2)
        else:
            return self.is_palindrome(test_str, len(test_str)//2, len(test_str)//2)

    def is_palindrome(self, test_str, left, right):
        """
        左右依次判断是否相等来判断回文
        整体流程：
        1. 结束条件：left < 0 则返回True
        2. 结束条件：如果left != right的值，则返回False
        3. 移动left，right
        """
        while True:
            # 1. 结束条件：left < 0 则返回True
            if left < 0:
                return True
            # 2. 结束条件：如果left != right的值，则返回False
            elif test_str[left] != test_str[right]:
                return False
            # 3. 移动left，right
            else:
                left -= 1
                right += 1


if __name__ == '__main__':
    # test_num = 121
    # test_num = -121
    # test_num = 10
    test_num = 21120
    print(Solution().isPalindrome(test_num))