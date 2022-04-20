# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a32_treenode.py
@Time: 2022-04-19 11:00
@Last_update: 2022-04-19 11:00
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
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.test = []

    def __str__(self):
        return f'{self.val}, [l:{self.left}, r:{self.right}]'


def create_tree(num_list):
    """
    建立根节点和节点列表
    1. 根据num_list建立相应的节点，如果为空则是空
    2. 遍历直到2*i+1小于num_list长度
    3. 按照i节点，2*i+1为左节点，2*i+2为右节点设置
    """
    if len(num_list) == 0:
        return None
    # 1. 根据num_list建立相应的节点，如果为空则是空
    node_list = [TreeNode(num) if num is not None else None for num in num_list]
    # 2. 遍历直到2*i+1小于num_list长度
    i = 0
    while 2*i+1 < len(num_list):
        this_node = node_list[i]
        this_node.left = node_list[2*i+1]
        this_node.right = node_list[2*i+2]

        i += 1

    return node_list[0]


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5]
    root = create_tree(num_list)
