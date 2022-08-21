# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a99_midorder_iteration.py
@Time: 2022-10-13 16:23
@Last_update: 2022-10-13 16:23
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


def midorder_uni_iteration(root):
    """
    中序遍历，迭代法，同一格式，左中右
    1. 创建结果列表，节点栈
    2. 遍历，条件为节点栈不为空
    3. 节点栈弹出最上节点
    4. 如果当前节点不为空，则表示继续遍历数据
    5. 如果节点左右不为空，按照右中左的顺序放入栈中，中后边放None表示已经遍历过
    6. 如果当前节点为空，则继续弹出最上节点，把数值放到结果列表中
    """
    if root is None:
        return []
    # 1. 创建结果列表，节点栈
    result_list, node_stack = [], [root]
    # 2. 遍历，条件为节点栈不为空
    while len(node_stack) != 0:
        # 3. 节点栈弹出最上节点
        cur_node = node_stack.pop()
        # 4. 如果当前节点不为空，则表示继续遍历数据
        if cur_node is not None:
            # 5. 如果节点左右不为空，按照右中左的顺序放入栈中，中后边放None表示已经遍历过
            if cur_node.right is not None:
                node_stack.append(cur_node.right)
            node_stack.append(cur_node)
            node_stack.append(None)
            if cur_node.left is not None:
                node_stack.append(cur_node.left)
            continue
        # 6. 如果当前节点为空，则继续弹出最上节点，把数值放到结果列表中
        cur_node = node_stack.pop()
        result_list.append(cur_node.val)

    return result_list


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(node)
    print(midorder_uni_iteration(node))
