# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a94_postorder_loop.py
@Time: 2022-10-12 12:35
@Last_update: 2022-10-12 12:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a91_tree_struct import make_tree


def postorder_loop(root):
    """
    后序遍历，递归方法
    1. 生成需要的结果列表
    2. 进行递归
    """
    def _recursion(node, res_list):
        """
        递归逻辑
        1. 递归参数返回，参数为node和结果列表，返回为结果列表
        2. 结束条件，node为None则返回结果列表
        3. 内部逻辑，左右中顺序遍历
        """
        # 1. 递归参数返回，参数为node和结果列表，返回为结果列表
        # 2. 结束条件，node为None则返回结果列表
        if node is None:
            return res_list
        # 3. 内部逻辑，左右中顺序遍历
        res_list = _recursion(node.left, res_list)
        res_list = _recursion(node.right, res_list)
        res_list.append(node.val)

        return res_list
    # 1. 生成需要的结果列表
    res_list = []
    # 2. 进行递归
    res_list = _recursion(root, res_list)

    return res_list


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(postorder_loop(node))

