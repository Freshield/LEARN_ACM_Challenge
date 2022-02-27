# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a38_back_loop_while.py
@Time: 2022-04-19 16:54
@Last_update: 2022-04-19 16:54
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


def back_loop_while(root):
    """
    后序遍历，左右中，是中右左的反向，也就是先用前序遍历，然后再反过来
    1. 创建结果矩阵和栈
    2. 遍历条件为当栈为空的时候
    3. 得到当前栈的top
    4. 把top的值放到结果列表中
    5. 如果不为空放入左边节点
    6. 如果不为空放入右边节点
    """
    if root is None:
        return []
    # 1. 创建结果矩阵和栈
    rst_list, stack = [], [root]
    # 2. 遍历条件为当栈为空的时候
    while len(stack) != 0:
        # 3. 得到当前栈的top
        this_node = stack.pop()
        # 4. 把top的值放到结果列表中
        rst_list.append(this_node.val)
        # 5. 如果不为空放入左边节点
        if this_node.left is not None:
            stack.append(this_node.left)
        # 6. 如果不为空放入右边节点
        if this_node.right is not None:
            stack.append(this_node.right)

    return rst_list[::-1]


if __name__ == '__main__':
    num_list = list(range(5))
    root = create_tree(num_list)
    print(back_loop_while(root))
