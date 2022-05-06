# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0004_findMedianSortedArrays.py
@Time: 2020-04-18 21:06
@Last_update: 2020-04-18 21:06
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import heapq


def get_Kth_num(nums1, start1, end1, nums2, start2, end2, K):
    """
    找到第K个大小的数
    整体流程：
    1. 得到nums1，nums2的长度
    2. 如果nums2 < nums1 则返回num2在前的，保证前边的小于等于第二个
    3. 如果nums1为空，则直接返回nums2的第K个值
    4. 得到各自第K/2的索引，注意大于数组长度的情况
    5. 判断相应索引的大小，递归调用
    """
    # 1. 得到nums1，nums2的长度
    len1 = end1 - start1 + 1
    len2 = end2 - start2 + 1
    # 2. 如果nums2 < nums1 则返回num2在前的，保证前边的小于等于第二个
    if len2 < len1:
        return get_Kth_num(nums2, start2, end2, nums1, start1, end1, K)

    # 3. 如果nums1为空，则直接返回nums2的第K个值
    if start1 > end1:
        return nums2[start2 + K - 1]

    if K == 1:
        return min(nums1[start1 + K - 1], nums2[start2 + K - 1])

    # 4. 得到各自第K/2的索引，注意大于数组长度的情况
    index1 = start1 + min(len1, K//2) - 1
    index2 = start2 + min(len2, K//2) - 1

    # 5. 判断相应索引的大小，递归调用
    if nums1[index1] > nums2[index2]:
        return get_Kth_num(nums1, start1, end1, nums2, index2+1, end2, K - (index2-start2+1))
    else:
        return get_Kth_num(nums1, index1+1, end1, nums2, start2, end2, K - (index1-start1+1))


def findMedianSortedArrays(nums1, nums2):
    """
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
    解法：
    使用二分查找，相当于要对两个数组查找总体的第K个数，
    分别对两个数组找到第K/2的位置的数进行比较，小的那个数的前K/2个数肯定小于第K个数，以此反复
    注意特殊情况，数组可能会被选择完，要是一个数组为空则只需要从第二个数组选择第K个数即可
    同时也要注意奇数偶数的问题，一个中位数为数，另一个为均值
    整体流程：
    1. 判断数组的奇偶分别返回数字和均值
    """
    # 1. 判断数组的奇偶分别返回数字和均值
    m = len(nums1)
    n = len(nums2)
    total_len = m + n
    # 偶数
    if total_len % 2 == 0:
        left = get_Kth_num(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (total_len+1)//2)
        right = get_Kth_num(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (total_len+2)//2)
        return (left + right) / 2
    else:
        return get_Kth_num(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (total_len+1)//2)

class Solution:
    """
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空
    解法：
    使用遍历数组的方法，上下一直走步，遍历到哪个值小就哪边再走一步，一共走(m+n)//2步
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        整体流程：
        1. 生成中间变量
        2. 遍历走步
        3. 遍历条件i<m and j<n and (i+j)<(m+n+2)//2
        4. 判断大小并放到堆中
        5. 判断剩余的值
        6. 根据长短返回
        """
        # 1. 生成中间变量
        heap = []
        i = 0
        j = 0
        step = 0

        if len(nums1) == 0:
            nums1 = nums2
        elif len(nums2) == 0:
            nums2 = nums1

        if (len(nums1) == 1) and (len(nums2) == 1):
            return (nums1[0] + nums2[0]) / 2


        m = len(nums1)
        n = len(nums2)
        mid = ((m+n) // 2) + 1

        # 2. 遍历走步
        # 3. 遍历条件i<m and j<n and (i+j)<(m+n)//2
        while True:
            # 4. 判断大小并放到堆中
            if nums1[i] < nums2[j]:
                heapq.heappush(heap, nums1[i])
                i += 1
            else:
                heapq.heappush(heap, nums2[j])
                j += 1

            if len(heap) > 2:
                heapq.heappop(heap)
            step += 1
            if (i==m) or (j==n) or (step == mid):
                break

        # 5. 判断剩余的值
        # 如果相等
        if (step < mid) and (i == m):
            while True:
                heapq.heappush(heap, nums2[j])
                j += 1
                if len(heap) > 2:
                    heapq.heappop(heap)
                step += 1
                if step == mid:
                    break
        elif (step < mid) and (j == n):
            while True:
                heapq.heappush(heap, nums1[i])
                i += 1
                if len(heap) > 2:
                    heapq.heappop(heap)
                step += 1
                if step == mid:
                    break

        # 6. 根据长短返回
        if (m+n) % 2 == 1:
            heapq.heappop(heap)
            return heapq.heappop(heap)
        else:
            rst = heapq.heappop(heap)
            return (rst + heapq.heappop(heap)) / 2






if __name__ == '__main__':
    # nums1 = [1]
    # nums2 = [2,3]
    # (1+2)//2 = 1
    # nums1 = [1, 3]
    # nums2 = [2, 4]
    #(2+2)//2 = 2
    # nums1 = [1,2,2,2.5]
    # nums2 = [i+1 for i in range(6)]
    # test = [1,2,3,4,5,6]
    # nums1 = [1, 1, 3, 3]
    # nums2 = [1, 1, 3, 3]
    nums1 = []
    nums2 = [1]
    # print(findMedianSortedArrays(nums1, nums2))
    print(Solution().findMedianSortedArrays(nums1, nums2))
