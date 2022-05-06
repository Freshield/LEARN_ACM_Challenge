# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0169_majorityElement.py
@Time: 2020-04-19 22:45
@Last_update: 2020-04-19 22:45
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
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    """
    def majorityElement(self, nums):
        """
        使用摩尔投票法
        整体流程：
        1. 生成投票变量
        2. 遍历num计票
        """
        # 1. 生成投票变量
        majority = None
        count = 0
        # 2. 遍历num计票
        for num in nums:
            if count == 0:
                majority = num
                count += 1
            else:
                if majority == num:
                    count += 1
                else:
                    count -= 1

        return majority

    def majorityElement_dict(self, nums):
        """
        使用字典的方法存储并计算个数
        整体流程：
        1. 遍历nums
        2. 存储到字典中
        3. 如果当前的数量大于一半，则直接返回
        """
        num_dict = dict()
        half = len(nums) // 2
        # 1. 遍历nums
        for num in nums:
            # 2. 存储到字典中
            num_dict[num] = num_dict.get(num, 0) + 1
            # 3. 如果当前的数量大于一半，则直接返回
            if num_dict[num] > half:
                return num


if __name__ == '__main__':
    # nums = [3, 2, 3]
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement_dict(nums))