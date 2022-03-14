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

    def __str__(self):
        return f'{self.val}, [l:{self.left}, r:{self.right}]'


def create_tree(num_list):
    """
    建立根节点和节点列表
    1. 创建根节点和节点队列
    2. 遍历数值
    3. 新建节点并放到节点队列中
    4. 如果节点队列top的左节点还为空则连接到左节点
    5. 如果节点队列top的有节点还为空则连接到右节点，并弹出此节点
    """
    if len(num_list) == 0:
        return None
    # 1. 创建根节点和节点队列
    root = TreeNode(num_list[0])
    node_queue = [root]
    # 2. 遍历数值
    for i in range(1, len(num_list)):
        #  3. 新建节点并放到节点队列中
        this_node = TreeNode(num_list[i])
        node_queue.append(this_node)
        # 4. 如果节点队列top的左节点还为空则连接到左节点
        if node_queue[0].left is None:
            node_queue[0].left = this_node
        # 5. 如果节点队列top的有节点还为空则连接到右节点，并弹出此节点
        elif node_queue[0].right is None:
            node_queue[0].right = this_node
            node_queue.pop(0)

    return root


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5]
    root = create_tree(num_list)
    print(root)
