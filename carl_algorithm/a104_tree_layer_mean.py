# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a104_layer_mean.py
@Time: 2022-10-13 22:04
@Last_update: 2022-10-13 22:04
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


def tree_layer_mean(root):
    """
    获取每层的平均值，层序遍历
    1. 处理为空的情况
    2. 创建结果列表，节点队列
    3. 遍历，直到节点队列为空
    4. 获取队列长度，生成暂存列表
    5. 遍历队列长度
    6. 获取弹出的头结点，并把数值放到暂存列表
    7. 不为空的左右节点，放到节点队列
    8. 把平均值放到结果列表
    """
    # 1. 处理为空的情况
    if root is None:
        return []
    # 2. 创建结果列表，节点队列
    result_list, node_queue = [], deque([root])
    # 3. 遍历，直到节点队列为空
    while len(node_queue) != 0:
        # 4. 获取队列长度，生成暂存列表
        length, tmp_list = len(node_queue), []
        # 5. 遍历队列长度
        for _ in range(length):
            # 6. 获取弹出的头结点，并把数值放到暂存列表
            cur_node = node_queue.popleft()
            tmp_list.append(cur_node.val)
            # 7. 不为空的左右节点，放到节点队列
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)
        # 8. 把平均值放到结果列表
        result_list.append(sum(tmp_list) / length)

    return result_list


if __name__ == '__main__':
    node = make_tree([3, 9, 20, None, None, 15, 7])
    print(node)
    print(tree_layer_mean(node))

