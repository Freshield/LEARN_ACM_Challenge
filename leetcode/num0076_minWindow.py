# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0076_minWindow.py
@Time: 2020-07-03 10:16
@Last_update: 2020-07-03 10:16
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from collections import defaultdict


class Solution:
    """
    给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
    解法：
    使用滑动窗口，
    准备，右侧右移，右更新，判断左移，左侧右移，左更新
    """
    def minWindow(self, raw_str, pair_str):
        """
        整体流程：
        0. 进行特判
        1. 准备
        2. 右侧右移
        3. 右更新
        4. 判断左移
        5. 左侧右移
        6. 左更新
        """
        # 0. 进行特判
        if len(raw_str) == 0 or len(pair_str) == 0:
            return ''

        # 1. 准备
        need_dict = {word: pair_str.count(word) for word in set(pair_str)}
        window = defaultdict(int)
        left, right, valid = 0, 0, 0
        start, min_len = -1, len(raw_str) + 1

        # 2. 右移
        while right < len(raw_str):
            right_str = raw_str[right]
            right += 1
            # 3. 右更新
            if right_str in need_dict:
                window[right_str] += 1
                if window[right_str] == need_dict[right_str]:
                    valid += 1

            # 4. 判断左移
            while valid == len(need_dict):
                if (right - left) < min_len:
                    start = left
                    min_len = right - left
                # 5. 左移
                left_str = raw_str[left]
                left += 1
                # 6. 左更新
                if left_str in need_dict:
                    if window[left_str] == need_dict[left_str]:
                        valid -= 1
                    window[left_str] -= 1

        return '' if start == -1 else raw_str[start: start+min_len]


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print(Solution().minWindow(S, T))