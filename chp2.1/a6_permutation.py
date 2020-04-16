#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_permutation.py
@Time: 2020-04-14 15:02
@Last_update: 2020-04-14 15:02
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def permutation(pos, permutation_list, used_list=None, value_list=None):
    """
    生成所有的排列方法
    解法：递归位置，如果还没使用过则继续递归直到全部都使用
    重点在于区分pos和i的意义，一个是当前的位置，一个是遍历的值的位置
    整体流程：
    1. 生成一样大小的是否使用的列表
    2. 终止条件pos等于pernmutation_list长度代表完成一次排列
    3. 3. 遍历当前pos的所有可能, i代表遍历的值, pos代表设置的位置
    4. 如果当前pos对应的值没有使用则继续查找下一个
    """
    # 1. 生成一样大小的是否使用的列表
    used_list = [False] * len(permutation_list) if used_list is None else used_list
    value_list = [-1] * len(permutation_list) if value_list is None else value_list

    # 2. 终止条件pos等于pernmutation_list长度代表完成一次排列
    if pos == len(permutation_list):
        print(value_list)

    # 3. 遍历当前pos的所有可能, i代表遍历的位置, pos代表当前的位置
    for i in range(len(permutation_list)):
        # 4. 如果当前pos对应的值没有使用则继续查找下一个
        if used_list[i] is False:
            used_list[i] = True
            value_list[pos] = permutation_list[i]
            permutation(pos + 1, permutation_list, used_list, value_list)
            used_list[i] = False
            value_list[pos] = -1


if __name__ == '__main__':
    permutation_list = list(range(3))
    permutation(0, permutation_list)