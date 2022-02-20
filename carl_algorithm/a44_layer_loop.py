# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a44_layer_loop.py
@Time: 2022-04-20 15:06
@Last_update: 2022-04-20 15:06
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree


def layer_loop(root):
    """
    层级遍历，广度优先搜索
    1. 建立节点队列和结果列表，放入root到节点队列
    2. 遍历直到节点队列为空
    3. 得到当前队列的长度，并遍历
    4. 把每个节点的左右节点，如果不是None则放入队列，并把值放入结果列表
    """
    if root is None:
        return []
    # 1. 建立节点队列和结果列表，放入root到节点队列
    from collections import deque
    queue, rst_list = deque([root]), []
    # 2. 遍历直到节点队列为空
    while len(queue) != 0:
        # 3. 得到当前队列的长度，并遍历
        que_length, tmp_list = len(queue), []
        # 4. 把每个节点的左右节点，如果不是None则放入队列，并把值放入结果列表
        for _ in range(que_length):
            this_node = queue.popleft()
            tmp_list.append(this_node.val)
            if this_node.left is not None:
                queue.append(this_node.left)
            if this_node.right is not None:
                queue.append(this_node.right)
        rst_list.append(tmp_list)

    return rst_list


if __name__ == '__main__':
    root = create_tree(list(range(5)))
    print(layer_loop(root))
