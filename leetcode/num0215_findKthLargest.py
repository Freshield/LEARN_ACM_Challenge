# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0215_findKthLargest.py
@Time: 2020-04-19 20:47
@Last_update: 2020-04-19 20:47
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


class Solution:
    """
    在未排序的数组中找到第 k 个最大的元素。
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    """

    def findKthLargest(self, nums, k):
        """
        使用快速选择的方法找寻
        解法：
        第k最大元素就是第N-k的最小元素
        随机找到一个位置，然后通过快速选择方法，把该位置数字放到相应的位置上
        再和k做比较，递归
        """
        return self.select(nums, 0, len(nums)-1, len(nums)-k)

    def select(self, nums, left, right, k_smallest):
        """
        整体流程：
        1. 边界条件：left == right时返回nums[left]
        2. 随机选择一个序号
        3. 按照这个序号重新排列nums
        4. 判别和k_smallest的关系，递归
        """
        # 1. 边界条件：left == right时返回nums[left]
        if left == right:
            return nums[left]

        # 2. 随机选择一个序号
        parti_index = (left + right) // 2

        # 3. 按照这个序号重新排列nums
        nums, parti_index = self.partition(nums, left, right, parti_index)

        # 4. 判别和k_smallest的关系，递归
        if k_smallest == parti_index:
            return nums[k_smallest]
        elif k_smallest < parti_index:
            return self.select(nums, left, parti_index-1, k_smallest)
        else:
            return self.select(nums, parti_index+1, right, k_smallest)


    def partition(self, nums, left, right, parti_index):
        """
        重新规划数组，让pari_index位置的数放到相应位置
        并且这个位置的左边都比它小，右边都比它大
        整体流程：
        1. 把parti_index的数和right调换，方便选择
        2. 遍历left到right-1
        3. 如果当前数值比pariti_value小，则把当前数值和rst_index调换
        4. 把rst_index和right进行调换
        """
        parti_value = nums[parti_index]
        # 1. 把parti_index的数和right调换，方便选择
        nums[parti_index], nums[right] = nums[right], nums[parti_index]
        rst_index = left
        # 2. 遍历left到right-1
        for i in range(left, right):
            # 3. 如果当前数值比pariti_value小，则把当前数值和rst_index调换
            if nums[i] < parti_value:
                nums[i], nums[rst_index] = nums[rst_index], nums[i]
                rst_index += 1
        # 4. 把rst_index和right进行调换
        nums[rst_index], nums[right] = nums[right], nums[rst_index]

        return nums, rst_index

    def findKthLargest_heap(self, nums, k):
        """
        解法：
        使用数据结构中的堆，这样循环放入，然后超过K则pop出来，最后顶上的为第K大的
        整体流程：
        1. 遍历列表
        2. 放入元素
        3. 如果超过k则pop
        4. 返回顶上元素
        """
        heap = []
        # 1. 遍历列表
        for num in nums:
            # 2. 放入元素
            heapq.heappush(heap, num)

            # 3. 如果超过k则pop
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))