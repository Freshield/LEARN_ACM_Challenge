# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a117_n_tree_max_depth.py
@Time: 2022-10-17 17:38
@Last_update: 2022-10-17 17:38
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


def n_tree_max_depth(root):
    """
    获取n叉树的最大深度
    1. 处理空的情况
    2. 创建节点队列，深度值
    3. 遍历，条件为节点队列不为空
    4. 获取节点长度，深度加一，并遍历
    5. 获取节点队列最左节点弹出节点
    6. 如果节点孩子不为空，则放入孩子节点
    """
    # 1. 处理空的情况
    if root is None:
        return 0
    # 2. 创建节点队列，深度值
    node_queue, depth_value = deque([root]), 0
    # 3. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 4. 获取节点长度，深度加一，并遍历
        length = len(node_queue)
        depth_value += 1
        for _ in range(length):
            # 5. 获取节点队列最左节点弹出节点
            cur_node = node_queue.popleft()
            # 6. 如果节点孩子不为空，则放入孩子节点
            if cur_node.children is not None:
                node_queue += cur_node.children

    return depth_value

