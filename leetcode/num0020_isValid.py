# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0020_isValid.py
@Time: 2020-04-19 22:57
@Last_update: 2020-04-19 22:57
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
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
    """
    def isValid(self, s):
        """
        使用LIFO来进行判断
        整体流程：
        1. 构建对应字典和遍历列表
        2. 遍历s
        3. 如果遇到右边的括号则pop看是否对应
        """
        # 1. 构建对应字典和遍历列表
        right_dict = {']': '[', '}': '{', ')': '('}
        lifo_list = []

        # 2. 遍历s
        for i in range(len(s)):
            # 3. 如果遇到右边的括号则pop看是否对应
            if s[i] not in right_dict.keys():
                lifo_list.append(s[i])
            else:
                if len(lifo_list) == 0:
                    return False
                last = lifo_list.pop(-1)
                if last != right_dict[s[i]]:
                    return False

        if len(lifo_list) != 0:
            return False
        else:
            return True




if __name__ == '__main__':
    test_str = ''
    # test_str = '(){}[]'
    # test_str = '(]'
    # test_str = '([])'
    # test_str = '({])'
    print(Solution().isValid(test_str))