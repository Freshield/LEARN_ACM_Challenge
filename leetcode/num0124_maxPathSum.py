#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0124_maxPathSum.py
@Time: 2020-05-11 10:16
@Last_update: 2020-05-11 10:16
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
    给定一个非空二叉树，返回其最大路径和。
    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
    解法：
    使用递归，一共两种情况，一个是左中右的情况，但是这种情况无法继续向上传播，所有需要全局最大值进行记录
    另一种就是当前节点和左右中最大的值继续向上传
    """
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root, is_root=True):
        """
        整体流程：
        1. 结束条件：如果是None则为0
        2. 得到左侧
        3. 得到右侧
        4. 看是否需要更新最大值
        5. 进行返回
        """
        # 1. 结束条件：如果是None则为0
        if root is None:
            return 0

        # 2. 得到左侧
        left_part = max(0, self.maxPathSum(root.left, False))
        # 3. 得到右侧
        right_part = max(0, self.maxPathSum(root.right, False))

        # 4. 看是否需要更新最大值
        self.max_sum = max(self.max_sum, root.val + left_part + right_part)

        # 5. 进行返回
        if not is_root:
            return root.val + max(left_part, right_part)
        else:
            return self.max_sum


def create_tree(val_list):
    node_queue = []
    head = None
    for val in val_list:
        this_node = TreeNode(val)
        if val is not None:
            node_queue.append(this_node)

        if head is None:
            head = this_node
            continue

        last_node = node_queue[0]
        if last_node.left is None:
            last_node.left = this_node
        elif last_node.right is None:
            last_node.right = this_node
            if last_node.left.val is None:
                last_node.left = None
            if last_node.right.val is None:
                last_node.right = None

            node_queue.pop(0)

    return head


if __name__ == '__main__':
    val_list = [-10,9,20,None,None,15,7]
    # val_list = [1,2,3]
    # val_list = [1,2]
    # val_list = [1,-2,-3,1,3,-2,None,-1]
    head = create_tree(val_list)
    print(head)
    print(Solution().maxPathSum(head))