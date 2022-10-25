# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a111_reverse_bitree.py
@Time: 2022-10-15 22:02
@Last_update: 2022-10-15 22:02
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a91_tree_struct import make_tree


def reverse_bitree(root):
    """
    翻转二叉树，使用迭代法，深度优先，前序遍历，中左右
    1. 处理空的情况
    2. 创建节点栈
    3. 遍历直到节点栈为空
    4. 弹出一个节点
    5. 如果不为空，则把当前节点的不为空的左右还在按照右左中顺序放回堆栈，中后加一个空作为标记
    6. 如果为空，则弹出最后，并把左右子节点翻转
    """
    # 1. 处理空的情况
    if root is None:
        return None
    # 2. 创建节点栈
    node_stack = [root]
    # 3. 遍历直到节点栈为空
    while len(node_stack) != 0:
        # 4. 弹出一个节点
        cur_node = node_stack.pop()
        # 5. 如果不为空，则把当前节点的不为空的左右还在按照右左中顺序放回堆栈，中后加一个空作为标记
        if cur_node is not None:
            if cur_node.right is not None:
                node_stack.append(cur_node.right)
            if cur_node.left is not None:
                node_stack.append(cur_node.left)
            node_stack.append(cur_node)
            node_stack.append(None)
            continue
        # 6. 如果为空，则弹出最后，并把左右子节点翻转
        cur_node = node_stack.pop()
        cur_node.left, cur_node.right = cur_node.right, cur_node.left

    return root


if __name__ == '__main__':
    node = make_tree([4, 2, 7, 1, 3, 6, 9])
    print(node)
    print(reverse_bitree(node))
