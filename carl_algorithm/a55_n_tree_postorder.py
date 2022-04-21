# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: n_tree_postorder.py
@Time: 2022-04-21 12:10
@Last_update: 2022-04-21 12:10
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def n_tree_postorder(root):
    """
    使用递归的方法遍历n叉树，递归三要素，参数，结束，逻辑
    1. 参数，放入root和结果列表
    2. 结束，如果为空则返回
    3. 逻辑，放入当前节点的值并递归
    """
    rst_list = []

    # 1. 参数，放入root和结果列表
    def inner_loop(node, rst_list):
        # 2. 结束，如果为空则返回root
        if node is None:
            return
        # 3. 逻辑，放入当前节点的值并递归
        for child in node.children:
            inner_loop(child, rst_list)
        rst_list.append(node.val)

    inner_loop(root, rst_list)

    return rst_list

