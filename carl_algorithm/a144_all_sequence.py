# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a144_all_chance.py
@Time: 2022-10-27 14:43
@Last_update: 2022-10-27 14:43
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def all_sequence(nums):
    """
    获取nums的全排列，使用回溯算法
    1. 生成需要的path list，res list
    2. 运行回溯算法
    3. 返回结果
    """
    # 1. 生成需要的path list，res list
    path_list, res_list = [], []

    def backtrack(num_list):
        """
        回溯递归
        1. 参数返回，num list
        2. 停止条件，如果输入的num list为空则把当前的path list存到结果res list中，并返回
        3. 回溯逻辑，遍历nums，把num放到path list中，同时把num从nums弹出，剩下的继续递归
        4. 完成后，把num放回相应的位置
        """
        # 2. 停止条件，如果输入的num list为空则把当前的path list存到结果res list中，并返回
        if len(num_list) == 0:
            res_list.append(path_list[:])
            return
        # 3. 回溯逻辑，遍历nums，把num放到path list中，同时把num从nums弹出，剩下的继续递归
        for i in range(len(num_list)):
            num = num_list.pop(i)
            path_list.append(num)

            backtrack(num_list)

            num_list.insert(i, num)
            path_list.pop()

    # 2. 运行回溯算法
    backtrack(nums)

    return res_list


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(all_sequence(nums))
