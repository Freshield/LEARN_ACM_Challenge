# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a62_path_sum.py
@Time: 2022-04-24 16:29
@Last_update: 2022-04-24 16:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree


def path_sum(root, target):
    """
    求是否有路径总和为target的路径，使用递归回溯，参返，结束，逻辑
    1. 参返：参数为节点以及包含当前节点值的已有的总和，返回为bool
    2. 结束：当遇到叶节点时候进行判断并返回
    3. 逻辑：使用回溯进行左右节点的值判断，如果为True则直接向上返回
    """
    # 1. 参返：参数为节点以及包含当前节点值的已有的总和，返回为bool
    def inner_loop(node, sum_value):
        # 2. 结束：当遇到叶节点时候进行判断并返回
        if (node.left is None) and (node.right is None):
            return True if sum_value == target else False
        # 3. 逻辑：使用回溯进行左右节点的值判断，如果为True则直接向上返回
        if node.left is not None:
            sum_value += node.left.val
            res_bool = inner_loop(node.left, sum_value)
            if res_bool is True:
                return True
            sum_value -= node.left.val
        if node.right is not None:
            sum_value += node.right.val
            res_bool = inner_loop(node.right, sum_value)
            if res_bool is True:
                return True
            sum_value -= node.right.val

        return False

    if root is not None:
        return inner_loop(root, root.val)
    else:
        return False


if __name__ == '__main__':
    root = create_tree(range(5))
    print(path_sum(root, target=5))
    print(root)
