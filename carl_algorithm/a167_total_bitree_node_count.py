# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a167_perfect_bitree_node_count.py
@Time: 2022-11-18 13:36
@Last_update: 2022-11-18 13:36
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


def total_bitree_node_count(root):
    """
    完全二叉树的节点个数，使用递归，利用完美二叉树的节点数可以直接计算的特性
    1. 调用递归，返回
    """
    def _recursion(_root):
        """
        递归部分
        1. 递归参数返回，根节点
        2. 结束条件，如果节点都为空则返回0
        3. 递归逻辑，先往左计算左边的深度，再往右计算右边的深度
        4. 如果两边的深度相同，则返回2 ** n - 1
        5. 不相同，则分别递归左边和右边并加1
        """
        # 2. 结束条件，如果节点都为空则返回0
        if _root is None:
            return 0
        # 3. 递归逻辑，先往左计算左边的深度，再往右计算右边的深度
        left, right = _root.left, _root.right
        left_depth, right_depth = 0, 0
        while left is not None:
            left = left.left
            left_depth += 1
        while right is not None:
            right = right.right
            right_depth += 1
        # 4. 如果两边的深度相同，则返回2 ** n - 1
        if left_depth == right_depth:
            return 1 + 2 * (2 ** left_depth - 1)
        # 5. 不相同，则分别递归左边和右边并加1
        return _recursion(_root.left) + _recursion(_root.right) + 1

    # 1. 调用递归，返回
    return _recursion(root)


if __name__ == '__main__':
    root = create_tree([i+1 for i in range(7)])
    print(total_bitree_node_count(root))
