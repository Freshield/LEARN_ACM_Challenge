# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a115_is_symmetric_tree.py
@Time: 2022-10-16 17:12
@Last_update: 2022-10-16 17:12
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


def is_symmetric_tree(root):
    """
    判断是否为对称数，使用迭代法，非层序遍历，使用栈
    1. 处理空的情况
    2. 创建节点栈，放入根节点的左右节点
    3. 遍历，条件为节点栈不为空
    4. 弹出最上的两个节点
    5. 处理其中有None的情况
    6. 如果两个节点值不同，则返回False
    7. 放入左节点的左节点，放入右节点的右节点
    8. 放入左节点的右节点，放入右节点的左节点
    """
    # 1. 处理空的情况
    if root is None:
        return False
    # 2. 创建节点栈，放入根节点的左右节点
    node_stack = [root.left, root.right]
    # 3. 遍历，条件为节点栈不为空
    while len(node_stack) != 0:
        # 4. 弹出最上的两个节点
        right_node = node_stack.pop()
        left_node = node_stack.pop()
        # 5. 处理其中有None的情况
        if (left_node is None) or (right_node is None):
            if not ((left_node is None) and (right_node is None)):
                return False
            continue
        # 6. 如果两个节点值不同，则返回False
        if left_node.val != right_node.val:
            return False
        # 7. 放入左节点的左节点，放入右节点的右节点
        node_stack.append(left_node.left)
        node_stack.append(right_node.right)
        # 8. 放入左节点的右节点，放入右节点的左节点
        node_stack.append(left_node.right)
        node_stack.append(right_node.left)

    return True


if __name__ == '__main__':
    node = make_tree([1, 2, 2, 3, 4, 4, 3])
    print(node)
    print(is_symmetric_tree(node))

