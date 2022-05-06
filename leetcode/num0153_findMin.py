# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0153_findMin.py
@Time: 2020-07-27 10:00
@Last_update: 2020-07-27 10:00
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
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    你可以假设数组中不存在重复元素。
    解法：使用二分查找，特判，中值判断，边界收缩
    """
    def findMin(self, nums):
        """
        整体流程：
        1. 进行特判
        2. 生成双指针等中间变量
        3. 中值判断
        4. 边界收缩
        """
        # 1. 进行特判
        if len(nums) == 0:
            return None
        # elif len(nums) <= 2:
        #     return min(nums)

        # 2. 生成双指针等中间变量
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            left_v = nums[left]
            mid_v = nums[mid]
            right_v = nums[right]
            # 3. 中值判断
            if (mid_v >= left_v) and (right_v < left_v):
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == '__main__':
    nums = [3,4,5,1,2]
    nums = [4,5,6,7,0,1,2]
    nums = [2,1]
    nums = [1,2]
    nums = [3,1,2]
    print(Solution().findMin(nums))