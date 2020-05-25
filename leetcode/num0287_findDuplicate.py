# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0287_findDuplicate.py
@Time: 2020-05-24 11:46
@Last_update: 2020-05-24 11:46
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
    给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
    可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
    解法：
    二分查找，找到1到n中间的数mid，遍历数组，
    如果等于mid大于一个则返回
    如果大于等于mid的数小于等于n-mid+1则在区间1到mid-1中查找
    否则再mid+1到n中间查找
    """
    def search_nums(self, nums, target):
        equal = 0
        bigger = 0
        for num in nums:
            if num == target:
                equal += 1
            elif num > target:
                bigger += 1

        return equal, bigger

    def findDuplicate(self, nums):
        """
        整体流程：
        1. 生成左右指针
        2. 得到mid
        3. 遍历数组进行计数
        4. 如果等于mid大于一个则返回mid
        5. 如果总计数大于等于mid的数小于等于n-mid+1则right=mid-1
        6. 否则left=mid+1
        """
        if len(nums) <= 1:
            return nums

        # 1. 生成左右指针
        left = 1
        right = len(nums) - 1

        while left <= right:
            # 2. 得到mid
            mid = left + (right - left) // 2
            # 3. 遍历数组进行计数
            equal, bigger = self.search_nums(nums, mid)
            # 4. 如果等于mid大于一个则返回mid
            if equal > 1:
                return mid
            # 5. 如果总计数大于等于mid的数小于等于n-mid+1则right=mid-1
            total = equal + bigger
            threshold = len(nums) - 1 - mid + 1
            if total <= threshold:
                right = mid - 1
            else:
                left = mid + 1



if __name__ == '__main__':
    nums = [1,3,4,2,2]
    nums = [3,1,3,4,2]
    print(Solution().findDuplicate(nums))