# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0448_findDisappearedNumbers.py
@Time: 2020-04-20 22:45
@Last_update: 2020-04-20 22:45
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
    给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，
    数组中的元素一些出现了两次，另一些只出现一次。
    找到所有在 [1, n] 范围之间没有出现在数组中的数字。
    您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗?
    你可以假定返回的数组不算在额外空间内。
    解法：
    把出现的数相应的位置都变为负数，则数组里正数的位置便是没出现过得
    """
    def findDisappearedNumbers(self, nums):
        """
        整体流程：
        1. 遍历对相应数位置的索引变为负数
        2. 遍历生成不为负数的数组
        """
        # 1. 遍历对相应数位置的索引变为负数
        for num in nums:
            num_index = abs(num) - 1
            num_index_value = abs(nums[num_index])
            nums[num_index] = -num_index_value

        return [i+1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))