# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a57_tree_max_depth.py
@Time: 2022-04-21 14:34
@Last_update: 2022-04-21 14:34
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


def tree_max_depth(root):
    """
    使用递归的方法，参数，结束，逻辑
    1. 参数：root，返回此node的深度
    2. 结束：如果为None则返回0
    3. 逻辑：左右节点的最大深度加一
    """
    # 1. 参数：root，返回此node的深度
    def inner_loop(node):
        # 2. 结束：如果为None则返回0
        if node is None:
            return 0
        # 3. 逻辑：左右节点的最大深度加一
        left_depth = inner_loop(node.left)
        right_depth = inner_loop(node.right)

        return 1 + max(left_depth, right_depth)

    if root is None:
        return 0
    return inner_loop(root)


if __name__ == '__main__':
    root = create_tree(range(5))
    print(tree_max_depth(root))
