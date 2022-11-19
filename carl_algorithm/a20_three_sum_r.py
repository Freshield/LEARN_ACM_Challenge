# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a20_three_sum_r.py
@Time: 2022-10-08 18:16
@Last_update: 2022-10-08 18:16
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def three_sum_r(nums):
    """
    三数之和，用双指针法
    1. 生成保存结果的数组，并对nums进行排序
    2. 遍历nums
    3. 如果num大于0，则直接返回
    4. 如果当前i和i-1相同则跳过
    5. 生成并遍历left，right，条件为left小于right
    6. 得到sum
    7. 如果sum大于0则right减一
    8. 如果sum小于0则left加一
    9. 当等于0时，放入当前组合
    10. 对left进行去重，条件为left小于right且left和left加一相同
    11. 对right进行去重，条件为left小于right且right和right减一相同
    12. 对left，right进行更新
    """
    # 1. 生成保存结果的数组，并对nums进行排序
    result_list = []
    nums.sort()

    # 2. 遍历nums
    for i in range(len(nums)-2):
        # 3. 如果num大于0，则直接返回
        if nums[i] > 0:
            return result_list

        # 4. 如果当前i和i-1相同则跳过
        if (i > 0) and (nums[i] == nums[i-1]):
            continue

        # 5. 生成并遍历left，right，条件为left小于right
        left, right = i+1, len(nums)-1
        while left < right:
            # 6. 得到sum
            sum_value = nums[i] + nums[left] + nums[right]
            # 7. 如果sum大于0则right减一
            if sum_value > 0:
                right -= 1
            # 8. 如果sum小于0则left加一
            elif sum_value < 0:
                left += 1
            # 9. 当等于0时，放入当前组合
            else:
                result_list.append([nums[i], nums[left], nums[right]])
                # 10. 对left进行去重，条件为left小于right且left和left加一相同
                while (left < right) and (nums[left] == nums[left+1]):
                    left += 1
                # 11. 对right进行去重，条件为left小于right且right和right减一相同
                while (left < right) and (nums[right] == nums[right-1]):
                    right -= 1
                # 12. 对left，right进行更新
                left += 1
                right -= 1

    return result_list


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum_r(nums))
