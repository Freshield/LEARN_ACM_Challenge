# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0016_threeSumClosest.py
@Time: 2020-06-15 10:20
@Last_update: 2020-06-15 10:20
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
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。
    解法：
    双指针法
    先对nums进行排序
    然后遍历nums寻找target-num
    如果num大于target则直接break
    双指针为i+1到最后一个值
    如果当前和大于target则移动右指针
    如果当前和小于target则记录并移动左指针
    如果左右指向为同一个则退出，并和全局最大进行比较
    """
    def threeSumClosest(self, nums, target):
        """
        整体流程：
        1. 对nums进行排序
        2. 处理特殊情况
        3. 生成左右指针等中间数值
        4. 对num进行遍历
        5. 如果大于target则直接break
        6. 如果和大于target则移动右指针
        7. 如果和小于target则移动左指针并记录
        8. 如果左右相等则退出
        """
        # 1. 对nums进行排序
        nums.sort()

        # 2. 处理特殊情况
        if len(nums) == 0:
            return -1

        # 3. 生成左右指针等中间数值
        rst_val = float('-inf')

        # 4. 对num进行遍历
        for i in range(len(nums) - 2):
            num = nums[i]
            tmp_sum = float('-inf')

            left = i + 1
            right = len(nums) - 1
            while not (left == right):
                sum = num + nums[left] + nums[right]
                if sum == target:
                    return target
                # 6. 如果和大于target则移动右指针
                elif sum > target:
                    tmp_sum = sum if abs(target-sum) < abs(target-tmp_sum) else tmp_sum
                    right -= 1
                # 7. 如果和小于target则移动左指针并记录
                else:
                    tmp_sum = sum if abs(target - sum) < abs(target - tmp_sum) else tmp_sum
                    left += 1

            rst_val = tmp_sum if abs(target-tmp_sum) < abs(target-rst_val) else rst_val

        return rst_val


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    nums = [0, 1, 2]
    target = 0
    print(Solution().threeSumClosest(nums, target))