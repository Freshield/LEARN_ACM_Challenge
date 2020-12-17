# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a173_min_depth.py
@Time: 2022-12-05 22:10
@Last_update: 2022-12-05 22:10
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
from a32_treenode import TreeNode, create_tree


def min_depth(root):
    """
    求二叉树最小深度，也就是当节点左右都为空的时候的深度，使用层序遍历
    1. 创建节点队列以及记录深度的数值
    2. 遍历，条件为节点队列不为空
    3. 记录当前的节点队列长度，深度加一，并遍历
    4. 推出最左的节点，并获取
    5. 如果当前节点左右节点都为空则返回深度
    6. 如果左节点不为空，则放入节点队列
    7. 如果右节点不为空，则放入节点队列
    """
    if root is None:
        return 0
    # 1. 创建节点队列以及记录深度的数值
    node_queue, min_depth = deque([root]), 0
    # 2. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 3. 记录当前的节点队列长度，深度加一，并遍历
        queue_length = len(node_queue)
        min_depth += 1
        for i in range(queue_length):
            # 4. 推出最左的节点，并获取
            this_node = node_queue.popleft()
            # 5. 如果当前节点左右节点都为空则返回深度
            if (this_node.left is None) and (this_node.right is None):
                return min_depth
            # 6. 如果左节点不为空，则放入节点队列
            if this_node.left is not None:
                node_queue.append(this_node.left)
            # 7. 如果右节点不为空，则放入节点队列
            if this_node.right is not None:
                node_queue.append(this_node.right)

    return min_depth


if __name__ == '__main__':
    root = create_tree([3, 9, 20, None, None, 15, 7])
    print(min_depth(root))
