# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_sequence_square_list_r.py
@Time: 2022-09-01 22:57
@Last_update: 2022-09-01 22:57
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def sequance_square_list(nums):
    """
    返回有序的平方值列表
    使用双指针方法，头和尾进行比较，将大的push进去
    1. 创建需要的变量
    2. 遍历直到left大于right
    3. 得到左右的平方值
    4. 如果左边大则放入左值并加一
    5. 如果右边大则放入右值并减一
    """
    # 1. 创建需要的变量
    square_list, left_p, right_p = [], 0, len(nums)-1
    # 2. 遍历直到left大于right
    while left_p <= right_p:
        # 3. 得到左右的平方值
        left_v, right_v = nums[left_p] ** 2, nums[right_p] ** 2
        # 4. 如果左边大则放入左值并加一
        if left_v > right_v:
            square_list.insert(0, left_v)
            left_p += 1
        else:
            square_list.insert(0, right_v)
            right_p -= 1

    return square_list


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sequance_square_list(nums))
