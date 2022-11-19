# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a119_combine.py
@Time: 2022-10-17 20:40
@Last_update: 2022-10-17 20:40
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
    组合，返回1-n所有可能k个数的组合，回溯
    1. 生成当前组合列表，结果列表
    2. 运行回溯
    """
    # 1. 生成当前组合列表，结果列表
    cur_comb_list, res_list = [], []

    def backtrack(begin_index):
        """
        回溯部分
        1. 参数返回，n，开始index
        2. 停止条件，当当前的组合列表长度为k时，就放到结果列表，并返回
        3. 回溯逻辑，遍历开始index之后到n，放到组合列表并递归，弹出组合列表
        4. 剪枝，i大于n - (k - len(cur_comb_list)) + 1则已经没有足够的元素了
        """
        # 2. 停止条件，当当前的组合列表长度为k时，就放到结果列表，并返回
        if len(cur_comb_list) == k:
            res_list.append(cur_comb_list[:])
            return
        # 3. 回溯逻辑，遍历剩下的元素列表，放到组合列表并递归，弹出组合列表
        for i in range(begin_index, n+1):
            # 4. 剪枝，当i大于n + 2 - len(cur_comb_list_)<k时则已经没有足够的元素了，可以直接返回
            if i > n - (k - len(cur_comb_list)) + 1:
                break
            cur_comb_list.append(i)
            backtrack(i+1)
            cur_comb_list.pop()
    # 2. 运行回溯
    backtrack(1)

    return res_list


if __name__ == '__main__':
    n = 4
    k = 4
    print(combine(n, k))
