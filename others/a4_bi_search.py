# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_bi_search.py
@Time: 2020-04-15 21:39
@Last_update: 2020-04-15 21:39
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def bi_search(num_list, target):
    """
    二分查找
    整体流程：
    1. 得到中间的索引
    2. 如果中间的值为target则返回True
    3. 如果中间的值小于target则把l移动到mid+1
    4. 如果中间的值大于target则把r移动到mid
    5. 如果r-l==1，则到了最后，判断r,l是否等于target
    """
    left = 0
    right = len(num_list) - 1
    while True:
        # 1. 得到中间的索引
        mid = (right + left) // 2
        mid_value = num_list[mid]
        # 2. 如果中间的值为target则返回True
        if mid_value == target:
            return True
        # 3. 如果中间的值小于target则把l移动到mid+1
        elif mid_value < target:
            left = mid + 1
        # 4. 如果中间的值大于target则把r移动到mid
        elif mid_value > target:
            right = mid

        # 5. 如果r-l==1，则到了最后，判断r,l是否等于target
        if right - left == 1:
            return (num_list[right] == target) or (num_list[left] == target)


if __name__ == '__main__':
    num_list = list(range(21))
    num_list.sort()
    for i in range(22):
        print(bi_search(num_list, i))