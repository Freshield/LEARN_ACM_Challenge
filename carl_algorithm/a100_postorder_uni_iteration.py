# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a100_postorder_uni_iteration.py
@Time: 2022-10-13 17:11
@Last_update: 2022-10-13 17:11
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


def postorder_uni_iteration(root):
    """
    后序遍历，迭代法，统一方式，左右中
    1. 创建结果列表，节点栈
    2. 遍历，条件为节点栈为空
    3. 节点栈弹出最上节点
    4. 如果节点不为空则代表继续遍历
    5. 如果左右节点不为空，则把左右节点和当前节点按照，中右左的顺序放回节点栈，当前节点后放空表示已经被遍历
    6. 如果节点为空则代表已经被遍历过，则弹出节点栈最上节点，把数值放到结果列表中
    """
    if root is None:
        return []
    # 1. 创建结果列表，节点栈
    result_list, node_stack = [], [root]
    # 2. 遍历，条件为节点栈为空
    while len(node_stack) != 0:
        # 3. 节点栈弹出最上节点
        cur_node = node_stack.pop()
        # 4. 如果节点不为空则代表继续遍历
        if cur_node is not None:
            # 5. 如果左右节点不为空，则把左右节点和当前节点按照，中右左的顺序放回节点栈，当前节点后放空表示已经被遍历
            node_stack.append(cur_node)
            node_stack.append(None)
            if cur_node.right is not None:
                node_stack.append(cur_node.right)
            if cur_node.left is not None:
                node_stack.append(cur_node.left)
            continue
        # 6. 如果节点为空则代表已经被遍历过，则弹出节点栈最上节点，把数值放到结果列表中
        cur_node = node_stack.pop()
        result_list.append(cur_node.val)

    return result_list


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(postorder_uni_iteration(node))
