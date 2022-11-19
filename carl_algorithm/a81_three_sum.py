# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a81_three_sum.py
@Time: 2022-10-09 16:18
@Last_update: 2022-10-09 16:18
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
    给出所有三数之和为0的不同组合
    1. 首先创建result list，并对nums进行排序
    2. 遍历第一层，到nums长度减2
    3. 如果index值大于0则break
    4. 如果index大于0，且index值等于index-1则跳过
    5. 创建左右指针，遍历，条件为left小于right
    6. 如果当前数值大于0则right减一
    7. 如果当前数值小于0则left加一
    8. 当等于的时候，把组合放入result list
    9. 对left进行去重，保证left小于right，条件为left等于left+1的值
    10. 对right进行去重，保证left小于right，条件为right等于right-1的值
    11. 对left，right进行更新
    """
    # 1. 首先创建result list，并对nums进行排序
    result_list = []
    nums.sort()
    # 2. 遍历第一层，到nums长度减2
    for index in range(len(nums) - 2):
        # 3. 如果index值大于0则break
        if nums[index] > 0:
            break
        # 4. 如果index大于0，且index值等于index-1则跳过
        if (index > 0) and (nums[index] == nums[index - 1]):
            continue
        # 5. 创建左右指针，遍历，条件为left小于right
        left, right = index + 1, len(nums) - 1
        while left < right:
            sum_value = nums[index] + nums[left] + nums[right]
            # 6. 如果当前数值大于0则right减一
            if sum_value > 0:
                right -= 1
            # 7. 如果当前数值小于0则left加一
            elif sum_value < 0:
                left += 1
            # 8. 当等于的时候，把组合放入result list
            else:
                result_list.append([nums[index], nums[left], nums[right]])
                # 9. 对left进行去重，保证left小于right，条件为left等于left+1的值
                while (left < right) and (nums[left] == nums[left + 1]):
                    left += 1
                # 10. 对right进行去重，保证left小于right，条件为right等于right-1的值
                while (left < right) and (nums[right] == nums[right - 1]):
                    right -= 1
                # 11. 对left，right进行更新
                left += 1
                right -= 1

    return result_list

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
