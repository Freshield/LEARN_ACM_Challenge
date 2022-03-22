# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a21_four_sum.py
@Time: 2022-04-15 17:07
@Last_update: 2022-04-15 17:07
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def four_sum(nums, target):
    """
    四数之和
    使用双指针方法
    1. 判断边界条件，直接退出
    2. 创建结果列表，并排序nums
    3. 遍历第一个指针，如果下一个值相等则跳过
    4. 遍历第二个指针，如果下一个值相等则跳过
    5. 建立左右指针，并开始遍历到左右指针不相等
    6. 如果等于目标值则放到结果列表中
    7. 移动左右指针跳过相同的数值
    8. 如果小于目标值则移动左指针
    9. 如果大于目标值则移动右指针
    """
    # 1. 判断边界条件，直接推出
    if len(nums) < 4:
        return []
    # 2. 创建结果列表
    res, nums = [], sorted(nums)
    # 3. 遍历第一个指针，如果下一个值相等则跳过
    for first_index in range(len(nums) - 3):
        first_value = nums[first_index]
        if (first_index != 0) and (first_value == nums[first_index - 1]):
            continue
        # 4. 遍历第二个指针，如果下一个值相等则跳过
        for second_index in range(first_index + 1, len(nums) - 2):
            second_value = nums[second_index]
            if (second_index != first_index + 1) and (second_value == nums[second_index - 1]):
                continue
            # 5. 建立左右指针，并开始遍历到左右指针不相等
            left_index, right_index = second_index + 1, len(nums) - 1
            while left_index < right_index:
                left_value = nums[left_index]
                right_value = nums[right_index]
                # 6. 如果等于目标值则放到结果列表中
                sum_value = first_value + second_value + left_value + right_value
                if sum_value == target:
                    res.append([first_value, second_value, left_value, right_value])
                    # 7. 移动左右指针跳过相同的数值
                    while (left_index < right_index) and (left_value == nums[left_index + 1]):
                        left_index += 1
                    while (left_index < right_index) and (right_value == nums[right_index - 1]):
                        right_index -= 1
                    left_index += 1
                    right_index -= 1
                # 8. 如果小于目标值则移动左指针
                elif sum_value < target:
                    left_index += 1
                # 9. 如果大于目标值则移动右指针
                else:
                    right_index -= 1

    return res


if __name__ == '__main__':
    nums = [2, 2, 2, 2]
    nums = [-2, -1, -1, 1, 1, 2, 2]
    nums = [-5, -2, -4, -2, -5, -4, 0, 0]
    target = 8
    target = 0
    target = -13
    print(four_sum(nums, target))
