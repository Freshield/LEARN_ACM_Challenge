# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a12_grayCode.py
@Time: 2020-04-25 18:10
@Last_update: 2020-04-25 18:10
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
    格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
    给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
    解法：
    递推调用，通过镜像的方法生成格雷编码
    """
    def grayCode(self, n):
        """
        整体流程：
        1. 处理极值情况
        2. 生成镜像数组并遍历生成新的数组
        3. 递推调用
        """
        # 1. 处理极值情况
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        # 2. 生成镜像数组并遍历生成新的数组
        num_list = [0, 1]
        # 3. 递推调用
        for i in range(2, n+1):
            tmp_list = []
            adder = 2 ** (i-1)
            for j in range(len(num_list)-1, -1, -1):
                tmp_list.append(num_list[j] + adder)
            num_list += tmp_list

        return num_list


if __name__ == '__main__':
    n = 3
    grad_code_list = Solution().grayCode(n)
    print(grad_code_list)