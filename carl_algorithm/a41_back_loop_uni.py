# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a41_back_loop_uni.py
@Time: 2022-04-19 17:31
@Last_update: 2022-04-19 17:31
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


def back_loop_uni(root):
    """
    后序遍历统一迭代版，左右中顺序，把节点排序和节点取值分开
    1. 生成结果列表和栈
    2. 遍历直到栈为空
    3. 得到当前栈的顶节点
    4. 如果不为None则是排序，按照中右左的顺序进行排序，并插入None
    5. 如果为None则为取值，得到None下一个节点值放入结果列表中
    """
    # 1. 生成结果列表和栈
    rst_list, stack = [], []
    if root is not None:
        stack.append(root)
    # 2. 遍历直到栈为空
    while len(stack) != 0:
        # 3. 得到当前栈的顶节点
        this_node = stack.pop()
        # 4. 如果不为None则是排序，按照中右左的顺序进行排序，并插入None
        if this_node is not None:
            stack.append(this_node)
            stack.append(None)

            if this_node.right is not None:
                stack.append(this_node.right)
            if this_node.left is not None:
                stack.append(this_node.left)
        # 5. 如果为None则为取值，得到None下一个节点值放入结果列表中
        else:
            this_node = stack.pop()
            rst_list.append(this_node.val)

    return rst_list


if __name__ == '__main__':
    num_list = list(range(5))
    root = create_tree(num_list)
    print(back_loop_uni(root))
