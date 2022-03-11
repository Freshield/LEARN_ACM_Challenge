# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a34_front_loop.py
@Time: 2022-04-19 14:30
@Last_update: 2022-04-19 14:30
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import TreeNode, create_tree


def front_loop(root, rst_list=[]):
    """
    前序遍历，中左右的顺序
    """
    if root is None:
        return rst_list

    rst_list.append(root.val)
    front_loop(root.left, rst_list)
    front_loop(root.right, rst_list)

    return rst_list


if __name__ == '__main__':
    num_list = list(range(5))
    root = create_tree(num_list)
    print(front_loop(root))
