#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0166_fractionToDecimal.py
@Time: 2020-04-27 11:07
@Last_update: 2020-04-27 11:07
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
    使用长除法，如果余数循环了则证明为循环小数，循环位为上次出现的地方
    """
    def fractionToDecimal(self, numerator, denominator):
        """
        整体流程：
        1. 处理特殊情况
        2. 生成返回矩阵
        3. 处理正负符号问题
        4. 处理整数部分
        5. 如果有余数则继续比较余数
        6. 生成余数的位置字典并记录当前位置
        7. 遍历获得新的余数
        8. 判断是否已整除，整除则返回
        9. 判断是否重复，如果重复则放括号返回
        10. 更新字典继续遍历
        """
        # 1. 处理特殊情况
        if numerator == 0:
            return '0'
        # 2. 生成返回矩阵
        rst_list = []
        # 3. 处理正负符号问题
        flag = -1 if numerator*denominator<0 else 1
        if flag == -1:
            rst_list.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        # 4. 处理整数部分
        integer, remainder = divmod(numerator, denominator)
        rst_list.append(str(integer))
        # 5. 如果有余数则继续比较余数
        if remainder == 0:
            return ''.join(rst_list)
        # 6. 生成余数的位置字典并记录当前位置
        rst_list.append('.')
        remainder_dict = {remainder: len(rst_list)}
        # 7. 遍历获得新的余数
        while True:
            remainder *= 10
            integer, remainder = divmod(remainder, denominator)
            rst_list.append(str(integer))
            # 8. 判断是否已整除，整除则返回
            if remainder == 0:
                return ''.join(rst_list)
            # 9. 判断是否重复，如果重复则放括号返回
            if remainder in remainder_dict.keys():
                pos = remainder_dict[remainder]
                rst_list.insert(pos, '(')
                rst_list.append(')')
                return ''.join(rst_list)
            # 10. 更新字典继续遍历
            remainder_dict[remainder] = len(rst_list)




if __name__ == '__main__':
    numerator = 1
    denominator = 2
    # numerator = 2
    # denominator = 1
    # numerator = 2
    # denominator = 3

    print(Solution().fractionToDecimal(numerator, denominator))