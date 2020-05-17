# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0088_merge.py
@Time: 2020-05-20 09:58
@Last_update: 2020-05-20 09:58
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
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
    说明:
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    """
    def merge(self, nums1, m, nums2, n):
        """
        从后边遍历添加
        1. 创建双指针和尾指针
        2. 结束条件为双指针其一小于0
        3. 如果up指针指向的值大于等于down指针指向的值则尾指针填入up的值
        4. 如果up指针指向的值小于down指针指向的值则尾指针填入down的值
        """
        if m == 0:
            nums1[:] = nums2[:]
            return nums1
        elif n == 0:
            return nums1
        # 1. 创建双指针和尾指针
        tail = len(nums1) - 1
        up = m-1
        down = n-1

        # 2. 结束条件为双指针其一小于0
        while True:
            if (up < 0) or (down < 0):
                break

            # 3. 如果up指针指向的值大于等于down指针指向的值则尾指针填入up的值
            if nums1[up] >= nums2[down]:
                nums1[tail] = nums1[up]
                tail -= 1
                up -= 1
            # 4. 如果up指针指向的值小于down指针指向的值则尾指针填入down的值
            else:
                nums1[tail] = nums2[down]
                tail -= 1
                down -= 1

        if down >= 0:
            for i in range(down+1):
                nums1[i] = nums2[i]

    def merge_positive(self, nums1, m, nums2, n):
        """
        整体流程：
        1. 创建双指针
        2. 结束条件为down指针等于n,或者up指针等于m
        3. 如果up指针的数值小于等于down指针的数值则up指针后移
        4. 如果up指针的数值大于down指针的数值则把down指针插入
        5. 如果down指针不等于n则把剩下的添加到num1
        """
        if m == 0:
            nums1[:] = nums2[:]
            return nums1
        elif n == 0:
            return nums1
        # 1. 创建双指针
        for i in range(len(nums1)-m):
            nums1.pop()
        up = 0
        down = 0

        # 2. 结束条件为down指针等于n,或者up指针等于m
        while True:
            # 2. 结束条件为down指针等于n,或者up指针等于m
            if (down == n) or (up == len(nums1)):
                break
            # 3. 如果up指针的数值小于等于down指针的数值则up指针后移
            if nums1[up] <= nums2[down]:
                up += 1
            # 4. 如果up指针的数值大于down指针的数值则把down指针插入
            else:
                nums1.insert(up, nums2[down])
                up += 1
                down += 1

        # 5. 如果down指针不等于n则把剩下的添加到num1
        if down != n:
            nums1 += nums2[down:]


if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1
    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    Solution().merge(nums1, m, nums2, n)
    print(nums1)