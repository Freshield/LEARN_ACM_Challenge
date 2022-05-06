# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0028_strStr.py
@Time: 2020-06-16 10:39
@Last_update: 2020-06-16 10:39
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
    实现 strStr() 函数。
    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
    如果不存在，则返回  -1。
    解法：
    Sunday算法
    使用双指针，遍历索引看是否相同，如果相同则直接返回
    如果不相同，查看偏移表来进行偏移
    偏移表：
    如果字符不在needle中，则为字符长
    如果字符在needle中，则为字符长减去当前字符的位置，如果重复则按照最后一个的位置算

    """
    def cal_shift(self, needle):
        shift_dict = dict()
        for i in range(len(needle)):
            shift_dict[needle[i]] = len(needle) - i

        shift_dict['ot'] = len(needle) + 1

        return shift_dict

    def strStr(self, haystack, needle):
        """
        整体流程：
        1. 构建偏移字典以及双指针等
        2. 遍历字符
        3. 看是否一致，如果不一致则进行判断
        """
        if (len(haystack) == 0) and (len(needle) == 0):
            return 0
        elif (len(haystack) == 0) and (len(needle) != 0):
            return -1

        # 1. 构建偏移字典以及双指针等
        shift_dict = self.cal_shift(needle)
        hay_index = 0

        # 2. 遍历字符
        while not (hay_index > (len(haystack)-len(needle))):
            tmp_str = haystack[hay_index:hay_index+len(needle)]
            # 3. 看是否一致，如果不一致则进行判断
            if tmp_str == needle:
                return hay_index

            shift_index = hay_index + len(needle)
            if shift_index >= len(haystack):
                break

            shift_word = haystack[shift_index]

            hay_index += shift_dict[shift_word] if shift_word in shift_dict else shift_dict['ot']

        return -1


if __name__ == '__main__':
    haystack = 'checkthisout'
    needle = 'this'
    haystack = "hello"
    needle = "ll"
    haystack = 'a'
    needle = 'a'
    print(Solution().strStr(haystack, needle))