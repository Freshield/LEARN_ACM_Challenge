# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0006_convert.py
@Time: 2020-05-18 17:15
@Last_update: 2020-05-18 17:15
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
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
    L   C   I   R
    E T O E S I I G
    E   D   H   N
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
    解法：
    通过rows个列表来维护字符串，通过方向来选择放的位置
    """
    def convert(self, s, numRows):
        """
        整体流程：
        1. 初始化返回列表等变量
        2. 遍历字符
        3. 把字符放到相应的字符串中
        4. 如果到达边界则更改方向
        """
        if numRows == 1:
            return s
        # 1. 初始化返回列表等变量
        rst_list = ['' for _ in range(numRows)]
        direction = 1
        pos = 0

        # 2. 遍历字符
        for word in s:
            # 3. 把字符放到相应的字符串中
            rst_list[pos] += word

            pos += direction

            # 4. 如果到达边界则更改方向
            if (pos == (numRows-1)) or (pos == 0):
                direction *= -1

        return ''.join(rst_list)


if __name__ == '__main__':
    s = "LEETCODEISHIRING"
    numRows = 4
    s = 'AB'
    numRows = 1
    print(Solution().convert(s, numRows))