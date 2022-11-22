# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a165_catch_rainfall.py
@Time: 2022-11-16 13:43
@Last_update: 2022-11-16 13:43
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def catch_rainfall(in_height):
    """
    接雨水，使用单调栈
    1. 创建单调栈，雨水量
    2. 遍历，从1到in height的长度
    3. 情况一，当前的值小于单调栈顶，入栈
    4. 情况二，当前的值等于单调栈顶，跳过
    5. 情况三，当前的值大于单调栈顶
    6. 遍历，条件为单调栈不为空，且当前的值大于单调栈顶
    7. 弹出栈顶，并获取相应的值
    8. 如果当前单调栈为空，则break
    9. 获取当前的栈顶
    10. 长为当前栈顶和当前值小的那个值减去弹出的高度值，宽为当前值减去栈顶，雨水量累加
    11. 最后，把当前值入栈
    """
    # 1. 创建单调栈，雨水量
    single_stack, res_rain = [0], 0
    # 2. 遍历，从1到in height的长度
    for i in range(1, len(in_height)):
        this_value = in_height[i]
        top_index = single_stack[-1]
        top_value = in_height[top_index]
        # 3. 情况一，当前的值小于单调栈顶，入栈
        if this_value < top_value:
            single_stack.append(i)
            continue
        # 4. 情况二，当前的值等于单调栈顶，跳过
        elif this_value == top_value:
            single_stack.append(i)
            continue
        # 5. 情况三，当前的值大于单调栈顶
        # 6. 遍历，条件为单调栈不为空，且当前的值大于单调栈顶
        while (len(single_stack) != 0) and (this_value > in_height[single_stack[-1]]):
            # 7. 弹出栈顶，并获取相应的值
            top_index = single_stack.pop()
            top_value = in_height[top_index]
            # 8. 如果当前单调栈为空，则break
            if len(single_stack) == 0:
                break
            # 9. 获取当前的栈顶
            new_top_index = single_stack[-1]
            new_top_value = in_height[new_top_index]
            # 10. 长为当前栈顶和当前值小的那个值减去弹出的高度值，宽为当前值减去栈顶，雨水量累加
            height = min(this_value, new_top_value) - top_value
            weight = i - new_top_index - 1
            res_rain += height * weight
        # 11. 最后，把当前值入栈
        single_stack.append(i)

    return res_rain


if __name__ == '__main__':
    in_height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    in_height = [4, 2, 0, 3, 2, 5]
    in_height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
    print(catch_rainfall(in_height))
