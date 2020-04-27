# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a14_npeople_kapple.py
@Time: 2020-04-25 18:37
@Last_update: 2020-04-25 18:37
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def backtrack(n_people, k_apple, people_index,
              used_dict, split_way_list):
    """
    整体流程：
    1. 结束条件：没有苹果了则记录当前选项并返回
    2. 遍历k给小朋友index
    3. 选择，递归，回溯
    """
    # 1. 结束条件：没有苹果了则记录当前选项并返回
    if k_apple == 0:
        split_way_list.append(str(used_dict))
        return used_dict, split_way_list
    elif people_index >= n_people:
        return used_dict, split_way_list

    # 2. 遍历k给小朋友index
    for i in range(k_apple+1):
        # 3. 选择，递归，回溯
        used_dict[people_index] = i
        used_dict, split_way_list = backtrack(n_people, k_apple-i, people_index+1,
                              used_dict, split_way_list)
        used_dict[people_index] = 0

    return used_dict, split_way_list


def npeople_kapple(n_people, k_apple):
    """
    n个小朋友分k个苹果，问怎么分配有多少种方法和分发是什么
    解法：
    使用回溯算法
    遍历一个小朋友的k种方法，然后递归调用n-1个小朋友K-k个苹果
    整体流程：
    1. 生成返回的列表以及分配的字典
    2. 调用回溯
    3. 返回结果
    """
    # 1. 生成返回的列表以及分配的字典
    split_way_list = []
    used_dict = {key: 0 for key in range(n_people)}

    # 2. 调用回溯
    used_dict, split_way_list = backtrack(
        n_people, k_apple, 0, used_dict, split_way_list)

    # 3. 返回结果
    return split_way_list


if __name__ == '__main__':
    n_people = 2
    k_apple = 4
    split_way_list = npeople_kapple(n_people, k_apple)
    print(split_way_list)