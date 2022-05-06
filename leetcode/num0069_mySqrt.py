# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0069_mySqrt.py
@Time: 2020-06-11 10:34
@Last_update: 2020-06-11 10:34
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
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
    解法：
    1. 使用二分查找，比较平方和x是否小
    """
    def mySqrt(self, x):
        """
        整体流程：
        1. 生成左右指针
        2. 遍历左右
        3. 如果中间的数的平方等于x则直接返回
        4. 如果中间的数小于x则ans为mid并且l = mid + 1
        5. 如果中间的数大于x则r = mid - 1
        """
        # 1. 生成左右指针
        left, right, ans = 0, x, -1

        # 2. 遍历左右
        while left <= right:
            mid = left + (right - left) // 2
            square = mid ** 2
            # 3. 如果中间的数的平方等于x则直接返回
            if square == x:
                ans = mid
                break
            # 4. 如果中间的数小于x则ans为mid并且l = mid + 1
            elif square < x:
                ans = mid
                left = mid + 1
            # 5. 如果中间的数大于x则r = mid - 1
            else:
                right = mid - 1

        return ans


if __name__ == '__main__':
    x = 4
    x = 8
    x = 9
    print(Solution().mySqrt(x))