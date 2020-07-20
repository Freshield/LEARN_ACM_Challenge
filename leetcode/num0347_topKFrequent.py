# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0347_topKFrequent.py
@Time: 2020-07-20 09:58
@Last_update: 2020-07-20 09:58
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
    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
    解法：
    使用字典来记录频率，然后进行排序返回
    """
    def topKFrequent(self, nums, k):
        """
        整体流程：
        1. 进行特判
        2. 生成freq_dict等变量
        3. 遍历nums得到出现的频率
        4. 对freq_dict进行排序
        5. 返回前k个元素
        """
        # 1. 进行特判
        if len(nums) == 0:
            return nums

        # 2. 生成freq_dict等变量
        freq_dict = dict()

        # 3. 遍历nums得到出现的频率
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # 4. 对freq_dict进行排序
        freq_list = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

        # 5. 返回前k个元素
        return [item[0] for item in freq_list[: k]]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    nums = [1]
    k = 1
    print(Solution().topKFrequent(nums, k))