# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0199_rightSideView.py
@Time: 2020-07-24 10:54
@Last_update: 2020-07-24 10:54
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
        return f'(left: {self.left}, val: {self.val}, right: {self.right})'


class Solution:
    """
    给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
    解法：
    使用宽度优先搜索，最后一个元素便是右侧看到的节点
    """
    def rightSideView(self, root):
        """
        整体流程：
        1. 进行特判
        2. 生成FIFO列表等中间变量
        3. 遍历每层列表
        4. 把最后一个元素放到里边
        """
        # 1. 进行特判
        if root is None:
            return []

        # 2. 生成FIFO列表等中间变量
        FIFO = [root]
        rst_list = []

        # 3. 遍历每层列表
        while len(FIFO) != 0:
            last_node = None
            for i in range(len(FIFO)):
                node = FIFO.pop(0)
                if node.left is not None:
                    FIFO.append(node.left)
                if node.right is not None:
                    FIFO.append(node.right)

                last_node = node

            # 4. 把最后一个元素放到里边
            rst_list.append(last_node.val)

        return rst_list


def create_tree(nums):
    root = None
    tree_list = []
    for num in nums:
        this_node = TreeNode(num)
        if num is not None:
            tree_list.append(this_node)
        if root is None:
            root = this_node
            continue

        if tree_list[0].left is None:
            tree_list[0].left = this_node
        else:
            tree_list[0].right = this_node

            tree_list[0].left = tree_list[0].left if tree_list[0].left.val is not None else None
            tree_list[0].right = tree_list[0].right if tree_list[0].right.val is not None else None
            tree_list.pop(0)

    return root


if __name__ == '__main__':
    nums = [1, 2, 3, None, 5, None, 4]
    root = create_tree(nums)
    print(root)
    print(Solution().rightSideView(root))

