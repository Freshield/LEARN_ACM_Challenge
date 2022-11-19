# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_shortest_sublist_r.py
@Time: 2022-09-04 23:32
@Last_update: 2022-09-04 23:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def shortest_sublist(s, nums):
    """
    获取大于等于s的最小连续子串长度
    1. 创建双指针，sum等变量，获取值为左闭右开
    2. 开始循环，结束为右指针越界
    3. 进行sum累加，如果sum小于s，则右指针加一，下一个循环
    4. 否则内循环，直到左指针小于等于右指针
    5. 记录当前的长度，看是否更新最小长度
    6. sum减去当前左指针的值，左指针加一，如果sum小于s则跳出
    """
    # 1. 创建双指针，sum等变量
    left_p, right_p, sum, shortest_length = 0, 0, 0, 0
    # 2. 开始循环，结束为右指针越界
    while right_p < len(nums):
        # 3. 进行sum累加，如果sum小于s，则右指针加一，下一个循环
        sum += nums[right_p]
        right_p += 1
        if sum < s:
            continue
        # 4. 否则内循环，直到左指针小于等于右指针
        while left_p < right_p:
            # 5. 记录当前的长度，看是否更新最小长度
            this_length = right_p - left_p
            shortest_length = this_length if (this_length < shortest_length) or (shortest_length == 0) else shortest_length
            # 6. sum减去当前左指针的值，左指针加一，如果sum小于s则跳出
            sum -= nums[left_p]
            left_p += 1
            if sum < s:
                break

    return shortest_length


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    shortest_length = shortest_sublist(s, nums)
    print(shortest_length)
