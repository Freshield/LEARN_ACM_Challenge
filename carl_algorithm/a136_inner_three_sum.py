# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_algorithm_test.py
@Time: 2022-10-21 10:45
@Last_update: 2022-10-21 10:45
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
"""
给你一个包含 n 个正整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b = c ？请你找出所有满足条件且不重复的三元组。

例子
输入
1, 2, 3, 4
输出
1, 2, 3
1, 3, 4

输入
1, 3, 4, 5, 5, 9, 10
输出
1, 3, 4
1, 4, 5
1, 9, 10
4, 5, 9
5, 5, 10
"""


def inner_three_sum(nums):
    """
    三数之和，使用双指针
    整体逻辑
    1. 处理特殊情况
    2. 创建结果列表，从后往前遍历，决定和c的值
    3. 创建左右指针，已使用值字典
    4. 遍历，条件为left小于right
    5. 去重，获取左右指针的值如果左右指针已存在字典中则跳过
    6. 存储当前的值到字典中
    7. 获取当前的和，如果等于c则左右都更新
    8. 如果当前的和大于c则right减一
    9. 如果当前的和小于c则左指针加一
    """
    # 1. 处理特殊情况
    if len(nums) < 3:
        return []
    # 2. 创建结果列表，从后往前遍历，决定和c的值
    res_list = []
    target_set = set()
    for i in range(len(nums) - 1, 1, -1):
        target_sum = nums[i]
        if target_sum in target_set:
            continue
        target_set.add(target_sum)
        # 3. 创建左右指针，已使用值字典
        left, right = 0, i - 1
        left_set, right_set = set(), set()
        # 4. 遍历，条件为left小于right
        while left < right:
            # 5. 去重，获取左右指针的值如果左右指针已存在字典中则跳过
            left_value, right_value = nums[left], nums[right]
            if left_value in left_set:
                left += 1
                continue
            if right_value in right_set:
                right -= 1
                continue
            # 7. 获取当前的和，如果等于c则左右都更新
            this_sum = left_value + right_value
            if this_sum == target_sum:
                res_list.append([left_value, right_value, target_sum])
                left += 1
                right -= 1
                # 6. 存储当前的值到字典中
                left_set.add(left_value)
                right_set.add(right_value)
                continue
            # 8. 如果当前的和大于c则right减一
            if this_sum > target_sum:
                right -= 1
                right_set.add(right_value)
                continue
            # 9. 如果当前的和小于c则左指针加一
            if this_sum < target_sum:
                left += 1
                left_set.add(left_value)
                continue

    return res_list


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(nums)
    print(three_sum(nums))
