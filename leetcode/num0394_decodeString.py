#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0394_decodeString.py
@Time: 2020-04-20 15:10
@Last_update: 2020-04-20 15:10
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
    给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
    你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
    此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
    解法：
    1. 如果遇到数字则建立递归函数处理
    """
    def deal_with_num(self, s, index):
        """
        整体流程：
        1. 遍历获得数字
        2. 情况1：如果遇到[则获取数字
        3. 情况2：如果遇到数字则递归
        4. 情况3：如果遇到字母则添加到inner_str
        5. 情况4：如果遇到]则返回字符和index
        """
        # 1. 遍历获得数字
        num = s[index]
        inner_str = ''
        rst_str = ''
        in_cycle = False
        while True:
            index += 1
            # 2. 情况1：如果遇到[则略过
            if s[index] == '[':
                num = int(num)
                in_cycle = True
            # 3. 情况2：如果遇到数字则递归
            elif ('0' <= s[index] <= '9') and in_cycle:
                tmp_str, index = self.deal_with_num(s, index)
                inner_str += tmp_str
            elif ('0' <= s[index] <= '9') and not in_cycle:
                num += s[index]
            # 4. 情况3：如果遇到字母则添加到inner_str
            elif ('a' <= s[index] <= 'z') or ('A' <= s[index] <= 'Z'):
                inner_str += s[index]
            # 5. 情况4：如果遇到]则返回字符和index
            elif s[index] == ']':
                rst_str += num * inner_str
                return rst_str, index


    def decodeString(self, s: str) -> str:
        """
        整体流程：
        1. 遍历字符
        2. 情况1：如果遇到数字则调用函数
        3. 情况2：如果遇到字母，则开始放入
        """
        if len(s) == 0:
            return s

        rst_str = ''
        index = 0
        # 1. 遍历字符
        while True:
            # 2. 情况1：如果遇到数字则调用函数
            if '0' <= s[index] <= '9':
                tmp_str, index = self.deal_with_num(s, index)
                rst_str += tmp_str
            # 3. 情况2：如果遇到字母，则开始放入
            elif ('a' <= s[index] <= 'z') or ('A' <= s[index] <= 'Z'):
                rst_str += s[index]

            index += 1
            if index >= len(s):
                break

        return rst_str


if __name__ == '__main__':
    s = "3[a]2[bc]"
    # s = "3[a2[c]]"
    # s = "2[abc]3[cd]ef"
    # s = '100[leetcode]'
    s = "3[a]2[b4[F]c]"
    print(Solution().decodeString(s))