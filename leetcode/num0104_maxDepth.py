#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0104_maxDepth.py
@Time: 2020-04-30 14:46
@Last_update: 2020-04-30 14:46
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
        return '(left:%s, val:%s right:%s)' % (str(self.left), str(self.val), str(self.right))


class Solution:
    """
    给定一个二叉树，找出其最大深度。
    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    说明: 叶子节点是指没有子节点的节点。
    解法：
    使用dfs来进行搜索
    """
    def maxDepth(self, root):
        """
        整体流程：
        1. 结束条件：左右节点都为None，返回0
        2. 如果左边节点不为None则递归左边节点
        3. 如果有右边节点不为None则递归右边节点
        4. 返回左边右边的最大值加1
        """
        if root is None:
            return 0
        # 1. 结束条件：左右节点都为None，返回0
        if (root.left is None) and (root.right is None):
            return 1

        # 2. 如果左边节点不为None则递归左边节点
        val = 0
        if root.left is not None:
            val = max(self.maxDepth(root.left), val)
        # 3. 如果有右边节点不为None则递归右边节点
        if root.right is not None:
            val = max(self.maxDepth(root.right), val)

        # 4. 返回左边右边的最大值加1
        return val + 1


if __name__ == '__main__':
    val_list = [3, 9, 20, None, None, 15, 7]
    root = None
    node_list = []
    is_left = TreeNode
    for val in val_list:
        new_node = TreeNode(val) if val is not None else None
        if root is None:
            root = new_node

        if len(node_list) == 0:
            node_list.append(new_node)
            node_list.append(new_node)
            continue

        if new_node is not None:
            node_list.append(new_node)
            node_list.append(new_node)

        this_node = node_list.pop(0)
        if is_left:
            this_node.left = new_node
            is_left = False
        else:
            this_node.right = new_node
            is_left = True

    depth = Solution().maxDepth(root)
    print(depth)




