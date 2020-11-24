# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a179_min_diff.py
@Time: 2022-12-26 14:57
@Last_update: 2022-12-26 14:57
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from collections import deque
from a32_treenode import create_tree, TreeNode


def min_diff(root):
    """
    因为是二叉搜索树，使用中序遍历，变成有序队列，然后再获取最小的差值
    使用迭代方式进行中序遍历
    整体流程：
    1. 创建节点栈，结果列表
    2. 遍历，条件为节点栈为空
    3. 弹出栈顶
    4. 如果不为空的话，把不为空的子节点按照左中右的顺序放入到节点栈，中的后边放入空节点
    5. 如果为空，则再弹出节点，放到结果列表中
    6. 最终遍历获取最小的差值
    """
    # 1. 创建节点栈，结果列表
    node_stack, res_list = [root], []
    # 2. 遍历，条件为节点栈为空
    while len(node_stack) != 0:
        # 3. 弹出栈顶
        this_node = node_stack.pop()
        # 4. 如果不为空的话，把不为空的子节点按照左中右的顺序放入到节点栈，中的后边放入空节点
        if this_node is not None:
            if this_node.left is not None:
                node_stack.append(this_node.left)
            node_stack.append(this_node)
            node_stack.append(None)
            if this_node.right is not None:
                node_stack.append(this_node.right)
        # 5. 如果为空，则再弹出节点，放到结果列表中
        else:
            this_node = node_stack.pop()
            res_list.append(this_node.val)
    # 6. 最终遍历获取最小的差值
    min_val = 1e8
    for i in range(1, len(res_list)):
        min_val = min(min_val, abs(res_list[i] - res_list[i-1]))

    return min_val


if __name__ == '__main__':
    root = create_tree([4, 2, 6, 1, 3])
    print(min_diff(root))
