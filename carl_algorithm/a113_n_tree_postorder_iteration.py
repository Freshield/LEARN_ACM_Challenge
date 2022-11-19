# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a113_n_tree_postorder_iteration.py
@Time: 2022-10-15 22:26
@Last_update: 2022-10-15 22:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def n_tree_postorder_iteration(root):
    """
    n叉树后序遍历，使用迭代法，左右中
    1. 处理空的情况
    2. 创建结果列表，节点堆栈
    3. 遍历，直到节点堆栈为空
    4. 获取节点堆栈弹出节点
    5. 如果不为空，把当前节点放回节点栈，并加上None
    6. 把不为空的child放到节点栈
    7. 如果为空，则把结果放到结果列表中
    """
    # 1. 处理空的情况
    if root is None:
        return []
    #  2. 创建结果列表，节点堆栈
    result_list, node_stack = [], [root]
    # 3. 遍历，直到节点堆栈为空
    while len(node_stack) != 0:
        # 4. 获取节点堆栈弹出节点
        cur_node = node_stack.pop()
        # 5. 如果不为空，把当前节点放回节点栈，并加上None
        if cur_node is not None:
            node_stack.append(cur_node)
            node_stack.append(None)
            # 6. 把不为空的child放到节点栈
            for child in cur_node.children[::-1]:
                if child is not None:
                    node_stack.append(child)
            continue
        # 7. 如果为空，则把结果放到结果列表中
        cur_node = node_stack.pop()
        result_list.append(cur_node.val)

    return result_list
