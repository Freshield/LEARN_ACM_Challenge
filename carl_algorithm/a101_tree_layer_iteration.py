# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a101_tree_layer_iteration.py
@Time: 2022-10-13 21:26
@Last_update: 2022-10-13 21:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a91_tree_struct import make_tree
from collections import deque


def tree_layer_iteration(root):
    """
    层序遍历
    1. 创建需要的结果列表和节点队列
    2. 遍历，条件为节点队列不为空
    3. 记录当前节点队列的长度，新建这层的结果列表
    4. 遍历节点队列的长度
    5. 从队首取出节点，把数值放到结果列表
    6. 把不为空的左右节点放到节点列表队尾
    7. 更新结果列表
    """
    if root is None:
        return []
    # 1. 创建需要的结果列表和节点队列
    result_list, node_queue = [], deque([root])
    # 2. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 3. 记录当前节点队列的长度，新建这层的结果列表
        length, tmp_list = len(node_queue), []
        # 4. 遍历节点队列的长度
        for _ in range(length):
            # 5. 从队首取出节点，把数值放到结果列表
            cur_node = node_queue.popleft()
            tmp_list.append(cur_node.val)
            # 6. 把不为空的左右节点放到节点列表队尾
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)
        # 7. 更新结果列表
        result_list.append(tmp_list)

    return result_list


if __name__ == '__main__':
    node = make_tree([3, 9, 20, None, None, 15, 7])
    print(node)
    print(tree_layer_iteration(node))

