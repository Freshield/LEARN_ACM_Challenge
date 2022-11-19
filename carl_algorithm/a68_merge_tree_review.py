# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a68_merge_tree_review.py
@Time: 2022-05-06 17:05
@Last_update: 2022-05-06 17:05
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


def merge_tree_review(root1, root2):
    """
    合并两个树，迭代，参返，结束，逻辑
    1. 参返：参数两个对应的节点，返回为合并后的节点
    2. 结束：如果其中一个为None则返回不为None的那个
    3. 逻辑：使用树一来进行合并
    """
    # 1. 参返：参数两个对应的节点，返回为合并后的节点
    def inner_loop(node1, node2):
        # 2. 结束：如果其中一个为None则返回不为None的那个
        if (node1 is None) or (node2 is None):
            return node1 if node1 is not None else node2

        # 3. 逻辑：使用树一来进行合并
        node1.val += node2.val
        node1.left = inner_loop(node1.left, node2.left)
        node1.right = inner_loop(node1.right, node2.right)

        return node1

    return inner_loop(root1, root2)


if __name__ == '__main__':
    root1 = create_tree([1, 3, 2, 5])
    root2 = create_tree([2, 1, 3, None, 4, None, 7])
    print(merge_tree_review(root1, root2))
