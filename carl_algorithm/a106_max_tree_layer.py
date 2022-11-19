# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a106_max_tree_layer.py
@Time: 2022-10-13 22:37
@Last_update: 2022-10-13 22:37
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


def max_tree_layer(root):
    """
    得到每层的最大值，层序遍历
    1. 处理空的情况
    2. 创建结果列表，节点队列
    3. 遍历，条件为节点队列不为空
    4. 获取节点队列的长度，创建暂存队列
    5. 遍历队列长度
    6. 获取节点队列弹出的头结点，把值放到暂存队列
    7. 如果左右不为空，则把相应节点放到节点列表
    8. 放入本层最大值到结果列表
    """
    # 1. 处理空的情况
    if root is None:
        return []
    # 2. 创建结果列表，节点队列
    result_list, node_queue = [], deque([root])
    # 3. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 4. 获取节点队列的长度，创建暂存队列
        length, tmp_list = len(node_queue), []
        # 5. 遍历队列长度
        for _ in range(length):
            # 6. 获取节点队列弹出的头结点，把值放到暂存队列
            cur_node = node_queue.popleft()
            tmp_list.append(cur_node.val)
            # 7. 如果左右不为空，则把相应节点放到节点列表
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)
        # 8. 放入本层最大值到结果列表
        result_list.append(max(tmp_list))

    return result_list


if __name__ == '__main__':
    node = make_tree([3, 9, 20, None, None, 15, 7])
    print(node)
    print(max_tree_layer(node))
