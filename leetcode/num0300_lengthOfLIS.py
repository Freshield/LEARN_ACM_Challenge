# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0300_lengthOfLIS.py
@Time: 2020-05-18 22:46
@Last_update: 2020-05-18 22:46
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
    给定一个无序的整数数组，找到其中最长上升子序列的长度。
    解法：
    一.使用动态规划
    1. dp的含义：dp[i]代表包含以num[i]结尾的最长上升子序列的长度
    2. dp的状态转换公式：
        dp[i]为 遍历dp[0]到dp[i-1]中相应的num的值，
        如果nums[i]比num[j]的值大，则为dp[j]+1，得到从0到i-1中最大的值
        dp[i] = max(dp[i], dp[j](0->i-1) + 1 if num[i] > j), 如果都没匹配上则为1
    3. dp的初始化：dp[1] = 1
    4. dp的遍历方式：
        i的依赖向左，所以i从小到大遍历
    """
    def lengthOfLIS(self, nums):
        """
        整体流程：
        1. 生成dp矩阵等变量
        2. 遍历nums的顺序i
        3. 遍历已经生成的dp顺序j
        4. 进行比较更新dp[i]
        5. 返回最大值
        """
        if len(nums) == 0:
            return 0

        # 1. 生成dp矩阵等变量
        dp = [1] * len(nums)
        max_value = 1

        # 2. 遍历nums的顺序i
        for i in range(len(nums)):
            # 3. 遍历已经生成的dp顺序j
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

            max_value = max_value if max_value > dp[i] else dp[i]

        # 5. 返回最大值
        return max_value


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))