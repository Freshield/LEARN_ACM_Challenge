#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a0_paper_number.py
@Time: 2020-04-13 15:20
@Last_update: 2020-04-13 15:20
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def binary_search_iter(search_list, target):
    """
    二分查找
    整体流程：
    1. 找到中心的值
    2. 如果等于target则返回True
    3. 如果小于target则移动l到当前位置，递归后边
    4. 如果大于target则移动r到当前位置，递归前边
    5. 如果l等于r则返回False
    """
    l = 0
    r = len(search_list)
    # 5. 如果l等于r则返回False
    if l == r:
        return False
    # 1. 找到中心的值
    mid = (r - l) // 2

    # 2. 如果等于target则返回
    if search_list[mid] == target:
        return True
    # 3. 如果小于target则移动l到当前位置，递归后边
    elif search_list[mid] < target:
        return binary_search_iter(search_list[mid+1: r], target)
    # 4. 如果大于target则移动r到当前位置，递归前边
    elif search_list[mid] > target:
        return binary_search_iter(search_list[l: mid], target)

    return False


def binary_search(search_list, target):
    """
    二分查找
    整体流程：
    0. 检查边界值
    1. 得到中心值
    2. 如果等于target则返回True
    3. 如果小于target则移动l到当前加1
    4. 如果大于target则移动r到当前
    5. 如果l和r只差一个则代表中间没有值了，返回False
    """
    l = 0
    r = len(search_list)

    while r - l > 1:
        # 1. 得到中心值
        mid = (r + l) // 2

        # 2. 如果等于target则返回True
        # 0. 检查边界值
        if (search_list[mid] == target) or (search_list[l] == target) or (search_list[r-1] == target):
            return True
        # 3. 如果小于target则移动l到当前
        elif search_list[mid] < target:
            l = mid+1
        # 4. 如果大于target则移动r到当前
        elif search_list[mid] > target:
            r = mid

    return False


def paper_number(n, m, paper_number_list):
    """
    计算paper_number_list中的数抽4次是否可能和为m
    解法：
    m = k1 + k2 + k3 + k4
    k3 + k4 = m - k1 - k2
    整体流程：
    1. 计算所有k3+k4的和
    2. 遍历k1,k2
    3. 用二分查找看是否能找到k3+k4=m-k1-k2
    """
    # 1. 计算所有k3+k4的和
    k3k4 = []
    for k3 in paper_number_list:
        for k4 in paper_number_list:
            k3k4.append(k3 + k4)

    k3k4.sort()

    # 2. 遍历k1,k2
    for k1 in paper_number_list:
        for k2 in paper_number_list:
            # 3. 用二分查找看是否能找到k3+k4=m-k1-k2
            if binary_search_iter(k3k4, m-k1-k2):
                return True

    return False


if __name__ == '__main__':
    m = 9
    paper_number_list = [1,3,5]
    result = paper_number(len(paper_number_list), m, paper_number_list)
    print(result)
    # for i in range(10):
    #     print(binary_search(list(range(10)), i))
    # print(binary_search(list(range(10)), 3))