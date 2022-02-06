# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a59_all_tree_path.py
@Time: 2022-04-21 15:32
@Last_update: 2022-04-21 15:32
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


def all_tree_path(root):
    """
    得到二叉树左右的路径，递归，中左右顺序，回溯，参返，结束，逻辑
    1. 参返：输入当前节点，已有路径，保存列表
    2. 结束：如果左右节点都为空则保存路径
    3. 逻辑：如果左节点不为空则path放入左节点并递归，然后回溯弹出左节点
    4. 如果右节点不为空则paht放入右节点并递归，然后回溯弹出右节点
    """
    # 1. 参返：输入当前节点，已有路径，保存列表
    def inner_loop(node, path_list, rst_list):
        # 2. 结束：如果左右节点都为空则保存路径
        if (node.left is None) and (node.right is None):
            rst_list.append('->'.join([str(sub.val) for sub in path_list]))
            return

        # 3. 逻辑：如果左节点不为空则path放入左节点并递归，然后回溯弹出左节点
        if node.left is not None:
            path_list.append(node.left)
            inner_loop(node.left, path_list, rst_list)
            path_list.pop()
        # 4. 如果右节点不为空则paht放入右节点并递归，然后回溯弹出右节点
        if node.right is not None:
            path_list.append(node.right)
            inner_loop(node.right, path_list, rst_list)
            path_list.pop()

        return

    if root is None:
        return ''
    rst_list = []
    inner_loop(root, [root], rst_list)

    return rst_list


if __name__ == '__main__':
    root = create_tree(range(5))
    print(all_tree_path(root))
