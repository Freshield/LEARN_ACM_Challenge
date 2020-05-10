# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0078_subsets.py
@Time: 2020-05-14 10:10
@Last_update: 2020-05-14 10:10
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
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
    解法：
    使用回溯算法
    """
    def __init__(self):
        self.res = []

    def backtrack(self, index, path, nums):
        """
        整体流程：
        1. 结束条件：如果到达边界则返回
        2. 把当前结果添加到结果中
        3. 遍历剩下的数字
        4. 选择，递归，回溯
        """
        # 2. 把当前结果添加到结果中
        self.res.append(path[:])

        # 1. 结束条件：如果到达边界则返回
        if index == len(nums):
            return None

        # 3. 遍历剩下的数字
        for i in range(index, len(nums)):
            # 4. 选择，递归，回溯
            path.append(nums[i])
            self.backtrack(i+1, path, nums)
            path.pop(-1)

    def subsets(self, nums):
        """
        整体流程：
        1. 去除特殊情况
        2. 调用回溯算法
        """
        # 1. 去除特殊情况
        if len(nums) == 0:
            return nums

        # 2. 调用回溯算法
        self.backtrack(0, [], nums)

        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))