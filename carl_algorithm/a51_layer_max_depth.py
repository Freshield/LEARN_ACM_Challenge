# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a51_layer_max_depth.py
@Time: 2022-04-20 18:40
@Last_update: 2022-04-20 18:40
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree


def layer_max_depth(root):
    """
    得到二叉树每层的平均值，层级遍历，得到平均值
    1. 建队列和列表
    2. 遍历到为空
    3. 遍历当前队列
    4. 得到每层平均值
    """
    # 1. 建队列和列表
    from collections import deque
    queue, rst_list = deque(), []
    if root is not None:
        queue.append(root)
    depth = 0
    # 2. 遍历到为空
    while len(queue) != 0:
        # 3. 遍历当前队列
        queue_length = len(queue)
        depth += 1
        for _ in range(queue_length):
            this_node = queue.popleft()
            if this_node.left is not None:
                queue.append(this_node.left)
            if this_node.right is not None:
                queue.append(this_node.right)

    return depth


if __name__ == '__main__':
    root = create_tree(range(5))
    print(layer_max_depth(root))

