# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a91_tree_struct.py
@Time: 2022-10-12 11:44
@Last_update: 2022-10-12 11:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def show_node(self, layer=0):
        return f'val: {self.val}\n' \
               f'{" " * 4 * (layer + 1)}' \
               f'left: {self.left.show_node(layer + 1) if self.left is not None else None}\n' \
               f'{" " * 4 * (layer + 1)}' \
               f'right: {self.right.show_node(layer + 1) if self.right is not None else None}'

    def __str__(self, layer=0):
        return self.show_node(layer)


def make_tree(vals):
    """
    创造tree
    1. 遍历生成node
    2. 遍历所有node，如果相应的索引存在
    3. 左节点为2*i+1
    4. 右节点为2*i+2
    """
    # 1. 遍历生成node
    node_list = [TreeNode(val) if val is not None else None for val in vals]
    # 2. 遍历所有node，如果相应的索引存在
    for index, node in enumerate(node_list):
        if node is None:
            continue
        # 3. 左节点为2*i+1
        if (2 * index + 1) < len(node_list):
            node.left = node_list[2 * index + 1]
        # 4. 右节点为2*i+2
        if (2 * index + 2) < len(node_list):
            node.right = node_list[2 * index + 2]

    return node_list[0]


if __name__ == '__main__':
    vals = [1, None, 2, 3]
    tree = make_tree(vals)
    print(tree)

