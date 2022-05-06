# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a56_is_mirror_tree.py
@Time: 2022-04-21 12:25
@Last_update: 2022-04-21 12:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree, TreeNode


def is_mirror_tree(root):
    """
    判断是否是镜像树，使用递归方法，参数，结束，逻辑
    1. 参数：左右节点
    2. 结束：左右节点不同时为None或者值不相同
    3. 逻辑：递归左右节点对应的节点
    """
    # 1. 参数：左右节点
    def inner_loop(left_node, right_node):
        # 2. 结束：左右节点不同时为None或者值不相同
        if (left_node is None) and (right_node is not None):
            return False
        elif (left_node is not None) and (right_node is None):
            return False
        elif (left_node is None) and (right_node is None):
            return True
        elif left_node.val != right_node.val:
            return False

        # 3. 逻辑：递归左右节点对应的节点
        out_res = inner_loop(left_node.left, right_node.right)
        in_res = inner_loop(left_node.right, right_node.left)

        return out_res and in_res

    if root is None:
        return True

    return inner_loop(root.left, root.right)


if __name__ == '__main__':
    root = create_tree(range(5))
    print(is_mirror_tree(root))

