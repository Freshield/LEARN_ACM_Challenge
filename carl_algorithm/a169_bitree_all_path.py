# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a169_bitree_all_path.py
@Time: 2022-11-27 12:14
@Last_update: 2022-11-27 12:14
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree, TreeNode


def bitree_all_path(root):
    """
    二叉树所有的路径，使用回溯算法
    1. 处理特殊情况
    """
    def _recursion(node, path_list, res_list):
        """
        使用回溯算法来进行所有路径递归
        1. 递归参数返回，当前节点，节点列表，结果列表
        2. 递归停止条件，当左右节点都为空的时候停止，并进行结果返回
        3. 如果左节点不为空，则递归左节点，然后回溯
        4. 如果右节点不为空，则递归右节点，然后回溯
        5. 返回节点列表和结果列表
        """
        # 2. 递归停止条件，当左右节点都为空的时候停止，并进行结果返回
        if (node.left is None) and (node.right is None):
            res_list.append('->'.join(path_list))
            return path_list, res_list
        # 3. 如果左节点不为空，则递归左节点，然后回溯
        if node.left is not None:
            path_list.append(str(node.left.val))
            _recursion(node.left, path_list, res_list)
            path_list.pop()
        # 4. 如果右节点不为空，则递归右节点，然后回溯
        if node.right is not None:
            path_list.append(str(node.right.val))
            _recursion(node.right, path_list, res_list)
            path_list.pop()
        # 5. 返回节点列表和结果列表
        return path_list, res_list

    path_list, res_list = _recursion(root, [str(root.val)], [])

    return res_list


if __name__ == '__main__':
    root = create_tree([1, 2, 3, None, 5])
    print(bitree_all_path(root))
