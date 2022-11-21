# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a164_loop_next_larger_element.py
@Time: 2022-11-15 21:43
@Last_update: 2022-11-15 21:43
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def loop_next_larger_element(nums):
    """
    循环数组中找到下一个更大的元素，使用单调栈
    1. 创建单调栈，结果列表
    2. 遍历，从1到长度为nums长度的两倍
    3. 使用i % len(nums)的方式来进行元素位置的获取
    4. 情况一，当前指代的值小于top指代的值，则入栈
    5. 情况二，当前指代的值等于top指代的值，则入栈
    6. 情况三，当前指代的值大于top指代的值
    7. 遍历，条件为单调栈不为空，且当前指代的值大于top指代的值
    8. 弹出top的位置，对应的位置res list设为当前的值
    9. 最后进行入栈
    """
    # 1. 创建单调栈，结果列表
    single_stack, res_list = [0], [-1] * len(nums)
    # 2. 遍历，从1到长度为nums长度的两倍
    for i in range(1, 2 * len(nums)):
        # 3. 使用i % len(nums)的方式来进行元素位置的获取
        index = i % len(nums)
        # 4. 情况一，当前指代的值小于top指代的值，则入栈
        if nums[index] < nums[single_stack[-1]]:
            single_stack.append(index)
            continue
        # 5. 情况二，当前指代的值等于top指代的值，则入栈
        elif nums[index] == nums[single_stack[-1]]:
            single_stack.append(index)
            continue
        # 6. 情况三，当前指代的值大于top指代的值
        # 7. 遍历，条件为单调栈不为空，且当前指代的值大于top指代的值
        while (len(single_stack) != 0) and (nums[index] > nums[single_stack[-1]]):
            # 8. 弹出top的位置，对应的位置res list设为当前的值
            top_index = single_stack.pop()
            res_list[top_index] = nums[index]
        # 9. 最后进行入栈
        single_stack.append(index)

    return res_list


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 3]
    nums = [1, 2, 1]
    print(loop_next_larger_element(nums))
