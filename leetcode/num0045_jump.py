# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0045_jump.py
@Time: 2020-07-17 10:50
@Last_update: 2020-07-17 10:50
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
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    解法：
    使用贪心算法
    """
    def jump(self, nums):
        """
        整体流程：
        1. 进行特判
        2. 生成maxpos，step，end等变量
        3. 遍历数组长度
        4. 更新可以到达最远的距离
        5. 如果i==end的时候进行当前区间的更新
        6. 返回步数
        """
        # 1. 进行特判
        if len(nums) == 0:
            return 0

        # 2. 生成maxpos，step，end等变量
        maxpos, step, end = 0, 0, 0

        # 3. 遍历数组长度
        for i in range(len(nums)-1):
            # 4. 更新可以到达最远的距离
            maxpos = max(maxpos, i + nums[i])

            # 5. 如果i==end的时候进行当前区间的更新
            if i == end:
                end = maxpos
                step += 1

        # 6. 返回步数
        return step

    def jump_raw(self, nums):
        """
        整体流程：
        1. 进行特判
        2. 生成now,begin,end,step的变量指针
        3. 遍历数组
        4. 结束条件为end大于等于len-1
        5. 计算begin到end区间中i的值加上nums[i]的最大值的索引
        6. 更新now,begin,end,step
        """
        # 1. 进行特判
        if len(nums) <= 1:
            return 0

        # 2. 生成now,begin,end,step的变量指针
        now, step, begin = 0, 1, 1
        end = now + nums[now]

        # 3. 遍历数组
        # 4. 结束条件为end大于等于len-1
        last_pos = len(nums) - 1
        while end < last_pos:
            # 5. 计算begin到end区间中i的值加上nums[i]的最大值的索引
            max_pos = max([(i, nums[i]) for i in range(begin, end+1)], key=lambda x: x[0] + x[1])[0]

            # 6. 更新now,begin,end,step
            step += 1
            now = max_pos
            begin = now + 1
            end = now + nums[now]

        return step


if __name__ == '__main__':
    # nums = [2,3,1,1,4]
    nums = [0]
    nums = [2, 1]
    print(Solution().jump(nums))