# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a177_search_bitree.py
@Time: 2022-12-19 20:44
@Last_update: 2022-12-19 20:44
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


def search_bitree(root, target):
    """
    在二叉搜索树进行搜索，使用迭代
    1. 遍历，直到root为None
    2. 如果当前root等于target则直接返回
    3. 如果target小于root则更新root为左节点
    4. 如果target大于root则更新root为右节点
    """
    # 1. 遍历，直到root为None
    while root is not None:
        # 2. 如果当前root等于target则直接返回
        if root.val == target:
            return root
        # 3. 如果target小于root则更新root为左节点
        if target < root.val:
            root = root.left
        # 4. 如果target大于root则更新root为右节点
        else:
            root = root.right

    return root


if __name__ == '__main__':
    root = create_tree([4, 2, 7, 1, 3])
    target = 2
    print(search_bitree(root, target))
