#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a31_sort_algorithms.py
@Time: 2020-04-29 16:19
@Last_update: 2020-04-29 16:19
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from random import randint


def generateRandomArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]

    return arr


def isSorted(alist):
    for i in range(len(alist)-1):
        if alist[i] > alist[i+1]:
            return False

    return True


def bubbleSort(alist):
    """
    冒泡排序，两两比较，然后交换位置
    整体流程：
    1. 遍历结尾的位置
    2. 从头遍历到结尾的位置
    3. 比较左右然后交换
    """
    # 1. 遍历结尾的位置
    for i in range(len(alist)-1, 0, -1):
        exchange = False
        # 2. 从头遍历到结尾的位置
        for j in range(i):
            # 3. 比较左右然后交换
            if alist[j+1] < alist[j]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True

        if not exchange:
            break

    return alist


def quickSort(alist, l=0, r=None):
    """
    快排，使用随机轴，把左右分为比轴小和比轴大的两部分
    整体流程：
    1. 得到r的值，为最后一个元素的pos
    2. 如果l>=r则返回
    3. 随机确定轴
    4. 把轴和l进行调换
    5. 初始j，i的位置
    6. 遍历i到r
    7. 如果遇到小于轴的值的则把j加1,然后调换位置
    8. 最后调换j和l的位置
    9. 递归继续排序左右半边
    """
    # 1. 得到r的值，为最后一个元素的pos
    r = r if r is not None else (len(alist)-1)

    # 2. 如果l>=r则返回
    if l >= r:
        return None

    # 3. 随机确定轴
    pivot = randint(l, r)
    v = alist[pivot]

    # 4. 把轴和l进行调换
    alist[l], alist[pivot] = alist[pivot], alist[l]

    # 5. 初始j，i的位置
    j = l
    i = l + 1

    # 6. 遍历i到r
    while i <= r:
        # 7. 如果遇到小于轴的值的则把j加1,然后调换位置
        if alist[i] <= v:
            j += 1
            alist[j], alist[i] = alist[i], alist[j]

        i += 1

    # 8. 最后调换j和l的位置
    alist[l], alist[j] = alist[j], alist[l]

    # 9. 递归继续排序左右半边
    quickSort(alist, l, j-1)
    quickSort(alist, j+1, r)




if __name__ == '__main__':
    alist = generateRandomArray(10, 0, 100)
    print(alist)
    # bubbleSort(alist)
    quickSort(alist)
    print(alist)