# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0075_sortColors.py
@Time: 2020-07-16 10:39
@Last_update: 2020-07-16 10:39
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
    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
    注意:
    不能使用代码库中的排序函数来解决这道题。
    解法：
    使用快排的partition思想
    使用zero,i,two三个遍历来分割整个区间
    1. 分区保证
        [0, zero)都为0
        [zero, i)都为1
        [two, len)都为2
    2. 初始化
        zero=0, i=0, two=len
    3. 交换流程
        i = 0, 交换zero和i的值，zero，i都加1
        i = 1, i加1
        i = 2, two减1, 交换i和two的值
    4. 结束条件
        i = two
    """
    def sortColors(self, nums):
        """
        整体流程：
        1. 进行特判
        2. 初始化变量
        3. 遍历i
        4. 进行数值交换
        """
        # 1. 进行特判
        if len(nums) < 2:
            return nums

        # 2. 初始化变量
        zero = i = 0
        two = len(nums)

        # 3. 遍历i
        while i < two:
            # 4. 进行数值交换
            # i = 0, 交换zero和i的值，zero，i都加1
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            # i = 1, i加1
            elif nums[i] == 1:
                i += 1
            # i = 2, two减1, 交换i和two的值
            else:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]

        return nums


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    print(Solution().sortColors(nums))