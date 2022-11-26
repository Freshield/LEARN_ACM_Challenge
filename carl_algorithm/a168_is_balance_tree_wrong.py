# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a168_is_balance_tree_wrong.py
@Time: 2022-11-26 17:10
@Last_update: 2022-11-26 17:10
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


def is_balance_tree(root):
    """
    判断一棵树是否为平衡二叉树，使用层序遍历
    1. 创建节点队列以及是否已经有叶节点
    2. 遍历，条件为节点队列不为空
    3. 记录当前节点队列长度，遍历此长度
    4. 推出节点队列开头的节点
    5. 如果当前节点左右都为空，则更改此层已经有叶节点值为True
    6. 全局已有叶节点为True，则返回False，否则添加左右节点入队
    7. 全都遍历后，更新全局已有叶节点值
    """
    if root is None:
        return True
    # 1. 创建节点队列以及是否已经有叶节点
    node_queue, global_exist_leaf = deque([root]), False
    # 2. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 3. 记录当前节点队列长度，遍历此长度
        this_length, tmp_exist_left = len(node_queue), False
        for _ in range(this_length):
            # 4. 推出节点队列开头的节点
            this_node = node_queue.popleft()
            # 5. 如果当前节点左右都为空，则更改此层已经有叶节点值为True
            if (this_node.left is None) and (this_node.right is None):
                tmp_exist_left = True
                continue
            # 6. 全局已有叶节点为True，则返回False，否则添加左右节点入队
            if global_exist_leaf is True:
                return False
            # 针对一遍有值的情况
            if (this_node.left is None) or (this_node.right is None):
                tmp_exist_left = True
            if this_node.left is not None:
                node_queue.append(this_node.left)
            if this_node.right is not None:
                node_queue.append(this_node.right)
        # 7. 全都遍历后，更新全局已有叶节点值
        global_exist_leaf = tmp_exist_left

    return True


if __name__ == '__main__':
    root = create_tree([3, 9, 20, None, None, 15, 7])
    root = create_tree([1, None, 2, None, None, None, 3])
    root = create_tree([1, 2, 3, 4, 5, 6, None, 8])
    print(root)
    print(is_balance_tree(root))
