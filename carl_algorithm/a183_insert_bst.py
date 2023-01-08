# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a183_insert_bst.py
@Time: 2023-01-02 22:57
@Last_update: 2023-01-02 22:57
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


def insert_bst(root, val):
    """
    在二叉搜索树中加入数值节点
    1. 遍历root节点
    2. 如果val大于node则target为右节点
    3. 如果val小于node则target为左节点
    4. 如果target为None，则创建节点，并返回
    5. 否则，更新node
    """
    if root is None:
        return TreeNode(val)
    # 1. 遍历root节点
    node = root
    while node is not None:
        # 2. 如果val大于root则target为右节点
        direction = ''
        if val > node.val:
            target = node.right
            direction = 'right'
        # 3. 如果val小于node则target为左节点
        elif val < node.val:
            target = node.left
            direction = 'left'

        # 4. 如果target为None，则创建节点，并返回
        if target is None:
            new_node = TreeNode(val)
            if direction == 'left':
                node.left = new_node
            else:
                node.right = new_node
            return root
        # 5. 否则，更新node
        node = target

    return root


if __name__ == '__main__':
    root = create_tree([4, 2, 7, 1, 3])
    val = 5
    print(insert_bst(root, val))

