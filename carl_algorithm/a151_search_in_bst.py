# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a151_search_in_bst.py
@Time: 2022-10-30 16:24
@Last_update: 2022-10-30 16:24
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


def search_in_bst(root, val):
    """
    在二叉搜索树中搜索目标值，使用递归
    1. 遍历，条件为root不为空
    2. 如果val等于当前node的val则返回node
    3. 如果val大于node的val则更新为右节点
    4. 如果val小于node的val则更新为左节点
    """
    # 1. 遍历，条件为root不为空
    while root is not None:
        # 2. 如果val等于当前node的val则返回node
        if val == root.val:
            return root
        # 3. 如果val大于node的val则更新为右节点
        elif val > root.val:
            root = root.right
        # 4. 如果val小于node的val则更新为左节点
        else:
            root = root.left

    return None


if __name__ == '__main__':
    root = create_tree([4, 2, 7, 1, 3])
    val = 2
    print(search_in_bst(root, val))
