# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0013_romanToInt.py
@Time: 2020-06-08 11:09
@Last_update: 2020-06-08 11:09
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
    罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
    """
    def __init__(self):
        self.roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.double_roman_dict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

    def romanToInt(self, s):
        rst_val = 0
        i = 0

        if len(s) >= 1:
            while True:
                if i > (len(s) - 1):
                    break
                elif i == (len(s) - 1):
                    rst_val += self.roman_dict[s[i]]
                    break
                    

                if f'{s[i]}{s[i + 1]}' in self.double_roman_dict:
                    rst_val += self.double_roman_dict[f'{s[i]}{s[i + 1]}']
                    i += 2
                else:
                    rst_val += self.roman_dict[s[i]]
                    i += 1
        
        return rst_val


if __name__ == '__main__':
    print(Solution().romanToInt('III'))