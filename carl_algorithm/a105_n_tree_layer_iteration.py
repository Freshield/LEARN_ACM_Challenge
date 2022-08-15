# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a105_n_tree_layer_iteration.py
@Time: 2022-10-13 22:18
@Last_update: 2022-10-13 22:18
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


def n_tree_layer_iteration(root):
    """
    n叉数层序遍历
    1. 处理为空的情况
    2. 创建结果列表，节点堆栈
    3. 遍历，条件为节点堆栈不为空
    4. 获取节点堆栈的长度，创建暂存列表
    5. 遍历节点堆栈长度
    6. 获取节点堆栈弹出的最左节点，并把数值放到暂存列表
    7. 子节点列表不为空，则把子节点都放到节点堆栈中
    8. 更新结果列表
    """
    # 1. 处理为空的情况
    if root is None:
        return []
    # 2. 创建结果列表，节点堆栈
    result_list, node_stack = [], deque([root])
    # 3. 遍历，条件为节点堆栈不为空
    while len(node_stack) != 0:
        # 4. 获取节点堆栈的长度，创建暂存列表
        length, tmp_list = len(node_stack), []
        # 5. 遍历节点堆栈长度
        for i in range(length):
            # 6. 获取节点堆栈弹出的最左节点，并把数值放到暂存列表
            cur_node = node_stack.popleft()
            tmp_list.append(cur_node.val)
            # 7. 子节点列表不为空，则把子节点都放到节点堆栈中
            if cur_node.children is not None:
                node_stack += cur_node.children
        # 8. 更新结果列表
        result_list.append(tmp_list)

    return result_list


if __name__ == '__main__':
    node = make_tree([3, 9, 20, None, None, 15, 7])
    print(node)
    print(n_tree_layer_iteration(node))
