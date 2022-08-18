# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a103_tree_right_sight.py
@Time: 2022-10-13 21:54
@Last_update: 2022-10-13 21:54
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


def tree_right_sight(root):
    """
    树的右视图，使用层序遍历
    1. 处理空的情况
    2. 生成结果列表，节点队列
    3. 遍历，条件为节点队列不为空
    4. 得到节点队列的长度
    5. 遍历节点队列的长度
    6. 获取队列弹出的头结点，如果当前为最后一个节点则放值到结果列表中
    7. 如果左右不为空，则放到节点列表中
    """
    # 1. 处理空的情况
    if root is None:
        return []
    # 2. 生成结果列表，节点队列
    result_list, node_queue = [], deque([root])
    # 3. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 4. 得到节点队列的长度
        length = len(node_queue)
        # 5. 遍历节点队列的长度
        for i in range(length):
            # 6. 获取队列弹出的头结点，如果当前为最后一个节点则放值到结果列表中
            cur_node = node_queue.popleft()
            if i == (length - 1):
                result_list.append(cur_node.val)
            # 7. 如果左右不为空，则放到节点列表中
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)

    return result_list


if __name__ == '__main__':
    node = make_tree([3, 9, 20, None, None, 15, 7])
    print(node)
    print(tree_right_sight(node))
