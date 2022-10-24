# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a112_n_tree_preorder.py
@Time: 2022-10-15 22:21
@Last_update: 2022-10-15 22:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def n_tree_preorder(root):
    """
    n叉树的前序遍历，中左右，用递归
    1. 处理空的情况
    2. 递归运行
    """
    def _recursion(node, res_list):
        """
        1. 参数返回，参数为节点，结果列表，返回为结果列表
        2. 终止条件：当前节点为空
        3. 递归逻辑：把当前节点值放到结果列表，按照顺序递归children
        """
        # 2. 终止条件：当前节点为空
        if node is None:
            return res_list
        # 3. 递归逻辑：把当前节点值放到结果列表，按照顺序递归children
        res_list.append(node.val)
        for child in node.children:
            res_list = _recursion(child, res_list)

        return res_list
    # 1. 处理空的情况
    if root is None:
        return []
    # 2. 递归运行
    return _recursion(root, [])

