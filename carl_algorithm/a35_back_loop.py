# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a35_back_loop.py
@Time: 2022-04-19 14:34
@Last_update: 2022-04-19 14:34
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


def back_loop(root, rst_list=[]):
    """
    后序遍历，左右中顺序
    """
    if root is None:
        return rst_list

    back_loop(root.left, rst_list)
    back_loop(root.right, rst_list)
    rst_list.append(root.val)

    return rst_list


if __name__ == '__main__':
    num_list = list(range(5))
    root = create_tree(num_list)
    print(back_loop(root))
