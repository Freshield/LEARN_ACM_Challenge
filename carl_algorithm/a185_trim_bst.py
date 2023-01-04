# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a185_trim_bst.py
@Time: 2023-01-04 13:44
@Last_update: 2023-01-04 13:44
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


def trim_bst(root, L, R):
    """
    修建二叉搜索树，使用递归的方法
    """
    def _recursion(node):
        """
        递归部分
        1. 参数返回，参数为当前节点node，返回为符合条件的节点node
        2. 停止条件，当node为None的时候则返回
        3. 递归逻辑，如果node的val比L小，则递归当前节点的左子节点并返回
        4. 如果node的val比R大，则递归当前节点的右子节点并返回
        5. 当前节点的左子节点为递归左子节点
        6. 当前节点的右子节点为递归右子节点
        7. 返回当前node
        """
        # 2. 停止条件，当node为None的时候则返回
        if node is None:
            return node
        # 3. 递归逻辑，如果node的val比L小，则递归当前节点的右子节点并返回
        if node.val < L:
            right = _recursion(node.right)
            return right
        # 4. 如果node的val比R大，则递归当前节点的左子节点并返回
        if node.val > R:
            left = _recursion(node.left)
            return left
        # 5. 当前节点的左子节点为递归左子节点
        node.left = _recursion(node.left)
        # 6. 当前节点的右子节点为递归右子节点
        node.right = _recursion(node.right)
        # 7. 返回当前node
        return node

    return _recursion(root)


if __name__ == '__main__':
    root = create_tree([3, 0, 4, None, 2, None, None, None, None, 1])
    root = create_tree([1, 0, 2])
    L, R = 1, 2
    print(trim_bst(root, L, R))
