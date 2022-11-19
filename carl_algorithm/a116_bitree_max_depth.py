# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a116_bitree_max_depth.py
@Time: 2022-10-17 17:30
@Last_update: 2022-10-17 17:30
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
from a91_tree_struct import make_tree


def bitree_max_depth(root):
    """
    获取二叉树的最大深度，使用层序遍历
    1. 处理空的情况
    2. 创建节点队列，深度值
    3. 遍历，条件为节点队列不为空
    4. 获取节点队列长度，深度加一，并遍历
    5. 获取节点队列最左的值
    6. 如果左右不为空，则放左右节点到节点队列中
    """
    # 1. 处理空的情况
    if root is None:
        return 0
    # 2. 创建节点队列，深度值
    node_queue, depth_value = deque([root]), 0
    # 3. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 4. 获取节点队列长度，深度加一，并遍历
        length = len(node_queue)
        depth_value += 1
        for _ in range(length):
            # 5. 获取节点队列最左的值
            cur_node = node_queue.popleft()
            # 6. 如果左右不为空，则放左右节点到节点队列中
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)

    return depth_value


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(node)
    print(bitree_max_depth(node))
