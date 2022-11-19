# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a97_postorder_iteration.py
@Time: 2022-10-13 10:07
@Last_update: 2022-10-13 10:07
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


def postorder_iteration(root):
    """
    后序遍历，使用迭代法，左右中，使用前序变化位置中右左然后再反过来
    1. 生成需要的结果列表，指针堆栈
    2. 遍历，条件为指针堆栈不为空
    3. 指针堆栈弹出，把值放到结果列表中，并把左右节点按照左右的顺序放到栈中
    4. 最终把结果列表倒序返回
    """
    if root is None:
        return []
    # 1. 生成需要的结果列表，指针堆栈
    result_list, node_stack = [], [root]
    # 2. 遍历，条件为指针堆栈不为空
    while len(node_stack) != 0:
        # 3. 指针堆栈弹出，把值放到结果列表中，并把左右节点按照左右的顺序放到栈中
        cur_node = node_stack.pop()
        result_list.append(cur_node.val)
        if cur_node.left is not None:
            node_stack.append(cur_node.left)
        if cur_node.right is not None:
            node_stack.append(cur_node.right)

    # 4. 最终把结果列表倒序返回
    return result_list[::-1]


if __name__ == '__main__':
    node = make_tree([1, None, 2, None, None, 3])
    print(postorder_iteration(node))
