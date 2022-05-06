# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a58_is_balance_tree.py
@Time: 2022-04-21 15:21
@Last_update: 2022-04-21 15:21
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


def is_balance_tree(root):
    """
    是否为平衡二叉树，递归方法，左右中顺序，参返，结束，逻辑
    1. 参返：参数为节点，返回为高度或者-1
    2. 结束：当节点为None的时候返回0
    3. 逻辑：如果左递归返回-1则-1
    4. 如果右递归返回-1则-1
    5. 如果左右高度相差1则返回-1
    6. 返回1+更深的那个
    """
    # 1. 参返：参数为节点，返回为高度或者-1
    def inner_loop(node):
        # 2. 结束：当节点为None的时候返回0
        if node is None:
            return 0
        # 3. 逻辑：如果左递归返回-1则-1
        left_depth = inner_loop(node.left)
        if left_depth == -1:
            return -1
        # 4. 如果右递归返回-1则-1
        right_depth = inner_loop(node.right)
        if right_depth == -1:
            return -1
        # 5. 如果左右高度相差1则返回-1
        if abs(left_depth - right_depth) > 1:
            return -1

        # 6. 返回1+更深的那个
        return 1 + max(left_depth, right_depth)

    if root is None:
        return True

    return True if inner_loop(root) != -1 else False


if __name__ == '__main__':
    root = create_tree(range(5))
    print(is_balance_tree(root))
