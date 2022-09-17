# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a21_four_sum_r.py
@Time: 2022-10-08 20:21
@Last_update: 2022-10-08 20:21
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
    四数之和，使用双指针法
    1. 创建结果列表，并对nums排序
    2. 遍历第一层，i
    3. 如果nums[i]大于target且nums[i]大于0，则直接返回result
    4. 如果i>0且nums[i] == nums[i-1]则继续
    5. 遍历第二层，j
    6. 如果nums[i]+nums[j]大于target且nums[i]+nums[j]大于0，则直接返回result
    7. 如果i>0且nums[j] == nums[j-1]则继续
    8. 创建left和right，遍历条件为left小于right
    9. 计算sum
    10. 如果sum大于target则right减一
    11. 如果sum小于target则left加一
    12. 如果sum等于target则加入结果字典
    13. 对right进行去重，条件为left<right，right和right-1相同
    14. 对left进行去重，条件为left<right，left和left+1相同
    15， 对left和right进行更新
    """
    # 1. 创建结果列表，并对nums排序
    result = []
    nums.sort()
    print(nums)

    # 2. 遍历第一层，i
    for i in range(len(nums)-3):
        # 3. 如果nums[i]大于target且nums[i]大于0，则直接返回result
        if (nums[i] > target) and (nums[i] > 0):
            break
        # 4. 如果i>0且nums[i] == nums[i-1]则继续
        if (i > 0) and (nums[i] == nums[i-1]):
            continue
        # 5. 遍历第二层，j
        for j in range(i+1, len(nums)-2):
            # 6. 如果nums[i]+nums[j]大于target且nums[i]+nums[j]大于0，则直接返回result
            if (nums[i] + nums[j] > target) and (nums[i] + nums[j] > 0):
                break
            # 7. 如果i>0且nums[j] == nums[j-1]则继续
            if (j > (i+1)) and (nums[j] == nums[j-1]):
                continue
            # 8. 创建left和right，遍历条件为left小于right
            left, right = j+1, len(nums)-1
            while left < right:
                # 9. 计算sum
                sum = nums[i] + nums[j] + nums[left] + nums[right]
                # 10. 如果sum大于target则right减一
                if sum > target:
                    right -= 1
                # 11. 如果sum小于target则left加一
                elif sum < target:
                    left += 1
                # 12. 如果sum等于target则加入结果字典
                else:
                    result.append([
                        nums[i], nums[j], nums[left], nums[right]
                    ])
                    # 13. 对right进行去重，条件为left<right，right和right-1相同
                    while (left < right) and (nums[right] == nums[right-1]):
                        right -= 1
                    # 14. 对left进行去重，条件为left<right，left和left+1相同
                    while (left < right) and (nums[left] == nums[left+1]):
                        left += 1
                    # 15， 对left和right进行更新
                    right -= 1
                    left += 1

    return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    nums = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
    target = 0
    print(four_sum(nums, target))
