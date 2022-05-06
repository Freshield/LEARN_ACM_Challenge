#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a30_fractionToDecimal.py
@Time: 2020-04-26 17:56
@Last_update: 2020-04-26 17:56
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
    给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
    如果小数部分为循环小数，则将循环的部分括在括号内。
    解法：
    使用长除法，看余数
    """
    def fractionToDecimal(self, numerator, denominator):
        """
        整体流程：
        1. 生成最终返回的列表
        2. 处理正负flag的问题
        3. 处理小数点前
        4. 遍历小数点部分
        5. 记录余数
        6. 如果出现过则放括号
        7. 如果余数为0,则为正常整除
        """
        # 特殊情况
        if numerator == 0:
            return '0'
        # 1. 生成最终返回的列表
        rst_list = []
        # 2. 处理正负flag的问题
        flag = 1 if numerator*denominator>0 else -1
        if flag == -1:
            rst_list.append('-')
        # 3. 处理小数点前
        numerator, denominator = abs(numerator), abs(denominator)
        left, right = divmod(numerator, denominator)
        rst_list.append(str(left))
        # 7. 如果余数为0,则为正常整除
        if right == 0:
            return ''.join(rst_list)
        rst_list.append('.')
        # 4. 遍历小数点部分
        right_dict = {right: len(rst_list)}
        while True:
            right *= 10
            left, right = divmod(right, denominator)
            rst_list.append(str(left))
            if right == 0:
                return ''.join(rst_list)
            # 6. 如果出现过则放括号
            if right in right_dict.keys():
                rst_list.insert(right_dict[right], '(')
                rst_list.append(')')
                return ''.join(rst_list)
            # 5. 记录余数
            right_dict[right] = len(rst_list)







if __name__ == '__main__':
    numerator = 1
    denominator = 2
    numerator = 2
    denominator = 1
    numerator = 2
    denominator = 3
    print(Solution().fractionToDecimal(numerator, denominator))