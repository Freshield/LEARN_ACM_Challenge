# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a33_mid_loop.py
@Time: 2022-04-19 12:13
@Last_update: 2022-04-19 12:13
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


def mid_loop(root, rst_list=[]):
    """
    中序遍历
    使用递归的方法进行遍历，确定三要素，输入，结束，顺序
    1. 结束条件为当前节点为None
    2. 顺序为左中右
    """
    # 1. 结束条件为当前节点为None
    if root is None:
        return rst_list
    # 2. 顺序为左中右
    mid_loop(root.left, rst_list)
    rst_list.append(root.val)
    mid_loop(root.right, rst_list)

    return rst_list


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5]
    root = create_tree(num_list)
    print(mid_loop(root))
    print(root)
