# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a31_top_k_freq_values.py
@Time: 2022-04-18 17:36
@Last_update: 2022-04-18 17:36
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import heapq


def top_k_freq_values(nums, k):
    """
    返回top k频率的数值
    使用堆来进行数值
    1. 统计相关的数值
    2. 把相应的数值放到堆中，如果大于k则弹出
    3. 最终返回k个最大的
    """
    # 1. 统计相关的数值
    freq_dict = dict()
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    # 2. 把相应的数值放到堆中，如果大于k则弹出
    heap = []
    for key, freq in freq_dict.items():
        heapq.heappush(heap, (freq, key))
        if len(heap) > k:
            heapq.heappop(heap)

    # 3. 最终返回k个最大的
    res_list = [0] * k
    for i in range(k - 1, -1, -1):
        res_list[i] = heapq.heappop(heap)[1]

    return res_list


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_freq_values(nums, k))
