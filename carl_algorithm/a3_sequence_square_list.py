# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_sequence_square_list.py
@Time: 2022-04-11 19:03
@Last_update: 2022-04-11 19:03
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def sequence_square_list(nums):
    """
    得到有序的平方结果
    使用双指针法
    1. 创建左右指针和结果列表
    2. 遍历条件为左右指针不相等
    3. 如果左指针指代的数值平方大于右指针数值平方则从左侧插入左指针的数值平方，并让左指针加一
    4. 如果右指针指代的数值平方大于左指针数值平方则从左侧插入右指针的数值平方，并让右指针减一
    """
    # 1. 创建左右指针和结果列表
    left_index, right_index, res_list = 0, len(nums) - 1, list()
    # 2. 遍历条件为左右指针不相等
    while left_index <= right_index:
        # 3. 如果左指针指代的数值平方大于右指针数值平方则从左侧插入左指针的数值平方，并让左指针加一
        if nums[left_index] ** 2 >= nums[right_index] ** 2:
            res_list.insert(0, nums[left_index] ** 2)
            left_index += 1
        else:
            res_list.insert(0, nums[right_index] ** 2)
            right_index -= 1

    return res_list


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    nums = [-7, -3, 2, 3, 11]
    print(sequence_square_list(nums))
