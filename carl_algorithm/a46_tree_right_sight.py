# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a46_tree_right_sight.py
@Time: 2022-04-20 15:55
@Last_update: 2022-04-20 15:55
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


def tree_right_sight(root):
    """
    二叉树的右视图，层级遍历然后取最后一个节点数值
    1. 建立节点队列和结果列表
    2. 遍历直到节点队列为空
    3. 得到当前层队列的长度并遍历，如果是最后一个节点则放到结果列表
    4. 左右节点不为空则放到节点队列
    """
    # 1. 建立节点队列和结果列表
    from collections import deque
    queue, rst_list = deque(), []
    if root is not None:
        queue.append(root)
    # 2. 遍历直到节点队列为空
    while len(queue) != 0:
        # 3. 得到当前层队列的长度并遍历，如果是最后一个节点则放到结果列表
        queue_length = len(queue)
        for i in range(queue_length):
            this_node = queue.popleft()
            if i == queue_length - 1:
                rst_list.append(this_node.val)
            if this_node.left is not None:
                queue.append(this_node.left)
            if this_node.right is not None:
                queue.append(this_node.right)

    return rst_list


if __name__ == '__main__':
    root = create_tree(range(5))
    print(tree_right_sight(root))
