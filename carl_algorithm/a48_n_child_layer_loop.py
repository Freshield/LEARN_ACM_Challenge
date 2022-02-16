# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a48_n_child_layer_loop.py
@Time: 2022-04-20 17:37
@Last_update: 2022-04-20 17:37
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def n_child_layer_loop(root):
    """
    n叉树层级遍历
    1. 建队列和列表
    2. 遍历到队列为空
    3. 遍历当前层队列
    4. 把值放到结果中，如果children不为None则添加到队列
    """
    # 1. 建队列和列表
    from collections import deque
    queue, rst_list = deque(), []
    if root is not None:
        queue.append(root)
    # 2. 遍历到队列为空
    while len(queue) != 0:
        # 3. 遍历当前层队列
        queue_length, tmp_list = len(queue), []
        for _ in range(queue_length):
            this_node = queue.popleft()
            tmp_list.append(this_node.val)
            if this_node.children is not None:
                for node in this_node.children:
                    queue.append(node)
        rst_list.append(tmp_list)
    return rst_list