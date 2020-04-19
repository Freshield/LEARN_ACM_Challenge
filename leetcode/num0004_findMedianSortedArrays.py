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


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2, 4]
    # nums1 = [1,2]
    # nums2 = [i+1 for i in range(10)]
    # test = [0,1,2,3,4,5,6,7]
    print(findMedianSortedArrays(nums1, nums2))
