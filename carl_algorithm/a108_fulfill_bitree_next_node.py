# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a108_fulfill_bitree_next_node.py
@Time: 2022-10-15 21:06
@Last_update: 2022-10-15 21:06
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
from a91_tree_struct import make_tree, TreeNode


def fulfill_bitree_next_node(root):
    """
    填充二叉树右端节点
    1. 处理空的情况
    2. 创建节点队列
    3. 遍历，条件为节点队列不为空
    4. 获取节点队列长度
    5. 遍历节点队列长度
    6. 获取节点队列最左弹出节点
    7. 如果左右不为空则放到节点队列中
    8. 当前节点的next指向节点队列的最左节点
    """
    # 1. 处理空的情况
    if root is None:
        return None
    # 2. 创建节点队列
    node_queue = deque([root])
    # 3. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 4. 获取节点队列长度
        length = len(node_queue)
        fake_node = TreeNode(None)
        # 5. 遍历节点队列长度
        for _ in range(length):
            # 6. 获取节点队列最左弹出节点
            cur_node = node_queue.popleft()
            # 7. 如果左右不为空则放到节点队列中
            if cur_node.left is not None:
                node_queue.append(cur_node.left)
            if cur_node.right is not None:
                node_queue.append(cur_node.right)
            # 8. 当前节点的next指向节点队列的最左节点
            fake_node.next = cur_node
            fake_node = cur_node

    return root


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(node)
    print(fulfill_bitree_next_node(node))
