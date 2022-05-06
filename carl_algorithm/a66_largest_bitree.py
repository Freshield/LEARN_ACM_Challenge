# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a66_largest_bitree.py
@Time: 2022-04-27 16:35
@Last_update: 2022-04-27 16:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import TreeNode


def largest_bitree(nums):
    """
    最大二叉树，通过递归的方法，参返，结束，逻辑
    1. 参返：参数为子列表，返回未当前子列表的根节点
    2. 结束：结束条件为如果列表为空则返回None
    3. 逻辑：先找到最大的节点，然后分为左右列表，分别递归
    """
    # 1. 参返：参数为子列表，返回未当前子列表的根节点
    def inner_loop(sub_list):
        # 2. 结束：结束条件为如果列表为空则返回None
        if len(sub_list) == 0:
            return None
        # 3. 逻辑：先找到最大的节点，然后分为左右列表，分别递归
        max_index = sub_list.index(max(sub_list))
        this_node = TreeNode(sub_list[max_index])

        left_node = inner_loop(sub_list[: max_index])
        right_node = inner_loop(sub_list[max_index+1:])

        this_node.left = left_node
        this_node.right = right_node

        return this_node

    if len(nums) == 0:
        return None

    return inner_loop(nums)


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    print(largest_bitree(nums))
