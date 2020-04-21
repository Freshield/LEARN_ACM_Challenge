#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0113_pathSum.py
@Time: 2020-04-21 14:48
@Last_update: 2020-04-21 14:48
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '(%s left:%s right:%s)' % (self.val, self.left, self.right)


class Tree(object):
    def __init__(self, values_list=None):
        self.root = None
        self.not_full_nodes = []
        if values_list is not None:
            for value in values_list:
                self.add(value)

    def add(self, value):
        new_node = TreeNode(value)
        if value is not None:
            self.not_full_nodes.append(new_node)

        if self.root is None:
            self.root = new_node
        else:
            not_full_node = self.not_full_nodes[0]
            if not_full_node.left is None:
                not_full_node.left = new_node
            elif not_full_node.right is None:
                not_full_node.right = new_node
                self.not_full_nodes.pop(0)

class Solution:
    """
    给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
    说明: 叶子节点是指没有子节点的节点。
    解法：DFS
    深度优先，如果已经大于sum则不再往下
    """
    def DFS(self, this_node, sum, target, path, rst_list):
        if (this_node is None) or (this_node.val is None):
            return -1

        new_sum = this_node.val + sum
        is_leaf = (this_node.left is None) and (this_node.right is None)

        if (new_sum == target) and is_leaf:
            rst_list.append(path + [this_node.val])
        elif not is_leaf:
            self.DFS(this_node.left, new_sum, target, path+[this_node.val], rst_list)
            self.DFS(this_node.right, new_sum, target, path+[this_node.val], rst_list)
        else:
            return -1

    def pathSum(self, root: TreeNode, sum):
        rst_list = []
        self.DFS(root, 0, sum, [], rst_list)

        return rst_list


if __name__ == '__main__':
    values = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    target = 22
    # values = [1,2,None]
    # target = 1
    # values = [-2, None, -3]
    # target = -5
    tree = Tree(values)
    print(tree.root)
    print(Solution().pathSum(tree.root, target))
