# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0046_permute.py
@Time: 2020-04-24 22:54
@Last_update: 2020-04-24 22:54
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
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。
    解法：
    使用回溯方法，遍历所有可能性
    """

    def backtrack_template(self, nums, choose_list, used_list, rst_dict):
        """
        回溯主体
        整体流程：
        1. 结束条件
        2. 遍历元素
        3. 选择，递归，回溯
        """
        # 1. 结束条件
        if len(choose_list) == len(nums):
            if tuple(choose_list) not in rst_dict:
                rst_dict[tuple(choose_list)] = 1

        # 2. 遍历元素
        for i in range(len(nums)):
            # 3. 选择，递归，回溯
            if not used_list[i]:
                used_list[i] = True
                choose_list.append(nums[i])
                rst_dict = self.backtrack_template(nums, choose_list, used_list, rst_dict)
                choose_list.pop(-1)
                used_list[i] = False

        return rst_dict

    def permute_template(self, nums):
        """
        整体流程：
        1. 生成中间所需要的变量
        2. 调用回溯
        3. 返回结果
        """
        # 1. 生成中间所需要的变量
        rst_dict = dict()
        used_list = [False for _ in range(len(nums))]

        # 2. 调用回溯
        rst_dict = self.backtrack(nums, [], used_list, rst_dict)

        # 3. 返回结果
        return [list(i) for i in rst_dict.keys()]

    def backtrack(self, nums, first, rst_list):
        """
        通过交换位置而不是记录来完成遍历
        整体流程：
        1. 结束条件
        2. 遍历可能
        3. 选择，交换，递归，回溯
        4. 返回结果
        """
        # 1. 结束条件
        if first == len(nums):
            rst_list.append(nums[:])
            return rst_list

        # 2. 遍历可能
        for i in range(first, len(nums)):
            # 3. 选择，交换，递归，回溯
            nums[i], nums[first] = nums[first], nums[i]
            rst_list = self.backtrack(nums, first+1, rst_list)
            nums[first], nums[i] = nums[i], nums[first]

        # 4. 返回结果
        return rst_list

    def permute(self, nums):
        """
        整体流程：
        1. 生成所需的中间变量
        2. 调用回溯
        3. 返回结果
        """
        # 1. 生成所需的中间变量
        rst_list = []

        # 2. 调用回溯
        rst_list = self.backtrack(nums, 0, rst_list)

        # 3. 返回结果
        return rst_list


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))