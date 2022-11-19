# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a96_midorder_iteration.py
@Time: 2022-10-12 13:21
@Last_update: 2022-10-12 13:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a91_tree_struct import make_tree


def midorder_iteration(root):
    """
    中序遍历，迭代法， 左中右
    1. 生成需要的结果列表，指针栈和当前节点
    2. 遍历，条件为指针栈不为空
    3. 如果节点不为空，则把当前节点放到指针栈，当前节点变为左节点
    4. 如果为空，则取指针栈最后的节点，把数值放到结果列表
    5. 当前节点移到右节点
    """
    if root is None:
        return []
    # 1. 生成需要的结果列表和指针栈
    res_list, p_stack, cur_node = [], [root], root
    # 2. 遍历，条件为指针栈不为空
    while len(p_stack) != 0:
        # 3. 如果节点不为空，则把当前节点放到指针栈，当前节点变为左节点
        if cur_node is not None:
            p_stack.append(cur_node.left)
            cur_node = cur_node.left
            continue
        # 4. 如果为空，则取指针栈最后的节点，把数值放到结果列表
        cur_node = p_stack.pop()
        res_list.append(cur_node.val)
        # 5. 当前节点移到右节点
        cur_node = cur_node.right

    return res_list


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(node)
    print(midorder_iteration(node))
