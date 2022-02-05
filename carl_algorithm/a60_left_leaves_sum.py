# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a60_left_leaves_sum.py
@Time: 2022-04-24 15:04
@Last_update: 2022-04-24 15:04
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


def left_leaves_sum(root):
    """
    计算左叶节点总和，使用递归方法，后序左右中顺序，递归三要素参返，结束，逻辑
    1. 参返：参数为输入的节点，返回当前节点下左节点的总和
    2. 结束：当当前节点为None的时候，返回0
    3. 逻辑：左右中顺序，中的时候来判断左节点是否为左叶节点并和左右节点相加返回
    """
    # 1. 参返：参数为输入的节点，返回当前节点下左节点的总和
    def inner_loop(node):
        # 2. 结束：当当前节点为None的时候，返回0
        if node is None:
            return 0
        # 3. 逻辑：左右中顺序，中的时候来判断左节点是否为左叶节点并和左右节点相加返回
        left_sum = inner_loop(node.left)
        right_sum = inner_loop(node.right)
        mid_sum = 0
        if (node.left is not None) and (node.left.left is None) and (node.left.right is None):
            mid_sum = node.left.val

        return mid_sum + left_sum + right_sum

    return inner_loop(root)


if __name__ == '__main__':
    root = create_tree([3,9,20,None,None,15,7])
    print(left_leaves_sum(root))
    print(root)

