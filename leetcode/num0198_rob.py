# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0198_rob.py
@Time: 2020-07-08 09:54
@Last_update: 2020-07-08 09:54
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
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
    影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
    解法：使用动态规划
    1. dp的含义：dp[i]表示第i个当前最高的总和
    2. dp的转移公式：一共两种情况，选当前的和选前一个的，dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    3. dp的初始值：dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
    4. dp的遍历方向：i的依赖向左，从小到大遍历
    """
    def rob(self, nums):
        """
        整体流程：
        0. 进行特判
        1. 生成dp列表以及需要的中间变量
        2. 初始化dp矩阵
        3. 遍历i
        4. 进行dp更新
        5. 返回最大值
        """
        # 0. 进行特判
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        # 1. 生成dp列表以及需要的中间变量
        dp = list(range(len(nums)))

        # 2. 初始化dp矩阵
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 3. 遍历i
        for i in range(2, len(nums)):
            # 4. 进行dp更新
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        print(dp)
        # 5. 返回最大值
        return dp[-1]


if __name__ == '__main__':
    nums = [1,2,3,1]
    nums = [2,7,9,3,1]
    print(Solution().rob(nums))