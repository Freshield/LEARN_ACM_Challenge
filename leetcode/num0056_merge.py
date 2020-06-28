# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0056_merge.py
@Time: 2020-06-28 09:47
@Last_update: 2020-06-28 09:47
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
    给出一个区间的集合，请合并所有重叠的区间。
    解法：
    使用贪心算法，来根据结尾进行合并
    """
    def merge(self, intervals):
        """
        整体流程：
        1. 进行特判
        2. 生成merged列表等中间变量
        3. 对列表按照起始位置进行排序
        4. 遍历列表和merged列表进行比较
        5. 如果merged为空或者merged的结尾比新的区间的开头严格小，则直接放入merged
        6. 否则进行合并，更新merged最后一个元素的结尾为当前区间的结尾
        """
        # 1. 进行特判
        if len(intervals) <= 1:
            return intervals

        # 2. 生成merged列表等中间变量
        merged = []

        # 3. 对列表按照起始位置进行排序
        intervals.sort(key=lambda x: x[0])

        # 4. 遍历列表和merged列表进行比较
        for interval in intervals:
            # 5. 如果merged为空或者merged的结尾比新的区间的开头严格小，则直接放入merged
            if len(merged) == 0 or (merged[-1][1] < interval[0]):
                merged.append(interval)
            # 6. 否则进行合并，更新merged最后一个元素的结尾为当前区间的结尾
            else:
                merged[-1][1] = interval[1] if merged[-1][1] < interval[1] else merged[-1][1]

        return merged


if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    intervals = [[1,4],[2,3]]
    print(Solution().merge(intervals))