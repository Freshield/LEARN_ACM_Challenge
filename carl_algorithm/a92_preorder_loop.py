# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a92_preorder_loop.py
@Time: 2022-10-12 12:05
@Last_update: 2022-10-12 12:05
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a91_tree_struct import TreeNode, make_tree


def preorder_loop(root):
    """
    前序遍历，递归法
    1. 创建返回列表
    2. 调用递归函数
    """
    def _recursion(node, result_list):
        """
        1. 递归参数返回，参数下一层节点，结果数组，返回结果数组
        2. 结束条件，为None返回
        3. 内部逻辑，中左右的顺序
        """
        # 1. 递归参数返回，参数下一层节点，返回数组，返回None
        # 2. 结束条件，为None返回
        if node is None:
            return result_list
        # 3. 内部逻辑，中左右的顺序
        result_list.append(node.val)
        result_list = _recursion(node.left, result_list)
        result_list = _recursion(node.right, result_list)

        return result_list
    # 1. 创建返回列表
    result_list = []
    # 2. 调用递归函数
    result_list = _recursion(root, result_list)

    return result_list


if __name__ == '__main__':
    root = make_tree([1, None, 2, None, None, 3])
    print(preorder_loop(root))
