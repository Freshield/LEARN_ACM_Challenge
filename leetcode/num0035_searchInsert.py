# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0035_searchInsert.py
@Time: 2020-06-24 10:55
@Last_update: 2020-06-24 10:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution:
    """
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。
    解法：
    使用二分查找，减治法
    1. 不是解区间：严格小于target的mid不是解
    2. 新搜索区间：left = mid + 1
    """
    def searchInsert(self, nums, target):
        """
        整体流程：
        1. 进行特判
        2. 构建左右指针并遍历
        3. 不是解区间：严格小于target的mid不是解
        4. 新搜索区间：left = mid + 1
        """
        # 1. 进行特判
        if len(nums) == 0:
            return 0
        elif target > nums[-1]:
            return len(nums)

        # 2. 构建左右指针并遍历
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right - left) // 2
            # 3. 不是解区间：严格小于target的mid不是解
            if nums[mid] < target:
                # 4. 新搜索区间：left = mid + 1
                left = mid + 1
            # elif nums[mid] == target:
            #     return mid
            else:
                right = mid

        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    nums = [1, 3, 5, 6]
    target = 2
    nums = [1, 3, 5, 6]
    target = 7
    nums = [1, 3, 5, 6]
    target = 0
    print(Solution().searchInsert(nums, target))