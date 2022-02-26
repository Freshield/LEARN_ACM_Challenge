# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a39_mid_loop_uni.py
@Time: 2022-04-19 17:13
@Last_update: 2022-04-19 17:13
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


def mid_loop_uni(root):
    """
    中序统一风格，左中右顺序
    这里把数据放置顺序和数据结果添加分开，让需要放置结果的节点前加入None来标记
    1. 生成结果列表和栈
    2. 遍历直到栈为空
    3. 得到当前节点
    4. 放置顺序，如果当前节点不为None
    5. 按照右中左的顺序放置入栈，并且把中节点前放置None
    6. 如果节点为None
    7. 放置数据部分，弹出None节点，并得到之后的节点，放入结果列表中
    """
    # 1. 生成结果列表和栈
    rst_list, stack = [], []
    if root is not None:
        stack.append(root)
    # 2. 遍历直到栈为空
    while len(stack) != 0:
        # 3. 得到当前节点
        this_node = stack.pop()
        # 4. 放置顺序，如果当前节点不为None
        if this_node is not None:
            # 5. 按照右中左的顺序放置入栈，并且把中节点前放置None
            if this_node.right is not None:
                stack.append(this_node.right)

            stack.append(this_node)
            stack.append(None)

            if this_node.left is not None:
                stack.append(this_node.left)
        # 6. 如果节点为None
        else:
            # 7. 放置数据部分，弹出None节点，并得到之后的节点，放入结果列表中
            this_node = stack.pop()
            rst_list.append(this_node.val)

    return rst_list


if __name__ == '__main__':
    num_list = list(range(5))
    root = create_tree(num_list)
    print(mid_loop_uni(root))
