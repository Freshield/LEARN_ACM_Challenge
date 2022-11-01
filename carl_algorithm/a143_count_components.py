# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_graph.py
@Time: 2022-10-26 10:03
@Last_update: 2022-10-26 10:03
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Node(object):
    """
    节点结构类
    """
    def __init__(self, val):
        self.root = val
        self.val = val
        self.link_num = 1

    def __str__(self):
        return f'val {self.val}, root {self.root}, link_num {self.link_num}'


class Graph(object):
    """整体图的结构"""
    def __init__(self):
        self.path_dict = dict()
        self.component = 0

    def add_node(self, node):
        if node.val not in self.path_dict:
            self.path_dict[node.val] = node
            self.component += 1

    def add_link(self, path_tuple):
        """
        连接本节点到目标节点
        1. 对比自己和目标节点的连接数量，如果大于等于目标则把对方改成自己
        2. 否则改成对方
        """
        val_left, val_right = path_tuple
        node_left, node_right = self.get(val_left), self.get(val_right)
        root_left, root_right = self.get_root(node_left), self.get_root(node_right)
        if root_left == root_right:
            return
        # 1. 对比自己和目标节点的连接数量，如果大于等于目标则把对方改成自己
        if root_left.link_num >= root_right.link_num:
            root_right.root = root_left.val
            root_left.link_num += root_right.link_num
        # 2. 否则改成对方
        else:
            root_left.root = root_right.val
            root_right.link_num += root_left.link_num

        self.component -= 1

    def get_root(self, node):
        """
        获取节点的根节点
        1. 遍历，条件为node的root不等于node的val
        2. 找到node val的节点，更新node
        3. 返回根节点
        """
        # 1. 遍历，条件为node的root不等于node的val
        while node.root != node.val:
            # 2. 找到node val的节点，更新node
            target_node = self.path_dict[node.root]
            node = target_node

        # 3. 返回根节点
        return node

    def is_connect(self, val_left, val_right):
        """
        判断两个点是否连接
        1. 找到左节点的root
        2. 找到右节点的root
        3. 返回是否一致
        """
        node_left, node_right = self.get(val_left), self.get(val_right)
        # 1. 找到左节点的root
        left_root = self.get_root(node_left)
        # 2. 找到右节点的root
        right_root = self.get_root(node_right)
        # 3. 返回是否一致
        return left_root.val == right_root.val

    def get(self, val):
        return self.path_dict[val]


def count_component(n, edges):
    """计算联通量"""
    graph = Graph()
    for i in range(n):
        graph.add_node(Node(i))
    for edge_tuple in edges:
        graph.add_link(edge_tuple)

    return graph.component


if __name__ == '__main__':
    n = 4
    edges = [[0, 1], [1, 2], [3, 4], [2, 3]]
    edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
    edges = [[2, 3], [1, 2], [1, 3]]
    print(count_component(n, edges))


