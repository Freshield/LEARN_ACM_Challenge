# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a93_midorder_loop.py
@Time: 2022-10-12 12:19
@Last_update: 2022-10-12 12:19
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


def midorder_loop(root):
    """
    中序遍历，递归的方法
    1. 创建结果列表
    2. 进行递归
    """
    def _recursion(node, rst_list):
        """
        递归逻辑
        1. 递归参数返回，参数为node和结果列表，返回为结果列表
        2. 结束条件，当node为None时直接返回
        3. 内部逻辑，左中右的顺序
        """
        # 1. 递归参数返回，参数为node和结果列表，返回为结果列表
        # 2. 结束条件，当node为None时直接返回
        if node is None:
            return rst_list
        # 3. 内部逻辑，左中右的顺序
        rst_list = _recursion(node.left, rst_list)
        rst_list.append(node.val)
        rst_list = _recursion(node.right, rst_list)

        return rst_list
    # 1. 创建结果列表
    rst_list = []
    # 2. 进行递归
    rst_list = _recursion(root, rst_list)

    return rst_list


if __name__ == '__main__':
    root = make_tree([1, None, 2, None, None, 3])
    print(midorder_loop(root))

