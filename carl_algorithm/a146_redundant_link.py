# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1146_redundant_link.py
@Time: 2022-10-29 22:08
@Last_update: 2022-10-29 22:08
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class UnionFind(object):
    """并查集"""
    def __init__(self):
        self.root_dict = dict()
        self.link_num_dict = dict()

    def union(self, left, right):
        """
        连接两个节点
        1. 找到左右节点的root
        2. 如果相同则直接返回
        3. 找出连接数多的那个节点，保证left为大的节点
        4. 把right的root改为left，left的link num加上right的link num
        """
        # 1. 找到左右节点的root
        left_root = self.find(left)
        right_root = self.find(right)
        # 2. 如果相同则直接返回
        if left_root == right_root:
            return
        # 3. 找出连接数多的那个节点，保证left为大的节点
        if self.link_num_dict[right_root] > self.link_num_dict[left_root]:
            left_root, right_root = right_root, left_root
        # 4. 把right的root改为left，left的link num加上right的link num
        self.root_dict[right_root] = left_root
        self.link_num_dict[left_root] += self.link_num_dict[right_root]

    def find(self, node):
        """
        查找当前的节点的根节点
        1. 遍历，条件为节点的key和value不一致
        2. node为root_dict的value值
        """
        if node not in self.root_dict:
            self.root_dict[node] = node
            self.link_num_dict[node] = 1
            return node
        # 1. 遍历，条件为节点的key和value不一致
        while node != self.root_dict[node]:
            node = self.root_dict[node]

        return node

    def is_same(self, left, right):
        return self.find(left) == self.find(right)


def redundant_link(edges):
    """
    使用并查集
    1. 遍历edges
    2. 如果是同一个集合，则返回当前边
    3. 进行连接
    """
    union = UnionFind()
    # 1. 遍历edges
    for edge in edges:
        left, right = edge
        # 2. 如果是同一个集合，则返回当前边
        if union.is_same(left, right):
            return edge
        # 3. 进行连接
        union.union(left, right)

    return []


if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    print(redundant_link(edges))
