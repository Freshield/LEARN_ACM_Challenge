# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0217_containsDuplicate.py
@Time: 2020-07-14 09:51
@Last_update: 2020-07-14 09:51
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
    给定一个整数数组，判断是否存在重复元素。
    如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
    解法：
    使用哈希表
    """
    def containsDuplicate(self, nums):
        """
        整体流程：
        1. 进行特判
        2. 生成存储字典等变量
        3. 遍历列表进行判定
        """
        # 1. 进行特判
        if len(nums) == 0:
            return False

        # 2. 生成存储字典等变量
        contains_dict = dict()

        # 3. 遍历列表进行判定
        for num in nums:
            if num in contains_dict:
                return True

            contains_dict[num] = 1

        return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    nums = [1,2,3,4]
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(Solution().containsDuplicate(nums))