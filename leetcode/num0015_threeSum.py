# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0015_threeSum.py
@Time: 2020-04-19 00:15
@Last_update: 2020-04-19 00:15
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
    def threeSum(self, nums):
        """
        给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
        注意：答案中不可以包含重复的三元组。
        解法：
        使用双指针的方法，首先对数组排序，先固定第一个数，这个数从左向右开始遍历，
        如果当前数已经大于0则再也不会三数和为0，则退出，同时如果和上一个值一样则跳过
        固定第一个数后，分别双指针从左和右往中间夹，
        结束条件：当L和R相等时则退出
        如果sum大于0则R右移，小于0则左移，等于0则放入并continue
        整体流程：
        1. 对数组排序
        2. 遍历第一个值a
        3. 如果a>0则break，上一个值相同则continue
        4. 遍历查找L,R, 如果L==R则break
        5. 找到相同值的L，R的最后一个和第一个
        6. 如果等于0则存储并移动L，R
        7. 如果小于0则左移L
        8. 如果大于0则右移R
        """
        # 1. 对数组排序
        nums.sort()
        rst_list = []
        # 2. 遍历第一个值a
        for a in range(len(nums)-2):
            # 3. 如果a>0则break，上一个值相同则continue
            if nums[a] > 0:
                break

            if (a > 0) and (nums[a] == nums[a-1]):
                continue

            # 4. 遍历查找L,R, 如果L==R则break
            L = a + 1
            R = len(nums) - 1
            while True:
                if L >= R:
                    break

                # 6. 如果等于0则存储并
                sum = nums[a] + nums[L] + nums[R]
                # 6. 如果等于0则存储并移动L，R
                if sum == 0:
                    rst_list.append([nums[a], nums[L], nums[R]])
                    while True:
                        if (L+1<R) and (nums[L+1] == nums[L]):
                            L += 1
                        else:
                            break
                    while True:
                        if (R-1 > L) and (nums[R-1] == nums[R]):
                            R -= 1
                        else:
                            break
                    L += 1
                    R -= 1
                # 7. 如果小于0则左移L
                elif sum < 0:
                    L += 1
                else:
                    R -= 1

        return rst_list




if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    nums = [0,0,0]
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print(Solution().threeSum(nums))