# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a69_search_tree_search.py
@Time: 2022-05-07 11:51
@Last_update: 2022-05-07 11:51
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


def search_tree_search(root, target):
    """
    二叉搜索树搜索，使用递归，参返，结束，逻辑
    1. 参返：参数为节点以及目标值，返回为节点或者None
    2. 结束：当节点为空或者None的时候返回
    3. 逻辑：大则左，小则右
    """
    # 1. 参返：参数为节点以及目标值，返回为节点或者None
    def inner_loop(node, target):
        # 2. 结束：当节点为空或者None的时候返回
        if (node is None) or (node.val == target):
            return node
        # 3. 逻辑：大则左，小则右
        if node.val < target:
            return inner_loop(node.right, target)
        if node.val > target:
            return inner_loop(node.left, target)

        return None

    return inner_loop(root, target)


if __name__ == '__main__':
    root = create_tree([4, 2, 7, 1, 3])
    target = 2
    print(search_tree_search(root, target))
