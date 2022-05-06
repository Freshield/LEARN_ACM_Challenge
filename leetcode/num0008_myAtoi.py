# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0008_myAtoi.py
@Time: 2020-04-19 19:32
@Last_update: 2020-04-19 19:32
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
    请你来实现一个 atoi 函数，使其能将字符串转换成整数。
    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
    如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
    假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
    该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
    注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
    在任何情况下，若函数不能进行有效的转换时，请返回 0 。
    提示：
    本题中的空白字符只包括空格字符 ' ' 。
    假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
    如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
    """
    def myAtoi(self, test_str: str):
        """
        整体流程：
        1. 先生成需要的变量
        2. 去除空字符
        3. 判断第一个字符是否合法
        4. 判断是否为flag
        5. 遍历数字，放到列表中
        6. 结束条件：如果当前字符不是数字则结束
        7. 遍历生成数字
        8, 看是否越界
        """
        if len(test_str) == 0:
            return 0

        # 1. 先生成需要的变量
        flag = 1
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        num_list = [str(i) for i in range(10)]
        rst_list = []
        rst_num = 0.

        # 2. 去除空字符
        begin = 0
        for i in range(len(test_str)):
            if test_str[i] == ' ':
                begin = i+1
                continue
            else:
                break

        if begin >= len(test_str):
            return 0

        # 3. 判断第一个字符是否合法
        if test_str[begin] not in (['-', '+'] + num_list):
            return 0

        # 4. 判断是否为flag
        if test_str[begin] == '-':
            flag = -1
            begin += 1
        elif test_str[begin] == '+':
            begin += 1

        if begin >= len(test_str):
            return 0

        # 5. 遍历数字，放到列表中
        for i in range(begin, len(test_str)):
            # 6. 结束条件：如果当前字符不是数字则结束
            if test_str[i] not in num_list:
                break
            # 5. 遍历数字，放到列表中
            rst_list.append(int(test_str[i]))

        # 7. 遍历生成数字
        times = 1
        for i in range(len(rst_list)-1, -1, -1):
            rst_num += rst_list[i] * times
            times *= 10
        rst_num *= flag

        # 8, 看是否越界
        if rst_num > INT_MAX:
            rst_num = INT_MAX
        elif rst_num < INT_MIN:
            rst_num = INT_MIN

        return int(rst_num)


if __name__ == '__main__':
    test_str = '42'
    # test_str = '   -42'
    # test_str = '4193 with words'
    # test_str = 'words and 987'
    # test_str = '-91283472332'
    print(Solution().myAtoi(test_str))
