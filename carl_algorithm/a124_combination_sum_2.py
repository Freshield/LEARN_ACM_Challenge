# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a124_combination_sum_2.py
@Time: 2022-10-18 15:37
@Last_update: 2022-10-18 15:37
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def combination_sum_2(candidates, target):
    """
    计算组合总和，每个只能用一次，注意会用重复问题
    1. 去重空的情况
    2. 进行排序
    3. 创建path列表，结果列表
    4. 调用回溯算法
    """
    # 1. 去重空的情况
    if (len(candidates) == 0) or (target == 0):
        return []
    # 2. 进行排序
    candidates.sort()
    # 3. 创建path列表，结果列表
    path_list, res_list = [], []

    def backtrack(start_index, cur_sum):
        """
        回溯递归
        1. 参数返回，参数start_index，cur_sum
        2. 停止条件，当cur_sum大于target则直接返回，如果等于则存储path到结果列表，并返回
        3. 回溯逻辑，遍历从start_index到candidates的长度，当前数值为candidates[i]，创建本层set
        4. 如果当前数值已经在本层字典中，则跳过
        5. cur_sum加当前值，path加当前值，本层set加当前值，回溯递归i+1，cur_sum减当前值，path弹出
        6. 剪枝，如果cur_sum加当前值大于target则break
        """
        # 2. 停止条件，当cur_sum大于target则直接返回，如果等于则存储path到结果列表，并返回
        if cur_sum > target:
            return
        if cur_sum == target:
            res_list.append(path_list[:])
            return
        # 3. 回溯逻辑，遍历从start_index到candidates的长度，当前数值为candidates[i]，创建本层set
        layer_set = set()
        for i in range(start_index, len(candidates)):
            cur_value = candidates[i]
            # 4. 如果当前数值已经在本层字典中，则跳过
            if cur_value in layer_set:
                continue
            # 6. 剪枝，如果cur_sum加当前值大于target则break
            if cur_sum + cur_value > target:
                break
            # 5. cur_sum加当前值，path加当前值，本层set加当前值，回溯递归i+1，cur_sum减当前值，path弹出
            cur_sum += cur_value
            path_list.append(cur_value)
            layer_set.add(cur_value)

            backtrack(i+1, cur_sum)

            cur_sum -= cur_value
            path_list.pop()

    # 4. 调用回溯算法
    backtrack(0, 0)

    return res_list


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combination_sum_2(candidates, target))

