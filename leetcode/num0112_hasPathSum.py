# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0112_hasPathSum.py
@Time: 2020-06-29 13:35
@Last_update: 2020-06-29 13:35
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
        # return f'(left: {self.left}, val: {self.val}, right: {self.right})'
        return str(self.val)


class Solution:
    """
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
    说明: 叶子节点是指没有子节点的节点。
    使用dfs来进行递归
    """
    def hasPathSum(self, root, sum, path_sum=None):
        """
        整体流程：
        1. 如果左右节点都为None则进行比较当前sum的值，如果是的直接返回True
        2. 如果左节点不为None，则继续递归左边
        3. 如果右节点不为None，则继续递归右边
        4. 如果全都没有则返回False
        """
        if root is None:
            return False

        this_path_sum = root.val if path_sum is None else path_sum + root.val

        # 1. 如果左右节点都为None则进行比较当前sum的值，如果是的直接返回True
        if (root.left is None) and (root.right is None):
            return this_path_sum == sum

        # 2. 如果左节点不为None，则继续递归左边
        if root.left is not None:
            rst = self.hasPathSum(root.left, sum, this_path_sum)
            if rst:
                return rst

        # 3. 如果右节点不为None，则继续递归右边
        if root.right is not None:
            rst = self.hasPathSum(root.right, sum, this_path_sum)
            if rst:
                return rst

        # 4. 如果全都没有则返回False
        if path_sum is None:
            return False


def create_tree(nums):
    head = None
    node_list = []

    for num in nums:
        this_node = TreeNode(num)
        if num is not None:
            node_list.append(this_node)

        if head is None:
            head = this_node
            continue

        check_node = node_list[0]
        if check_node.left is None:
            check_node.left = this_node
        else:
            check_node.right = this_node

            check_node.left = check_node.left if check_node.left.val is not None else None
            check_node.right = check_node.right if check_node.right.val is not None else None
            node_list.pop(0)

    return head


if __name__ == '__main__':
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    head = create_tree(nums)
    print(Solution().hasPathSum(head, 21))
