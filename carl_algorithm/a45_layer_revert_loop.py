# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a45_layer_revert_loop.py
@Time: 2022-04-20 15:44
@Last_update: 2022-04-20 15:44
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


def layer_revert_loop(root):
    """
    反序得到层级遍历的结果，先正常广度优先遍历，然后结果列表反置
    1. 创建节点队列和结果列表
    2. 遍历直到队列为空
    3. 遍历队列本层节点，把相应的左右节点放入队列，把值放入结果列表
    4. 返回反序
    """
    # 1. 创建节点队列和结果列表
    from collections import deque
    queue, rst_list = deque(), []
    if root is not None:
        queue.append(root)

    # 2. 遍历直到队列为空
    while len(queue) != 0:
        # 3. 遍历队列本层节点，把相应的左右节点放入队列，把值放入结果列表
        queue_length, tmp_list = len(queue), []
        for _ in range(queue_length):
            this_node = queue.popleft()
            tmp_list.append(this_node.val)
            if this_node.left is not None:
                queue.append(this_node.left)
            if this_node.right is not None:
                queue.append(this_node.right)
        rst_list.append(tmp_list)

    return rst_list[::-1]


if __name__ == '__main__':
    root = create_tree(list(range(5)))
    print(layer_revert_loop(root))
