# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0053_maxSubArray.py
@Time: 2020-04-19 14:00
@Last_update: 2020-04-19 14:00
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
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    """
    def maxSubArray(self, nums):
        """
        滚动加总，如果当前sum<0则从i重新计算，因为加上复数只会更小，如果大于0才继续计算
        整体流程：
        1. 遍历i
        2. 如果当前sum<0则从i重新计算，因为加上负数只会更小，如果大于0才继续计算
        """
        sum = nums[0]
        max_sum = sum
        for i in range(1, len(nums)):
            sum = sum + nums[i] if sum >= 0 else nums[i]
            max_sum = max_sum if max_sum > sum else sum

        return max_sum

    def maxSubArray_split(self, nums):
        """
        分治法，最大自序必在左半边，右半边或者中间，分别求出
        整体流程：
        1. 终止条件：len(nums)==1，返回nums[0]
        2. 使用递归得到左，右两个自序的和
        3. 得到中间的和
        4. 返回三个和中最大的
        """
        # 1. 终止条件：len(nums)==1，返回nums[0]
        if len(nums) == 1:
            return nums[0]

        # 2. 使用递归得到左，右两个自序的和
        left_sum_max = self.maxSubArray_split(nums[0: len(nums)//2])
        right_sum_max = self.maxSubArray_split(nums[len(nums)//2: len(nums)])

        # 3. 得到中间的和
        center_left = nums[len(nums)//2 - 1]
        tmp = center_left
        for i in range(len(nums)//2-2, -1, -1):
            tmp += nums[i]
            center_left = max(center_left, tmp)
        center_right = nums[len(nums)//2]
        tmp = center_right
        for i in range(len(nums)//2+1, len(nums)):
            tmp += nums[i]
            center_right = max(center_right, tmp)
        center_sum_max = center_left + center_right

        return max(left_sum_max, right_sum_max, center_sum_max)


    def maxSubArray_dp(self, nums):
        """
        使用动态规划方法来解
        解法：
        1. dp表示：dp[i]表示结尾为i的最大子序列和
        2. dp关系：
            i. 如果dp[i-1]<0，则dp[i] = nums[i]
            ii. 如果dp[i-1]>=0，则dp[i] = dp[i-1]+nums[i]
        3. dp初始值：dp[0] = nums[0]
        4. dp如何遍历：
            i的以来向左，所以i从小到大遍历
        整体流程：
        1. 设置初始值
        2. 遍历i的索引
        3. 得到dp[i]的值，并和最大值比较
        """
        # 1. 设置初始值
        dp = [None] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]

        # 2. 遍历i的索引
        for i in range(1, len(nums)):
            # 3. 得到dp[i]的值，并和最大值比较
            dp[i] = nums[i] if dp[i-1] < 0 else dp[i-1] + nums[i]
            max_sum = max(dp[i], max_sum)

        return max_sum


    def maxSubArray_force(self, nums):
        """
        暴力求解法，时间复杂度N**3
        整体流程：
        1. 遍历起始点begin
        2. 遍历右边点end，查找最大和
        """
        max_sum = -1
        for begin in range(len(nums)):
            for end in range(begin+1, len(nums)):
                sum = 0
                for i in range(begin, end):
                    sum += nums[i]
                    if sum > max_sum:
                        max_sum = sum

        return max_sum

    def maxSubArray_force_1(self, nums):
        """
        暴力求解法, 时间复杂度N**2
        整体流程：
        1. 遍历起始点begin
        2. 遍历右边点end，查找最大和
        """
        max_sum = -1
        for begin in range(len(nums)):
            sum = nums[begin]
            for end in range(begin+1, len(nums)):
                sum += nums[end]
                max_sum = max(max_sum, sum)

        return max_sum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray_split(nums))
