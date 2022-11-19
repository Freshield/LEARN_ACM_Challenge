# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a89_find_k_most_freq.py
@Time: 2022-10-11 20:28
@Last_update: 2022-10-11 20:28
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


def find_k_most_freq(nums, k):
    """
    找到k个最高频的数字
    1. 构建小顶堆，词频字典
    2. 遍历创建词频字典
    3. 遍历向小顶堆插入词频的tuple
    4. 如果小顶堆的数量超过k，则pop出最小的
    5. 返回倒序结果
    """
    # 1. 构建小顶堆，词频字典
    heap, freq_dict = [], dict()
    # 2. 遍历创建词频字典
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    # 3. 遍历向小顶堆插入词频的tuple
    for num, freq in freq_dict.items():
        heapq.heappush(heap, (freq, num))
        # 4. 如果小顶堆的数量超过k，则pop出最小的
        if len(heap) > k:
            heapq.heappop(heap)

    #5. 返回倒序结果
    result = []
    for i in range(len(heap)):
        result.append(heapq.heappop(heap)[1])

    return result[::-1]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(find_k_most_freq(nums, k))
