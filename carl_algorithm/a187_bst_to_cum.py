# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a187_bst_to_cum.py
@Time: 2023-01-10 13:06
@Last_update: 2023-01-10 13:06
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


def bst_to_cum(root):
    """
    使用反中序遍历，也就是右中左的递归方式
    """
    cum_value = 0

    def _recursion(node, cum_value):
        """
        递归部分，使用反中序的顺序进行递归
        1. 参数返回，参数为树的节点和cum_value，返回为cum_value
        2. 停止条件，当节点为空时候返回
        3. 递归逻辑，顺序为右中左的顺序
        4. 递归右边的节点
        5. cum加上当前节点的数值，更新当前节点的数值
        6. 递归左右的节点
        """
        # 2. 停止条件，当节点为空时候返回
        if node is None:
            return cum_value
        # 3. 递归逻辑，顺序为右中左的顺序
        # 4. 递归右边的节点
        cum_value = _recursion(node.right, cum_value)
        # 5. cum加上当前节点的数值，更新当前节点的数值
        cum_value += node.val
        node.val = cum_value
        # 6. 递归左右的节点
        cum_value = _recursion(node.left, cum_value)

        return cum_value

    _recursion(root, cum_value)

    return root


if __name__ == '__main__':
    root = create_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    print(bst_to_cum(root))
