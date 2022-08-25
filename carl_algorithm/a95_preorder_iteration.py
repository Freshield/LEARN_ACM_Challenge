# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a95_preorder_iteration.py
@Time: 2022-10-12 13:01
@Last_update: 2022-10-12 13:01
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


def preorder_iteration(root):
    """
    前序遍历，迭代法，中左右
    1. 创建结果列表，指针栈，并放入root
    2. 遍历，条件为栈不为空
    3. 弹出栈，把值放到结果列表中
    4. 如果不为空，往指针栈里放入左节点和右节点，需要反过来放
    """
    if root is None:
        return []
    # 1. 创建结果列表，指针栈，并放入root
    res_list, p_stack = [], [root]
    # 2. 遍历，条件为栈不为空
    while len(p_stack) != 0:
        # 3. 弹出栈，把值放到结果列表中
        node = p_stack.pop()
        res_list.append(node.val)
        # 4. 如果不为空，往指针栈里放入左节点和右节点
        if node.right is not None:
            p_stack.append(node.right)
        if node.left is not None:
            p_stack.append(node.left)

    return res_list


if __name__ == '__main__':
    root = make_tree([3, 1, 2])
    print(root)
    print(preorder_iteration(root))
