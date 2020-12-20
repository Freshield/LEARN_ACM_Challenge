# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a170_left_leaf_sum.py
@Time: 2022-11-28 22:21
@Last_update: 2022-11-28 22:21
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
from a32_treenode import create_tree, TreeNode


def left_leaf_sum(root):
    """
    左叶节点之和，使用层序遍历
    1. 创建节点队列和总和数值
    2. 遍历，条件为节点队列不为空
    3. 记录队列长度，进行遍历
    4. 从节点队列推出最左，如果当前节点左节点不为空
    5. 如果左节点为叶节点则更新总和，否则放到节点队列中
    6. 如果当前节点的右节点不为空，则放到节点队列中
    """
    # 1. 创建节点队列和总和数值
    node_queue, sum_value = deque([root]), 0
    # 2. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 3. 记录队列长度，进行遍历
        queue_length = len(node_queue)
        for i in range(queue_length):
            # 4. 从节点队列推出最左，如果当前节点左节点不为空
            this_node = node_queue.popleft()
            left_node = this_node.left
            if left_node is not None:
                # 5. 如果左节点为叶节点则更新总和，否则放到节点队列中
                if (left_node.left is None) and (left_node.right is None):
                    sum_value += left_node.val
                else:
                    node_queue.append(left_node)
            # 6. 如果当前节点的右节点不为空，则放到节点队列中
            if this_node.right is not None:
                node_queue.append(this_node.right)

    return sum_value


if __name__ == '__main__':
    root = create_tree([3, 9, 20, None, None, 15, 7])
    print(left_leaf_sum(root))
