# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0102_levelOrder.py
@Time: 2020-06-12 10:21
@Last_update: 2020-06-12 10:21
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
        return f'(left:{self.left}, val:{self.val}, right:{self.right})'


class Solution:
    """
    给你一个二叉树，请你返回其按 层序遍历 得到的节点值。
    （即逐层地，从左到右访问所有节点）。
    解法：
    使用bfs来进行遍历
    """
    def levelOrder(self, root):
        if root is None:
            return []
        stack = [root]
        rst_list = []
        while len(stack) != 0:
            tmp_list = []
            for i in range(len(stack)):
                node = stack.pop(0)
                tmp_list.append(node.val)
                stack += [node.left] if node.left is not None else []
                stack += [node.right] if node.right is not None else []

            rst_list.append(tmp_list)

        return rst_list


def create_tree(nums):
    begin = None
    tree_nodes = []

    for num in nums:
        this_node = TreeNode(num)
        if num is not None:
            tree_nodes.append(this_node)

        if begin is None:
            begin = this_node
            continue

        if tree_nodes[0].left is None:
            tree_nodes[0].left = this_node
        else:
            tree_nodes[0].right = this_node
            pop_node = tree_nodes.pop(0)
            pop_node.left = pop_node.left if pop_node.left.val is not None else None
            pop_node.right = pop_node.right if pop_node.right.val is not None else None

    return begin


if __name__ == '__main__':
    nums = [3,9,20,None,None,15,7]
    root = create_tree(nums)
    print(Solution().levelOrder(root))