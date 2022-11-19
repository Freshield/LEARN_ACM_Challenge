# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a123_combination_sum.py
@Time: 2022-10-18 14:55
@Last_update: 2022-10-18 14:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def combination_sum(candidates, target):
    """
    组合总和，从candidates中无限选出和为target的组合，使用回溯
    1. 处理空的情况
    2. 创建path列表，结果列表
    3. 调用回溯递归
    """
    # 1. 处理空的情况
    if (len(candidates) == 0) or (target == 0):
        return []
    candidates.sort()
    # 2. 创建path列表，结果列表
    path_list, res_list = [], []

    def backtrack(start_index, cur_sum):
        """
        回溯递归部分
        1. 参数返回，start_index, cur_sum
        2. 停止条件，当前和大于target则直接返回，如果等于则path列表放到结果列表然后返回
        3. 回溯逻辑，遍历start_index到candidates的长度，和加i，path列表加i，回溯start_index，和减i，path列表弹出
        4. 剪枝，如果当前和加i大于target则直接break
        """
        # 2. 停止条件，当前和大于target则直接返回，如果等于则放到结果列表然后返回
        if cur_sum > target:
            return
        if cur_sum == target:
            res_list.append(path_list[:])
            return
        # 3. 回溯逻辑，遍历start_index到candidates的长度，和加i，path列表加i，回溯start_index，和减i，path列表弹出
        for i in range(start_index, len(candidates)):
            # 4. 剪枝，如果当前和加i大于target则直接break
            if (cur_sum + candidates[i]) > target:
                break
            cur_sum += candidates[i]
            path_list.append(candidates[i])

            backtrack(i, cur_sum)

            cur_sum -= candidates[i]
            path_list.pop()

    # 3. 调用回溯递归
    backtrack(0, 0)

    return res_list


if __name__ == '__main__':
    candidates = [8, 7, 4, 3]
    target = 11
    print(combination_sum(candidates, target))
