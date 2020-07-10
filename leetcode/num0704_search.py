# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0704_search.py
@Time: 2020-07-10 10:17
@Last_update: 2020-07-10 10:17
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
    给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
    写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
    解法：
    使用减治的方法使用二分查找，特判，中值判断，边界收缩
    """
    def search(self, nums, target):
        """
        整体流程：
        1. 进行特判
        2. 生成左右边界等变量
        3. 得到中值
        4. 中值判断
        5. 边界收缩
        6. 判断结果
        """
        # 1. 进行特判
        if len(nums) == 0:
            return -1
        elif (target > nums[-1]) or (target < nums[0]):
            return -1

        # 2. 生成左右边界等变量
        left, right = 0, len(nums) - 1

        while left < right:
            # 3. 得到中值
            mid = left + (right - left) // 2
            # 4. 中值判断
            if nums[mid] < target:
                # 5. 边界收缩
                left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                right = mid

        # 6. 判断结果
        return left if nums[left] == target else -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    # target = 2
    print(Solution().search(nums, target))