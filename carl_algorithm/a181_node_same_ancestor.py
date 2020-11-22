# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a181_node_same_ancestor.py
@Time: 2022-12-28 12:53
@Last_update: 2022-12-28 12:53
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


def node_same_ancestor(root, p, q):
    """
    二叉树最近的公共祖先，使用后序遍历方法
    """
    def _recursion(node, p, q):
        """
        递归回溯部分
        1. 参数返回，参数为要处理的节点，返回为递归的结果或者空
        2. 停止条件，如果遇到p，q或者为None则直接返回
        3. 递归逻辑，递归左节点获取结果
        4. 递归右节点获取结果
        5. 如果左右节点结果都不为空则返回返回本节点的值
        6. 如果左节点不为空右节点为空，则返回左节点
        7. 如果右节点不为空左节点为空，则返回右节点
        8. 如果左右节点都为空，则返回空
        """
        # 2. 停止条件，如果遇到p，q或者为None则直接返回
        if (node is None) or (node.val == p.val) or (node.val == q.val):
            return node
        # 3. 递归逻辑，递归左节点获取结果
        left_node = _recursion(node.left, p, q)
        # 4. 递归右节点获取结果
        right_node = _recursion(node.right, p, q)
        # 5. 如果左右节点结果都不为空则返回返回本节点的值
        if (left_node is not None) and (right_node is not None):
            return node
        # 6. 如果左节点不为空右节点为空，则返回左节点
        elif (left_node is not None) and (right_node is None):
            return left_node
        # 7. 如果右节点不为空左节点为空，则返回右节点
        elif (right_node is not None) and (left_node is None):
            return right_node
        # 8. 如果左右节点都为空，则返回空
        else:
            return None

    return _recursion(root, p, q)


if __name__ == '__main__':
    root = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(node_same_ancestor(root, 5, 1))
