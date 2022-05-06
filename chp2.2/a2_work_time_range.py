#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_work_time_range.py
@Time: 2020-04-16 10:30
@Last_update: 2020-04-16 10:30
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class WorkTime(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return 's:%d, e:%d' % (self.start, self.end)


def solve(work_time_list, n):
    """
    n个工作，从s开始t结束，每个只能参加一次，并且不能终止，最多参加多少个工作
    解法：
    用贪心算法，找结束最早的
    整体流程：
    1. 对时间序列按结束时间进行排序
    2. 遍历时间序列，找到下一个开始的时间
    3. 如果开始时间在上一个结束时间之后则在这个时段进行工作
    """
    # 1. 对时间序列按结束时间进行排序
    work_time_list.sort(key=lambda x: x.end)

    end_time = -1
    work_count = 0
    # 2. 遍历时间序列，找到下一个开始的时间
    for work_time in work_time_list:
        # 3. 如果开始时间在上一个结束时间之后则在这个时段进行工作
        if work_time.start > end_time:
            end_time = work_time.end
            work_count += 1

    return work_count


if __name__ == '__main__':
    s = [1,2,4,6,8]
    t = [3,5,7,9,10]
    work_time_list = []
    for i in range(len(s)):
        work_time_list.append(WorkTime(s[i], t[i]))

    print(solve(work_time_list, len(work_time_list)))