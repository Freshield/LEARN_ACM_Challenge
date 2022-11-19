# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a102_tree_inv_layer_iteration.py
@Time: 2022-10-13 21:42
@Last_update: 2022-10-13 21:42
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


def tree_inv_layer_iteration(root):
    """
    倒序层序遍历，先正序再把结果倒过来
    1. 去除空情况
    2. 生成结果列表，节点队列
    3. 遍历，条件为节点队列不为空
    4. 获取节点队列长度，创建暂存列表
    5. 遍历长度，获取节点队列最左节点
    6. 把结果放入，并如果不为空放入左右节点
    7. 更新结果列表
    """
    # 1. 去除空情况
    if root is None:
        return []
    # 2. 生成结果列表，节点队列
    result_list, node_queue = [], deque([root])
    # 3. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 4. 获取节点队列长度，创建暂存列表
        length, tmp_list = len(node_queue), []
        # 5. 遍历长度，获取节点队列最左节点
        for _ in range(length):
            cur_node = node_queue.popleft()
            # 6. 把结果放入，并如果不为空放入左右节点
            tmp_list.append(cur_node.val)
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)
        # 7. 更新结果列表
        result_list.append(tmp_list)

    return result_list[::-1]


if __name__ == '__main__':
    node = make_tree([3, 9, 20, None, None, 15, 7])
    print(tree_inv_layer_iteration(node))
