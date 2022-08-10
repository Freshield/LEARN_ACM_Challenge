# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a110_bitree_min_depth.py
@Time: 2022-10-15 21:33
@Last_update: 2022-10-15 21:33
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


def bitree_min_depth(root):
    """
    二叉树最小深度
    1. 处理为空的情况
    2. 创建深度数值，节点队列
    3. 遍历，直到节点队列为空
    4. 获取节点队列长度，深度加一
    5. 遍历节点队列长度
    6. 获取节点队列最左弹出节点
    7. 如果当前节点左右都为空，则直接返回当前深度
    8. 如果左右不为空则放到节点队列
    """
    # 1. 处理为空的情况
    if root is None:
        return 0
    # 2. 创建深度数值，节点队列
    depth_value, node_queue = 0, deque([root])
    # 3. 遍历，直到节点队列为空
    while len(node_queue) != 0:
        # 4. 获取节点队列长度，深度加一
        length = len(node_queue)
        depth_value += 1
        # 5. 遍历节点队列长度
        for _ in range(length):
            # 6. 获取节点队列最左弹出节点
            cur_node = node_queue.popleft()
            # 7. 如果当前节点左右都为空，则直接返回当前深度
            if (cur_node.left is None) and (cur_node.right is None):
                return depth_value
            # 8. 如果左右不为空则放到节点队列
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)

    return depth_value


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(node)
    print(bitree_min_depth(node))
