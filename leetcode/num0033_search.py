#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0033_search.py
@Time: 2020-04-20 10:04
@Last_update: 2020-04-20 10:04
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
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。
    """
    def search(self, nums, target):
        """
        通过二分查找来进行搜索，需要注意的是和普通的二分查找不同
        这里还需要判断当前部分是正序还是反序的
        整体流程：
        1. 生成需要的变量
        2. 结束条件为左边大于等于右边
        3. 得到中心位置
        4. 判断三个位置是否为target
        5. 判断哪边为正序
        6. 判断target是否在正序一侧
        """
        # 1. 生成需要的变量
        left = 0
        right = len(nums) - 1
        
        # 2. 结束条件为左边大于等于右边
        while left <= right:
            # 3. 得到中心位置
            mid = (left + right) // 2
            # 4. 判断三个位置是否为target
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            
            # 5. 判断哪边为正序
            # 左边正序
            if nums[left] < nums[mid]:
                # 6. 判断target是否在正序一侧
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右边正序
            else:
                # 6. 判断target是否在正序一侧
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

            


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 3
    print(Solution().search(nums, target))