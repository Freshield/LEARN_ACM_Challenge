#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a29_eraseOverlapIntervals.py
@Time: 2020-04-26 17:47
@Last_update: 2020-04-26 17:47
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
    给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
    注意:
    可以认为区间的终点总是大于它的起点。
    区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
    解法：
    用贪心算法，按照结尾时间算
    """
    def eraseOverlapIntervals(self, intervals):
        """
        整体流程：
        1. 对数据按结尾时间排序
        2. 遍历数组
        3. 找出所有要删除的区间数量
        """
        if len(intervals) <= 1:
            return 0
        # 1. 对数据按结尾时间排序
        intervals.sort(key=lambda x: x[1])
        # 2. 遍历数组
        earse_count = 0
        end = intervals[0][0]
        for inter in intervals:
            if inter[0] >= end:
                end = inter[1]
            else:
                earse_count += 1

        return earse_count


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals = [[1, 2], [1, 2], [1, 2]]
    intervals = [[1, 2], [2, 3]]
    print(Solution().eraseOverlapIntervals(intervals))