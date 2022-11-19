# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a107_fulfill_next_node.py
@Time: 2022-10-15 20:29
@Last_update: 2022-10-15 20:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from collections import deque
from a91_tree_struct import make_tree, TreeNode


def fulfill_next_node(root):
    """
    把树间的节点进行填充
    1. 创建节点栈，虚拟头结点
    2. 遍历，条件为节点栈不为空
    3. 得到节点栈的长度，恢复虚拟头结点
    4. 遍历节点栈的长度
    5. 得到节点栈最左边弹出的节点，如果左右不为空则放到节点栈中
    6. 让虚拟头结点的下一个指向此节点，更新虚拟头结点
    """
    if root is None:
        return None
    # 1. 创建节点栈，虚拟头结点
    node_stack = deque([root])
    # 2. 遍历，条件为节点栈不为空
    while len(node_stack) != 0:
        # 3. 得到节点栈的长度，恢复虚拟头结点
        length = len(node_stack)
        fake_node = TreeNode(None)
        # 4. 遍历节点栈的长度
        for _ in range(length):
            # 5. 如果左右不为空则放到节点栈中
            cur_node = node_stack.popleft()
            if cur_node.left is not None:
                node_stack.append(cur_node.left)
            if cur_node.right is not None:
                node_stack.append(cur_node.right)
            # 6. 让虚拟头结点的下一个指向此节点，更新虚拟头结点
            fake_node.next = cur_node
            fake_node = cur_node

    return root


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    # print(node)
    print(fulfill_next_node(node))
