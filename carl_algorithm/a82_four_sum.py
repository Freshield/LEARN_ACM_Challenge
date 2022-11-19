# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a82_four_sum.py
@Time: 2022-10-09 16:47
@Last_update: 2022-10-09 16:47
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def four_sum(nums):
    """
    四数之和
    1. 创建result list，并对nums进行排序
    2. 进行第一层遍历，到nums的长度减3
    3. 如果i大于target，且i大于0，则break
    4. 如果i的值和i-1的值相同则跳过
    5. 进行第二层遍历，到nums的长度减2
    6. 如果i的值加j的值大于target，且i的值加j的值大于0，则break
    7. 如果j的值和j-1的值相同则跳过
    8. 构建left，right指针
    9. 遍历，条件为left小于right
    10. 计算sum value
    11. 如果sum大于target，则right减一
    12. 如果sum小于target，则left加一
    13. 如果等于，则放入result list
    14. 对right去重，条件为left小于right，且right的值和right减一的值相同
    15. 对left去重，条件为left小于right，且left的值和left加一的值相同
    16. 更新left，right
    """
    # 1. 创建result list，并对nums进行排序
    result_list = []
    nums.sort()
    # 2. 进行第一层遍历，到nums的长度减3
    for i in range(len(nums) - 3):
        # 3. 如果i大于target，且i大于0，则break
        if (nums[i] > target) and (nums[i] > 0):
            break
        # 4. 如果i的值和i-1的值相同则跳过
        if (i > 0) and (nums[i] == nums[i - 1]):
            continue
        # 5. 进行第二层遍历，到nums的长度减2
        for j in range(i + 1, len(nums) - 2):
            # 6. 如果i的值加j的值大于target，且i的值加j的值大于0，则break
            if (nums[i] + nums[j] > target) and (nums[i] + nums[j] > 0):
                break
            # 7. 如果j的值和j-1的值相同则跳过
            if (j > i + 1) and (nums[j] == nums[j - 1]):
                continue
            # 8. 构建left，right指针
            left, right = j + 1, len(nums) - 1
            # 9. 遍历，条件为left小于right
            while left < right:
                # 10. 计算sum value
                sum_value = nums[i] + nums[j] + nums[left] + nums[right]
                # 11. 如果sum大于target，则right减一
                if sum_value > target:
                    right -= 1
                # 12. 如果sum小于target，则left加一
                elif sum_value < target:
                    left += 1
                # 13. 如果等于，则放入result list
                else:
                    result_list.append([
                        nums[i], nums[j], nums[left], nums[right]
                    ])
                    # 14. 对right去重，条件为left小于right，且right的值和right减一的值相同
                    while (left < right) and (nums[right] == nums[right - 1]):
                        right -= 1
                    # 15. 对left去重，条件为left小于right，且left的值和left加一的值相同
                    while (left < right) and (nums[left] == nums[left + 1]):
                        left += 1
                    # 16. 更新left，right
                    left += 1
                    right -= 1

    return result_list


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(four_sum(nums))
