# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a36_front_loop_while.py
@Time: 2022-04-19 15:44
@Last_update: 2022-04-19 15:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree


def front_loop_while(root):
    """
    使用迭代的方法进行前序遍历
    1. 构建结果列表以及栈
    2. 遍历直到栈为空
    3. 得到新的节点，放把值放到结果列表中
    4. 如果右节点不为None则放到栈
    5. 如果左节点不为None则放到栈
    """
    if root is None:
        return []
    # 1. 构建结果列表以及栈
    rst_list, stack = [], [root]
    # 2. 遍历直到栈为空
    while len(stack) != 0:
        # 3. 得到新的节点，放把值放到结果列表中
        this_node = stack.pop()
        rst_list.append(this_node.val)
        # 4. 如果右节点不为None则放到栈
        if this_node.right is not None:
            stack.append(this_node.right)
        # 5. 如果左节点不为None则放到栈
        if this_node.left is not None:
            stack.append(this_node.left)

    return rst_list


if __name__ == '__main__':
    num_list = list(range(5))
    root = create_tree(num_list)
    print(front_loop_while(root))
