# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_shortest_sublist.py
@Time: 2022-04-11 20:28
@Last_update: 2022-04-11 20:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def shortest_sublist(nums, s):
    """
    最短子序列
    使用滑动窗口
    1. 创建开始指针，结果长度以及和的值
    2. 遍历结束指针到队尾
    3. 遍历开始指针到结束指针
    4. 如果当前子序列和大于等于val，则记录长度，和的值减去开始指针的值，开始指针加一
    5. 否则退出循环
    """
    # 1. 创建开始，结束，结果长度指针以及和的值
    begin_index, res_length, sum = 0, len(nums) + 1, 0
    # 2. 遍历结束指针到队尾
    for end_index in range(len(nums)):
        sum += nums[end_index]
        # 3. 遍历开始指针到结束指针
        while begin_index <= end_index:
            # 4. 如果当前子序列和大于等于s，则记录长度，和的值减去开始指针的值，开始指针加一
            if sum >= s:
                tmp_length = end_index - begin_index + 1
                res_length = tmp_length if tmp_length < res_length else res_length
                sum -= nums[begin_index]
                begin_index += 1
            else:
                break

    return res_length if res_length != len(nums) + 1 else 0


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(shortest_sublist(nums, s))
