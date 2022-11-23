# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a166_largest_rectangle_area.py
@Time: 2022-11-17 13:29
@Last_update: 2022-11-17 13:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def largest_rectangle_area(heights):
    """
    求柱状图中矩形的最大面积，单调栈
    1. 创建单调栈以及面积数值，增加前后的0区域方便最终的相应计算
    2. 遍历，从1到heights的长度
    3. 情况一，如果当前的数值大于栈顶，则入栈，continue
    4. 情况二，如果当前的数值等于栈顶，则直接跳过，continue
    5. 情况三，如果当前的数值小于栈顶
    6. 遍历，条件为单独栈不为空，且当前的数值小于栈顶
    7. 弹出，获取为top value
    8. 获取当前的栈顶，next top value
    9. 计算当前矩形高度为高，当前i到next top index为宽的矩形面积
    10. 最后把当前的i入栈
    """
    # 1. 创建单调栈以及面积数值，增加前后的0区域方便最终的相应计算
    single_stack, max_area = [0], 0
    heights = [0] + heights + [0]
    # 2. 遍历，从1到heights的长度
    for i in range(1, len(heights)):
        this_value = heights[i]
        top_index, top_value = single_stack[-1], heights[single_stack[-1]]
        # 3. 情况一，如果当前的数值大于栈顶，则入栈，continue
        if this_value > top_value:
            single_stack.append(i)
            continue
        # 4. 情况二，如果当前的数值等于栈顶，则直接跳过，continue
        elif this_value == top_value:
            single_stack.append(i)
            continue
        # 5. 情况三，如果当前的数值小于栈顶
        # 6. 遍历，条件为单独栈不为空，且当前的数值小于栈顶
        while (len(single_stack) != 0) and (this_value < heights[single_stack[-1]]):
            # 7. 弹出，获取为top value
            top_index = single_stack.pop()
            top_value = heights[top_index]
            # 8. 获取当前的栈顶，next top value
            next_top_index = single_stack[-1]
            next_top_value = heights[next_top_index]
            # 9. 计算当前矩形高度为高，当前i到next top index为宽的矩形面积
            this_area = top_value * (i - next_top_index - 1)
            max_area = max(max_area, this_area)
        # 10. 最后把当前的i入栈
        single_stack.append(i)

    return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    heights = [0, 9]
    print(largest_rectangle_area(heights))
