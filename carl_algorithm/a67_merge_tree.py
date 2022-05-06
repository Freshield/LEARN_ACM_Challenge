# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a67_merge_tree.py
@Time: 2022-04-27 17:32
@Last_update: 2022-04-27 17:32
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


def merge_tree(root1, root2):
    """
    合并两个树，递归，参返，结束，逻辑
    1. 参返：参数为两个相应树的对应节点，返回为合并后的树的节点
    2. 结束：如果其中一个为None则返回另一个
    3. 逻辑：把树1的相应节点值变为合并后的节点，然后进行递归
    """
    # 1. 参返：参数为两个相应树的对应节点，返回为合并后的树的节点
    def inner_loop(node1, node2):
        # 2. 结束：如果其中一个为None则返回另一个
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        # 3. 逻辑：把树1的相应节点值变为合并后的节点，然后进行递归
        node1.val += node2.val

        node1.left = inner_loop(node1.left, node2.left)
        node1.right = inner_loop(node1.right, node2.right)

        return node1

    return inner_loop(root1, root2)


if __name__ == '__main__':
    root1 = create_tree([1, 3, 2, 5])
    root2 = create_tree([2, 1, 3, None, 4, None, 7])
    print(root1)
    print(root2)
    print(merge_tree(root1, root2))

