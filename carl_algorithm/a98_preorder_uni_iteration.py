# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a98_preorder_uni_iteration.py
@Time: 2022-10-13 15:54
@Last_update: 2022-10-13 15:54
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


def preorder_uni_iteration(root):
    """
    前序遍历，迭代法，统一风格，中左右
    1. 创建结果列表，节点栈
    2. 遍历，条件为节点栈不为空
    3. 弹出节点栈最上节点
    4. 如果节点不为空，代表继续遍历，不存储结果
    5. 如果左右不为空，依次放入右左中，并在中后边放入空节点表示以及被遍历过
    6. 如果节点为空，代表放入结果，弹出节点栈最上节点，把结果存储到结果列表中
    """
    if root is None:
        return []
    # 1. 创建结果列表，节点栈
    result_list, node_stack = [], [root]
    # 2. 遍历，条件为节点栈不为空
    while len(node_stack) != 0:
        # 3. 弹出节点栈最上节点
        cur_node = node_stack.pop()
        # 4. 如果节点不为空，代表继续遍历，不存储结果
        if cur_node is not None:
            # 5. 如果左右不为空，依次放入右左中，并在中后边放入空节点表示以及被遍历过
            if cur_node.right is not None:
                node_stack.append(cur_node.right)
            if cur_node.left is not None:
                node_stack.append(cur_node.left)
            node_stack.append(cur_node)
            node_stack.append(None)
            continue
        # 6. 如果节点为空，代表放入结果，弹出节点栈最上节点，把结果存储到结果列表中
        cur_node = node_stack.pop()
        result_list.append(cur_node.val)

    return result_list


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(node)
    print(preorder_uni_iteration(node))
