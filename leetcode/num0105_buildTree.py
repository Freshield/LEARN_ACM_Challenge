#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0105_buildTree.py
@Time: 2020-05-12 11:08
@Last_update: 2020-05-12 11:08
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
        return '{left: %s, val: %s, right: %s}' % (self.left, self.val, self.right)


class Solution:
    """
    根据一棵树的前序遍历与中序遍历构造二叉树。
    注意:
    你可以假设树中没有重复的元素。
    解法：
    根据pre和in的特性
    pre的开始就是根节点，而in的跟节点左右就是左子和右子
    """
    def buildTree(self, preorder, inorder):
        """
        整体流程：
        1. 结束条件：如果列表为空则返回None
        2. 找到根节点的位置
        3. 得到左树
        4. 得到右树
        """
        # 1. 结束条件：如果列表为空则返回None
        if len(preorder) == 0:
            return None

        # 2. 找到根节点的位置
        val = preorder[0]
        index = inorder.index(val)
        this_node = TreeNode(val)

        # 3. 得到左树
        this_node.left = self.buildTree(preorder[1: index+1], inorder[: index])

        # 4. 得到右树
        this_node.right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return this_node


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # preorder = [1, 2, 3]
    # inorder = [3, 2, 1]
    print(Solution().buildTree(preorder, inorder))
