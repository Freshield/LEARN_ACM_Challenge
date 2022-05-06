# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0226_invertTree.py
@Time: 2020-07-30 11:39
@Last_update: 2020-07-30 11:39
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
    翻转一棵二叉树。
    解法：使用广度优先搜索
    """
    def invertTree(self, root):
        """
        整体流程：
        1. 进行特判
        2. 生成node_list等中间变量
        3. 进行反转和放node
        """
        # 1. 进行特判
        if root is None:
            return root

        # 2. 生成node_list等中间变量
        node_list = [root]

        # 3. 进行反转和放node
        while len(node_list) != 0:
            this_node = node_list.pop(0)
            this_node.left, this_node.right = this_node.right, this_node.left

            if this_node.left is not None:
                node_list.append(this_node.left)
            if this_node.right is not None:
                node_list.append(this_node.right)

        return root


def create_tree(nums):
    root = None
    node_list = []

    for num in nums:
        this_node = TreeNode(num)
        node_list.append(this_node)
        if root is None:
            root = this_node
            continue

        if node_list[0].left is None:
            node_list[0].left = this_node
        else:
            node_list[0].right = this_node
            node_list.pop(0)

    return root


if __name__ == '__main__':
    nums = [4,2,7,1,3,6,9]

    root = create_tree(nums)
    root = Solution().invertTree(root)
    print(root)