# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a121_combine_sum.py
@Time: 2022-10-17 21:33
@Last_update: 2022-10-17 21:33
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def combine_sum(k, n):
    """
    获得所有k个数的和为n的组合，使用回溯算法
    1. 生成需要的path列表，结果列表
    2. 调用回溯算法
    """
    # 1. 生成需要的path列表，结果列表
    path_list, res_list = [], []

    def backtrack(cur_sum, begin_index):
        """
        回溯部分
        1. 参数返回，当前和，begin_index
        2. 停止条件，当前的path列表长度大于k则停止，如果当前和等于n则放到结果列表中
        3. 回溯逻辑，遍历i从begin_index到10，累加和，放i到path，回溯i+1，和减i，path弹出
        4. 剪枝，path长度为p，剩下的空间为k-p，剩下的遍历为10-i，当(10-i)<(k-p)则以及不够数量
        如果cur_sum加i以及大于n，则直接break
        """
        # 2. 停止条件，当前和大于n则直接返回，或者当前的path列表长度等于k则停止，如果当前和等于n则放到结果列表中
        if cur_sum > n:
            return
        if len(path_list) == k:
            if cur_sum == n:
                res_list.append(path_list[:])
            return
        # 3. 回溯逻辑，遍历i从begin_index到10，累加和，放i到path，回溯i+1，和减i，path弹出
        for i in range(begin_index, 10):
            # 4. 剪枝，path长度为p，剩下的空间为k-p，剩下的遍历为10-i，当(10-i)<(k-p)则以及不够数量
            #         如果cur_sum加i以及大于n，则直接break
            if ((cur_sum + i) > n) or ((10 - i) < (k - len(path_list))):
                break
            cur_sum += i
            path_list.append(i)

            backtrack(cur_sum, i + 1)

            cur_sum -= i
            path_list.pop()

    #2. 调用回溯算法
    backtrack(0, 1)

    return res_list


if __name__ == '__main__':
    k = 3
    n = 7
    print(combine_sum(k, n))
