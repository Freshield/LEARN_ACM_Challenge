#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0042_trap.py
@Time: 2020-04-27 16:59
@Last_update: 2020-04-27 16:59
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
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    解法：
    一. 分层方法，遍历数组，找到第一个不为0且下一个为0的位置为left，找到第一个为0且下一个不为0的为right
    二. 单调栈发，遍历数组，持续放元素到栈中，如果遇到比自己小的就开始计算水
    三. 双指针法，左右夹逼，记录最大值，找到都大于最大值的地方，比较左右进行计算，最后减去所有柱体
    """
    def trap(self, height):
        """
        整体流程：
        1. 生成最大值，左右指针等变量
        2. 得到两边的最大值
        3. 得到当前的最大值
        4. 如果左边小于最大值一直移动左边的指针直到大于最大值
        5. 如果右边小于最大值一直移动右边指针直到大于最大值
        6. 结束条件：左指针等于右指针
        """
        if len(height) < 3:
            return 0
        # 1. 生成最大值，左右指针等变量
        left = 0
        left_max = height[0]
        right = len(height) - 1
        right_max = height[right]
        rst = 0
        # 2. 得到两边的最大值
        max_val = max(left_max, right_max)
        while True:
            # 6. 结束条件：左指针等于右指针
            if left == right:
                break
            # 4. 如果左边小于最大值一直移动左边的指针直到大于最大值
            while left_max < max_val:
                rst += left_max - height[left]
                left += 1
                left_max = left_max if height[left] <= left_max else height[left]
            # 5. 如果右边小于最大值一直移动右边指针直到大于最大值
            while right_max < max_val:
                rst += right_max - height[right]
                right -= 1
                right_max = right_max if height[right] <= right_max else height[right]

            # 3. 得到当前的最大值
            while left_max <= max_val:
                if left == right:
                    break
                rst += left_max - height[left]
                left += 1
                left_max = left_max if height[left] <= left_max else height[left]

            max_val = left_max

        return rst



    def trap_stack(self, height):
        if len(height) < 3:
            return 0

        stack = []
        ans = 0
        for i in range(len(height)):
            while True:
                if len(stack) == 0:
                    stack.append((i, height[i]))
                    break
                if height[i] == stack[-1][1]:
                    stack.pop(-1)
                    stack.append((i, height[i]))
                    break
                if height[i] < stack[-1][1]:
                    stack.append((i, height[i]))
                    break

                cur = stack.pop(-1)

                if len(stack)>0:
                    stackTop = stack[-1]
                    #stackTop此时指向的是此次接住的雨水的左边界的位置。右边界是当前的柱体，即i。
                    #Math.min(height[stackTop], height[i]) 是左右柱子高度的min，减去height[curIdx]就是雨水的高度。
                    #i - stackTop - 1 是雨水的宽度。
                    rst = (min(stackTop[1], height[i]) - cur[1]) * (i - stackTop[0] - 1)
                    ans += rst
                else:
                    stack.append((i, height[i]))
                    break



        return ans



    def trap_left_right(self, height):
        """
        整体流程：
        1. 生成左右指针和中间变量
        2. 遍历位置搜索left，搜索同时让数组数值减1，并大于0
        3. 找到left后，开始从下一个位置开始找right
        4. 如果right已经到数组尾则置零left，right
        5. 如果本次全部找完后没有水则退出
        """
        if len(height) < 3:
            return 0
        # 1. 生成左右指针和中间变量
        left = 1
        sum = 0
        height.insert(0, 0)
        height.append(0)
        # 2. 遍历位置搜索left，搜索同时让数组数值减1，并大于0
        while True:
            if left >= (len(height) - 2):
                break
            if not ((height[left] >= height[left - 1]) and (height[left] > height[left + 1])):
                left += 1
                continue
            # 3. 找到left后，开始从下一个位置开始找right
            right = left + 1
            for right in range(left + 1, len(height) - 1):
                if not ((height[right] > height[right - 1]) and
                        (height[right] >= height[right + 1])):
                    right += 1
                else:
                    h = min(height[left], height[right])
                    for i in range(left, right + 1):
                        sum += max(0, h - height[i])
                        if height[i] < h:
                            height[i] = h
                    if height[right] >= height[left]:
                        break

            if right >= (len(height) - 1):
                left += 1
                continue

            left = right


        return sum


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [0]
    # height = [0,2,0]
    # height = [2,0,2]
    # height = [4,2,3]
    # height = [5, 2, 1, 2, 1, 5]
    # height = [4, 2, 0, 3, 2, 5]
    rst_val = Solution().trap(height)
    print(rst_val)
