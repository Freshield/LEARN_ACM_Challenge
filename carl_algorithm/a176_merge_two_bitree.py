# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a176_merge_two_bitree.py
@Time: 2022-12-17 11:39
@Last_update: 2022-12-17 11:39
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


def merge_two_bitree(node1, node2):
    """
    合并两个二叉树，使用前序遍历
    """
    def _recursion(node1, node2):
        """
        递归部分，使用前序遍历
        1. 参数返回，参数为node1和node2的节点，返回为生成的新节点
        2. 停止条件，如果node1为None则返回node2，如果node2为空则返回node1
        3. 递归逻辑，创建新的节点，值为node1和node2的和
        4. 这个节点的左节点为递归node1的左节点和node2的左节点
        5. 这个节点的右节点为递归node1的右节点和node2的右节点
        """
        # 2. 停止条件，如果node1为None则返回node2，如果node2为空则返回node1
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        # 3. 递归逻辑，创建新的节点，值为node1和node2的和
        this_node = TreeNode(node1.val + node2.val)
        # 4. 这个节点的左节点为递归node1的左节点和node2的左节点
        this_node.left = _recursion(node1.left, node2.left)
        # 5. 这个节点的右节点为递归node1的右节点和node2的右节点
        this_node.right = _recursion(node1.right, node2.right)

        return this_node

    return _recursion(node1, node2)


if __name__ == '__main__':
    node1 = create_tree([1, 3, 2, 5])
    node2 = create_tree([2, 1, 3, None, 4, None, 7])
    print(merge_two_bitree(node1, node2))

