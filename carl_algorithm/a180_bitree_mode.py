# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a180_bitree_mode.py
@Time: 2022-12-27 10:11
@Last_update: 2022-12-27 10:11
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree, TreeNode


def bitree_mode(root):
    """
    二叉搜索树中的众数，使用中序遍历
    1. 创建节点栈，以及最大值，累加值，前一个节点，结果列表
    2. 遍历，条件为节点栈不为空
    3. 获取弹出的栈顶
    4. 如果不为空，按照左中右的顺序放入不为空的节点，中后边放如空节点
    5. 如果为空，则获取弹出的栈顶
    6. 如果和前一个节点值不同，则count为1，否则count加1
    7. 如果count等于最大值，则把当前节点放到结果列表中
    8. 如果count大于最大值，则清空结果列表，更新最大值，放入当前节点值
    9. 更新pre_node
    """
    # 1. 创建节点栈，以及最大值，累加值，前一个节点，结果列表
    node_stack, res_list = [root], []
    max_count, count, pre_node = -1, 0, root
    # 2. 遍历，条件为节点栈不为空
    while len(node_stack) != 0:
        # 3. 获取弹出的栈顶
        this_node = node_stack.pop()
        # 4. 如果不为空，按照左中右的顺序放入不为空的节点，中后边放如空节点
        if this_node is not None:
            if this_node.left is not None:
                node_stack.append(this_node.left)
            node_stack.append(this_node)
            node_stack.append(None)
            if this_node.right is not None:
                node_stack.append(this_node.right)
            continue
        # 5. 如果为空，则获取弹出的栈顶
        this_node = node_stack.pop()
        # 6. 如果和前一个节点值不同，则count为1，否则count加1
        if this_node.val != pre_node.val:
            count = 1
        else:
            count += 1
        # 7. 如果count等于最大值，则把当前节点放到结果列表中
        if count == max_count:
            res_list.append(this_node.val)
        # 8. 如果count大于最大值，则清空结果列表，更新最大值，放入当前节点值
        if count > max_count:
            max_count = count
            res_list = [this_node.val]
        # 9. 更新pre_node
        pre_node = this_node

    return res_list


if __name__ == '__main__':
    root = create_tree([1, None, 2, None, None, 2])
    print(bitree_mode(root))

