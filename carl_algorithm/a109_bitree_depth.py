# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a109_bitree_depth.py
@Time: 2022-10-15 21:24
@Last_update: 2022-10-15 21:24
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


def bitree_depth(root):
    """
    获取二叉树的深度，使用层序遍历，列表长度就是
    1. 生成深度数值，节点队列
    2. 遍历，条件为节点队列不为空
    3. 获取节点队列长度，深度加一
    4. 遍历节点队列长度
    5. 获取节点队列最左弹出的数值
    6. 如果左右不为空则放到节点队列中
    """
    if root is None:
        return 0
    # 1. 生成深度列表，节点队列
    depth_value, node_queue = 0, deque([root])
    # 2. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 3. 获取节点队列长度，深度加一
        length = len(node_queue)
        depth_value += 1
        # 4. 遍历节点队列长度
        for _ in range(length):
            # 5. 获取节点队列最左弹出的数值
            cur_node = node_queue.popleft()
            # 6. 如果左右不为空则放到节点队列中
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)

    return depth_value


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(node)
    print(bitree_depth(node))

