#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0136_singleNumber.py
@Time: 2020-04-24 10:30
@Last_update: 2020-04-24 10:30
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
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    说明：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    解法：
    使用异或方法，直接得到那个唯一的数
    """
    def singleNumber(self, nums):
        """
        整体流程：
        1. 处理特殊情况
        2. 遍历对所有数字进行异或比较
        """
        # 1. 处理特殊情况
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]

        # 2. 遍历对所有数字进行异或比较
        for i in range(1, len(nums)):
            nums[i] = nums[i] ^ nums[i-1]

        return nums[-1]


if __name__ == '__main__':
    nums = [2, 2, 1]
    # nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))