# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a63_path_sum_links.py
@Time: 2022-04-24 19:10
@Last_update: 2022-04-24 19:10
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


def path_sum_links(root, target):
    """
    获取目标值的路径，递归回溯，参返结束逻辑
    1. 参返：参数为节点以及包括当前节点的值
    2. 结束：当到叶节点时，如果到达了target则把当前路径放到结果列表中
    3. 逻辑：把左右节点分别进行回溯递归
    """
    result, path_links = [], []
    # 1. 参返：参数为节点以及包括当前节点的值
    def inner_loop(node, sum_value):
        # 2. 结束：当到叶节点时，如果到达了target则把当前路径放到结果列表中
        if (node.left is None) and (node.right is None):
            if sum_value == target:
                result.append(path_links.copy())
            return
        # 3. 逻辑：把左右节点分别进行回溯递归
        if node.left is not None:
            path_links.append(node.left.val)
            sum_value += node.left.val

            inner_loop(node.left, sum_value)

            path_links.pop()
            sum_value -= node.left.val
        if node.right is not None:
            path_links.append(node.right.val)
            sum_value += node.right.val

            inner_loop(node.right, sum_value)

            path_links.pop()
            sum_value -= node.right.val

        return

    if root is not None:
        path_links.append(root.val)
        inner_loop(root, root.val)

    return result


if __name__ == '__main__':
    root = create_tree(range(5))
    print(path_sum_links(root, target=5))
