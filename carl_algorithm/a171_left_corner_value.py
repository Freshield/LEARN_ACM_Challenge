# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a171_left_corner_value.py
@Time: 2022-11-29 11:40
@Last_update: 2022-11-29 11:40
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
from a32_treenode import create_tree, TreeNode


def left_corner_value(root):
    """
    获取二叉树左下节点的值，使用层序遍历
    1. 创建节点队列和corner node
    2. 遍历，条件为节点队列不为空
    3. 获取当前节点队列长度并遍历
    4. 从队列最左推出节点
    5. 如果当前索引为0，则更新corner node
    6. 如果左右不为空则放入左右节点
    """
    # 1. 创建节点队列和corner node
    node_queue, corner_node = deque([root]), root
    # 2. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 3. 获取当前节点队列长度并遍历
        node_length = len(node_queue)
        for i in range(node_length):
            # 4. 从队列最左推出节点
            this_node = node_queue.popleft()
            # 5. 如果当前索引为0，则更新corner node
            if i == 0:
                corner_node = this_node
            # 6. 如果左右不为空则放入左右节点
            if this_node.left is not None:
                node_queue.append(this_node.left)
            if this_node.right is not None:
                node_queue.append(this_node.right)

    return corner_node.val


if __name__ == '__main__':
    root = create_tree([2, 1, 3])
    print(left_corner_value(root))

