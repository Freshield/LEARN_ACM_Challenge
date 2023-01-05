# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a184_delete_sbt.py
@Time: 2023-01-03 10:30
@Last_update: 2023-01-03 10:30
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


def delete_sbt(root, val):
    """
    删除搜索二叉树中的节点，使用递归的方法
    """
    def _recursion(node):
        """
        递归回溯部分
        1. 参数返回，参数为节点，返回为节点
        2. 停止条件，如果为节点为None则返回None
        3. 递归逻辑，如果节点值大于val则递归到左节点，如果小于val则递归到右节点
        4. 剩下为等于的情况，如果左右节点都为None，则返回None
        5. 如果左节点不为空，右节点为空，则返回左节点
        6. 如果右节点不为空，左节点为空，则返回右节点
        7. 如果左右节点都不为空，遍历找到右节点的最左节点
        8. 把node的左节点放到这个节点上，返回右节点
        """
        # 2. 停止条件，如果为节点为None则返回None
        if node is None:
            return None
        # 3. 递归逻辑，如果节点值大于val则递归到左节点，如果小于val则递归到右节点
        if node.val > val:
            node.left = _recursion(node.left)
            return node
        elif node.val < val:
            node.right = _recursion(node.right)
            return node
        # 4. 剩下为等于的情况，如果左右节点都为None，则返回None
        if (node.left is None) and (node.right is None):
            return None
        # 5. 如果左节点不为空，右节点为空，则返回左节点
        if (node.left is not None) and (node.right is None):
            return node.left
        # 6. 如果右节点不为空，左节点为空，则返回右节点
        if (node.right is not None) and (node.left is None):
            return node.right
        # 7. 如果左右节点都不为空，遍历找到右节点的最左节点
        most_left = node.right
        while most_left.left is not None:
            most_left = most_left.left
        # 8. 把node的左节点放到这个节点上，返回右节点
        most_left.left = node.left
        return node.right

    return _recursion(root)


if __name__ == '__main__':
    root = create_tree([5, 3, 6, 2, 4, None, 7])
    val = 3
    print(delete_sbt(root, val))

