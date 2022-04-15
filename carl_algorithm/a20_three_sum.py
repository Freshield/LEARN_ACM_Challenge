# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a20_three_sum.py
@Time: 2022-04-15 15:54
@Last_update: 2022-04-15 15:54
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def three_sum(nums):
    """
    三数之和
    使用双指针的方法
    1. 判断边界条件退出
    2. 创建结果数组并对nums排序
    3. 遍历开始数到nums-2的长度，并创作左右指针
    4. 如果上一个结果的开头一样则跳过
    5. 遍历左右指针直到左右指针相等
    6. 如果三数只和为0则放到结果中
    7. 略去相同的左指针和右指针
    8. 如果三数只和小于0则移动右指针
    9. 如果三数只和大于0则移动左指针
    """
    # 1. 判断边界条件退出
    if len(nums) < 3:
        return []
    # 2. 创建结果数组并对nums排序
    left_index, right_index, nums, res = 1, len(nums) - 1, sorted(nums), []
    # 3. 遍历开始数到nums-2的长度，并创作左右指针
    for cur in range(len(nums) - 2):
        cur_value = nums[cur]
        left_index, right_index = cur + 1, len(nums) - 1
        # 4. 如果上一个结果的开头一样则跳过
        if (len(res) != 0) and (res[-1][0] == cur_value):
            continue

        # 5. 遍历左右指针直到左右指针相等
        while left_index < right_index:
            left_value, right_value = nums[left_index], nums[right_index]
            # 6. 如果三数只和为0则放到结果中
            sum_value = cur_value + left_value + right_value
            if sum_value == 0:
                res.append([cur_value, left_value, right_value])

                # 7. 略去相同的左指针和右指针
                while (left_index < right_index) and (left_value == nums[left_index+1]):
                    left_index += 1
                while (left_index < right_index) and (right_value == nums[right_index-1]):
                    right_index -= 1
                left_index += 1
                right_index -= 1
            # 8. 如果三数只和小于0则移动右指针
            elif sum_value < 0:
                left_index += 1
            # 9. 如果三数只和大于0则移动左指针
            else:
                right_index -= 1

    return res


if __name__ == '__main__':
    nums = [-4, -1, -1, -1, -1, 2]
    nums = [0, 0, 0]
    target = 0
    print(three_sum(nums))
