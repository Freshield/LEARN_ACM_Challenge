# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a145_seq_anti_bitree.py
@Time: 2022-10-29 20:49
@Last_update: 2022-10-29 20:49
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


def seq_bitree(root):
    """
    使用层序遍历来进行序列表
    1. 创建需要的节点队列，结果列表
    2. 遍历，条件为节点队列不为空
    3. 获取队列头，如果为空则放到结果列表，继续
    4. 否则把自己的值放到结果列表，并把左右节点放到节点队列
    5. 返回结果列表字符
    """
    if root is None:
        return str(None)
    # 1. 创建需要的节点队列，结果列表
    node_queue, res_list = deque([root]), []
    # 2. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 3. 获取队列头，如果为空则放到结果列表，继续
        this_node = node_queue.popleft()
        if this_node is None:
            res_list.append(None)
            continue
        # 4. 否则把自己的值放到结果列表，并把左右节点放到节点队列
        res_list.append(this_node.val)
        node_queue.append(this_node.left)
        node_queue.append(this_node.right)

    return str(res_list)


def anti_bitree(str_tree):
    """
    反序列化树，数组法
    1. 恢复字符为数组并创建节点
    2. 遍历列表的数值
    3. 如果当前为None则跳过
    4. 如果2*i+1超过列表长度则break
    5. 第2*i+1为左节点
    6. 如果2*i+2超过列表长度则break
    7. 第2*i+2为右节点
    """
    str_tree = eval(str_tree)
    if str_tree is None:
        return None
    # 1. 恢复字符为数组并创建节点
    node_list = [TreeNode(i) if i is not None else None for i in str_tree]
    # 2. 遍历列表的数值
    for i, node in enumerate(node_list):
        # 3. 如果当前为None则跳过
        if node is None:
            continue
        # 4. 如果2*i+1超过列表长度则break
        if 2 * i + 1 >= len(node_list):
            break
        # 5. 第2*i+1为左节点
        node.left = node_list[2*i+1]
        # 6. 如果2*i+2超过列表长度则break
        if 2 * i + 2 >= len(node_list):
            break
        # 7. 第2*i+2为右节点
        node.right = node_list[2*i+2]

    return node_list[0]


def anti_bitree_seq(str_tree):
    """
    反序列化树，遍历法
    1. 恢复字符为数组并创建节点队列，以及指代的i
    2. 遍历，条件为节点队列不为空
    3. 获取节点队列的最开头
    4. 如果数组i小于数组长度且不为None，则生成树节点，连接为左节点，并放到节点队列
    5. 如果数组i+1小于数组长度且不为None，则生成数节点，连接为右节点，并放到节点队列
    6. 更新i为i+2
    """
    tree_list = eval(str_tree)
    if tree_list is None:
        return None
    # 1. 恢复字符为数组并创建节点队列，以及指代的i
    root = TreeNode(tree_list[0])
    node_list, i = deque([root]), 1
    # 2. 遍历，条件为节点队列不为空
    while len(node_list) != 0:
        # 3. 获取节点队列的最开头
        this_node = node_list.popleft()
        # 4. 如果数组i小于数组长度且不为None，则生成树节点，连接为左节点，并放到节点队列
        if (i <= len(tree_list)) and (tree_list[i] is not None):
            left_node = TreeNode(tree_list[i])
            this_node.left = left_node
            node_list.append(left_node)
        # 5. 如果数组i+1小于数组长度且不为None，则生成数节点，连接为右节点，并放到节点队列
        if (i + 1 <= len(tree_list)) and (tree_list[i + 1] is not None):
            right_node = TreeNode(tree_list[i + 1])
            this_node.right = right_node
            node_list.append(right_node)
        # 6. 更新i为i+2
        i += 2

    return root


if __name__ == '__main__':
    root = create_tree([None])
    str_tree = seq_bitree(root)
    print(str_tree)
    print(anti_bitree_seq(str_tree))

