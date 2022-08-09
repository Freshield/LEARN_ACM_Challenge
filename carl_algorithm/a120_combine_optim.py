# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a120_combine_optim.py
@Time: 2022-10-17 21:11
@Last_update: 2022-10-17 21:11
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def combine(n, k):
    """
    组合问题，使用回溯
    1. 生成path列表，结果列表
    2. 运行回溯
    """
    path_list, res_list = [], []

    def backtrack(begin_index):
        """
        回溯递归部分
        1. 参数返回，begin_index
        2. 停止条件，当path列表长度为k时，把结果放到结果列表
        3. 回溯逻辑，从begin_index遍历到n+1，把i放入path列表，回溯递归，path列表弹出i
        4. 剪枝优化，当前path列表长度为p，还剩k-p个位置，遍历还剩n + 1 - i个数，
        如果n + 1 - i < k - p，表示以及没有足够的数来遍历，则可以直接停止
        """
        # 2. 停止条件，当path列表长度为k时，把结果放到结果列表
        if len(path_list) == k:
            res_list.append(path_list[:])
            return
        # 3. 回溯逻辑，从begin_index遍历到n+1，把i放入path列表，回溯递归i + 1，path列表弹出i
        for i in range(begin_index, n + 1):
            # 4. 剪枝优化，当前path列表长度为p，还剩k-p个位置，遍历还剩n + 1 - i个数，
            #         如果n + 1 - i < k - p，表示以及没有足够的数来遍历，则可以直接停止
            if (n + 1 - i) < (k - len(path_list)):
                break
            path_list.append(i)
            backtrack(i + 1)
            path_list.pop()

    backtrack(1)

    return res_list


if __name__ == '__main__':
    n = 4
    k = 4
    print(combine(n, k))
