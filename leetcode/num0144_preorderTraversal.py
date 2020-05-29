# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0144_preorderTraversal.py
@Time: 2020-05-29 10:21
@Last_update: 2020-05-29 10:21
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
        return f'{{left:{self.left}, val: {self.val}, right:{self.right}}}'


class Solution:
    """
    给定一个二叉树，返回它的 前序 遍历。
    解法：
    使用dfs来进行遍历
    """
    def __init__(self):
        self.num_list = []

    def preorderTraversal(self, root):
        if root is None:
            return self.num_list

        self.num_list.append(root.val)
        left_list = [root.left] if root.left is not None else []
        right_list = [root.right] if root.right is not None else []

        while True:
            if len(left_list) != 0:
                left_node = left_list.pop(0)
                self.num_list.append(left_node.val)
                if left_node.left is not None:
                    left_list.append(left_node.left)
                if left_node.right is not None:
                    right_list.append(left_node.right)
            elif len(right_list) != 0:
                right_node = right_list.pop(-1)
                self.num_list.append(right_node.val)
                if right_node.left is not None:
                    left_list.append(right_node.left)
                if right_node.right is not None:
                    right_list.append(right_node.right)
            else:
                break

        return self.num_list

    def preorderTraversal_recu(self, root):
        if root is not None:
            self.num_list.append(root.val)
            self.preorderTraversal_recu(root.left)
            self.preorderTraversal_recu(root.right)

        return self.num_list

def create_tree(nums):
    begin = None
    node_list = []

    for num in nums:
        this_node = TreeNode(num)
        if num is not None:
            node_list.append(this_node)
        if begin is None:
            begin = this_node
            continue

        if node_list[0].left is None:
            node_list[0].left = this_node
        else:
            node_list[0].right = this_node
            node_list[0].left = node_list[0].left if node_list[0].left.val is not None else None
            node_list[0].right = None if node_list[0].right.val is None else node_list[0].right
            node_list.pop(0)

    return begin


if __name__ == '__main__':
    nums = [1, None, 2, 3]
    # nums = [1,4,3,2]
    head = create_tree(nums)
    print(head)
    print(Solution().preorderTraversal(head))