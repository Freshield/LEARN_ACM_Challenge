#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0011_maxArea.py
@Time: 2020-04-20 15:02
@Last_update: 2020-04-20 15:02
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
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
    在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    说明：你不能倾斜容器，且 n 的值至少为 2。
    解法：
    使用双指针，移动短的那边知道指针相等。原理是无论如何移动长侧得到的结果只会减少，
    因为高度只可能相等或减少，而宽度会减少
    """
    def maxArea(self, height):
        """
        整体流程：
        1. 生成双指针和最大面积
        2. 遍历，结束条件为左小于右
        3. 生成当前面积并和最大面积比较
        4. 移动短侧
        """
        # 1. 生成双指针和最大面积
        left = 0
        right = len(height) - 1
        max_area = -1
        # 2. 遍历，结束条件为左小于右
        while left < right:
            # 3. 生成当前面积并和最大面积比较
            width = right - left
            area = width * min(height[left], height[right])
            if area > max_area:
                max_area = area
            else:
                max_area = max_area

            # 4. 移动短侧
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))