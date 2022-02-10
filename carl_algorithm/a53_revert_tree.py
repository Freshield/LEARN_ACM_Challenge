# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a53_revert_tree.py
@Time: 2022-04-20 18:57
@Last_update: 2022-04-20 18:57
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


def revert_tree(root):
    """
    反转二叉树，使用广度优先搜索
    1. 建立队列和列表
    2. 遍历直到队列为空
    3. 遍历当前队列
    4. 反转左右节点
    """
    # 1. 建立队列和列表
    from collections import deque
    queue = deque()
    if root is not None:
        queue.append(root)
    # 2. 遍历直到队列为空
    while len(queue) != 0:
        # 3. 遍历当前队列
        queue_length = len(queue)
        for _ in range(queue_length):
            # 4. 反转左右节点
            this_node = queue.popleft()
            this_node.left, this_node.right = this_node.right, this_node.left
            if this_node.left is not None:
                queue.append(this_node.left)
            if this_node.right is not None:
                queue.append(this_node.right)

    return root


if __name__ == '__main__':
    root = create_tree(range(5))

    print(revert_tree(root))
