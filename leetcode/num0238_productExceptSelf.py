# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0238_productExceptSelf.py
@Time: 2020-05-28 10:36
@Last_update: 2020-05-28 10:36
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
    给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    解法:
    构建左边乘积列表，右边的乘积列表使用单个值，然后直接得到结果乘积的结果
    """
    def productExceptSelf(self, nums):
        """
        整体流程：
        1. 构建左边乘积列表
        2. 遍历得到右边乘积的值
        3. 更新结果列表
        """
        if len(nums) == 0:
            return 0

        # 1. 构建左边乘积列表
        rst_list = [1]
        for i in range(len(nums) - 1):
            rst_list.append(nums[i] * rst_list[i])

        # 2. 遍历得到右边乘积的值
        right = 1
        for i in range(len(nums)-1, -1, -1):
            # 3. 更新结果列表
            rst_list[i] = rst_list[i] * right
            right *= nums[i]

        return rst_list


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))