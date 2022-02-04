# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a61_find_leaf_value.py
@Time: 2022-04-24 15:54
@Last_update: 2022-04-24 15:54
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


def find_leaf_value(root):
    """
    查找左叶节点，使用广度优先，
    1. 建立队列和最左值
    2. 遍历直到队列为空
    3. 遍历当前队列
    4. 更新最左值，放入节点，左右的顺序
    """
    # 1. 建立队列和列表还有最左值
    from collections import deque
    queue, left_down_value = deque(), None
    if root is not None:
        queue.append(root)
        left_down_value = root.val
    # 2. 遍历直到队列为空
    while len(queue) != 0:
        # 3. 遍历当前队列
        queue_length = len(queue)
        for i in range(queue_length):
            this_node = queue.popleft()
            # 4. 更新最左值，放入节点，左右的顺序
            if i == 0:
                left_down_value = this_node.val
            if this_node.left is not None:
                queue.append(this_node.left)
            if this_node.right is not None:
                queue.append(this_node.right)

    return left_down_value


if __name__ == '__main__':
    root = create_tree(range(5))
    print(find_leaf_value(root))
