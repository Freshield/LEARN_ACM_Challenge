# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a163_next_larger_element.py
@Time: 2022-11-14 13:01
@Last_update: 2022-11-14 13:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def next_larger_element(nums1, nums2):
    """
    下一个更大的数，使用单调栈
    1. 创建单调栈，res list和nums1的哈希表
    2. 遍历从1到nums2的长度
    3. 情况一，如果当前的值小于栈顶索引的值，则入栈
    4. 情况二，如果当前的值等于栈顶索引的值，则入栈
    5. 情况三，如果当前的值大于栈顶索引的值
    6. 遍历，条件为栈不为空且当前的值大于栈顶索引的值
    7. 弹出栈顶的值
    8. 如果栈顶的值在哈希表中则把res list相应的值改为当前的值
    9. 最后，把当前的值入栈
    """
    # 1. 创建单调栈，res list和nums1的哈希表
    single_stack, res_list = [0], [-1] * len(nums1)
    nums1_dict = {value: i for i, value in enumerate(nums1)}
    # 2. 遍历从1到nums2的长度
    for i in range(1, len(nums2)):
        this_value = nums2[i]
        stack_top_value = nums2[single_stack[-1]]
        # 3. 情况一，如果当前的值小于栈顶索引的值，则入栈
        if this_value < stack_top_value:
            single_stack.append(i)
            continue
        # 4. 情况二，如果当前的值等于栈顶索引的值，则入栈
        elif this_value == stack_top_value:
            single_stack.append(i)
            continue
        # 5. 情况三，如果当前的值大于栈顶索引的值
        # 6. 遍历，条件为栈不为空且当前的值大于栈顶索引的值
        while (len(single_stack) != 0) and (this_value > nums2[single_stack[-1]]):
            # 7. 弹出栈顶的值
            stack_top_index = single_stack.pop()
            stack_top_value = nums2[stack_top_index]
            # 8. 如果栈顶的值在哈希表中则把res list相应的值改为当前的值
            if stack_top_value in nums1_dict:
                res_list[nums1_dict[stack_top_value]] = this_value
        # 9. 最后，把当前的值入栈
        single_stack.append(i)

    return res_list


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(next_larger_element(nums1, nums2))
