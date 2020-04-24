#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0026_removeDuplicates.py
@Time: 2020-04-24 10:10
@Last_update: 2020-04-24 10:10
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
    给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
    解法：
    通过双指针来进行换值
    """
    def removeDuplicates(self, nums):
        """
        整体流程：
        1. 处理特殊情况
        2. 设置双指针并赋予初值
        3. 遍历，遍历条件为j小于矩阵长度
        4. 如果i, j的数值相同则移动j
        5. 如果i, j的数值不同则移动j，移动i并把j的值赋给i
        """
        # 1. 处理特殊情况
        if len(nums) < 2:
            return len(nums)

        # 2. 设置双指针并赋予初值
        i = 0
        j = 1

        # 3. 遍历，遍历条件为j小于矩阵长度
        while j < len(nums):
            # 4. 如果i, j的数值相同则移动j
            if nums[i] == nums[j]:
                j += 1
            # 5. 如果i, j的数值不同则移动j，移动i并把j的值赋给i
            else:
                i += 1
                nums[i] = nums[j]
                j += 1

        return len(nums[: i+1])



if __name__ == '__main__':
    nums = [1, 1, 2]
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # nums = []
    # nums = [1]
    print(Solution().removeDuplicates(nums))