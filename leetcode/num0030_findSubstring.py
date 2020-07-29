# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0030_findSubstring.py
@Time: 2020-07-28 10:41
@Last_update: 2020-07-28 10:41
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from collections import Counter


class Solution:
    """
    给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
    注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
    解法：使用滑动窗口的方法
    """
    def findSubstring(self, s, words):
        """
        整体流程：
        1. 进行特判
        2. 根据words生成字符的哈希表words_dict
        3. 生成左右指针等中间变量
        4. 遍历字符
        5. 如果开头的字符位置开始的词不在words_dict，则左右加1
        6. 如果开头的字符在words_dict
        7. 遍历查找后边的词
        8. 如果不在words_dict，则左右指针移动到相应位置加1，更新tmp_dict
        9. 如果在tmp_dict但是相应的值大于words_dict的值，则移动左右指针到当前位置，更新tmp_dict
        10. 如果在words_dict且小于等于words_dict的值则更新tmp_dict
        11. 返回结果
        """
        # 1. 进行特判
        if (len(s) == 0) or (len(words) == 0):
            return []

        # 2. 根据words生成字符的哈希表words_dict
        words_dict = Counter(words)

        # 3. 生成左右指针等中间变量
        word_len = len(words[0])
        left, right = 0, word_len * len(words)
        rst_list = []
        tmp_dict = dict()

        # 4. 遍历字符
        while right <= len(s):
            tmp_word = s[left: left+word_len]
            # 5. 如果开头的字符位置开始的词不在words_dict，则左右加1
            if tmp_word not in words_dict:
                left += 1
                right += 1
                continue

            # 6. 如果开头的字符在words_dict
            # 7. 遍历查找后边的词
            tmp_dict[tmp_word] = tmp_dict.get(tmp_word, 0) + 1
            inner_left = left + word_len
            inner_right = inner_left + word_len
            while inner_right <= right:
                next_word = s[inner_left: inner_right]
                tmp_dict[next_word] = tmp_dict.get(next_word, 0) + 1
                # 8. 如果不在words_dict，则左右指针移动到相应位置加1，更新tmp_dict
                if next_word not in words_dict:
                    left = left + 1
                    right = left + word_len * len(words)
                    tmp_dict = dict()
                    break
                # 9. 如果在tmp_dict但是相应的值大于words_dict的值，则移动左右指针到当前位置，更新tmp_dict
                elif tmp_dict[next_word] > words_dict[next_word]:
                    left += 1
                    right = left + word_len * len(words)
                    tmp_dict = dict()
                    break
                # 10. 如果在words_dict且小于等于words_dict的值则更新tmp_dict
                else:
                    inner_left += word_len
                    inner_right = inner_left + word_len

            if right == inner_left:
                rst_list.append(left)
                left += 1
                right = left + word_len * len(words)
                tmp_dict = dict()

        return rst_list



if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "good"]
    # s = "aaaaaaaa"
    # words = ["aa", "aa", "aa"]
    s = "abaababbaba"
    words = ["ab", "ba", "ab", "ba"]
    print(Solution().findSubstring(s, words))