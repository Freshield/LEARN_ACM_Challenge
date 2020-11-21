# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a182_search_bitree_ancestor.py
@Time: 2022-12-29 14:45
@Last_update: 2022-12-29 14:45
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


def search_bitree_ancestor(root, p, q):
    """
    二叉搜索树最近公共祖先，如果值在区间内，则为公共祖先
    1. 遍历，条件为root不为空
    2. 如果root比p，q都小，则递归到右节点
    3. 如果root比p，q都大，则递归到左节点
    4. 否则返回root
    """
    # 1. 遍历，条件为root不为空
    while root is not None:
        # 2. 如果root比p，q都小，则递归到右节点
        if (root.val < p.val) and (root.val < q.val):
            root = root.right
        # 3. 如果root比p，q都大，则递归到左节点
        elif (root.val > p.val) and (root.val > q.val):
            root = root.left
        # 4. 否则返回root
        else:
            return root

    return None


if __name__ == '__main__':
    root = create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left
    q = root.right
    print(search_bitree_ancestor(root, p, q))
