#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0236_lowestCommonAncestor.py
@Time: 2020-05-09 10:33
@Last_update: 2020-05-09 10:33
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
        return '{left: %s, val: %s, right: %s}' % (str(self.left), str(self.val), str(self.right))


class Solution:
    """
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
    最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
    解法：
    使用递归的方法，一共两种情况，p，q在同一侧，p,q在两侧
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        整体流程：
        1. 结束条件为叶节点或者等于p或q
        2. 得到左边的结果
        3. 得到右边的结果
        4. 如果左边右边都不是None代表是p,q在两边，则直接返回当前节点
        5. 如果左边是None则代表p,q都在右边，则直接返回右边结果
        6. 如果右边是None则代表p,q都在左边，则直接返回左边结果
        """
        # 1. 结束条件为叶节点或者等于p或q
        if (root is None) or (root.val == p) or (root.val == q):
            return root

        # 2. 得到左边的结果
        left_rst = self.lowestCommonAncestor(root.left, p, q)
        # 3. 得到右边的结果
        right_rst = self.lowestCommonAncestor(root.right, p, q)

        # 4. 如果左边右边都不是None代表是p,q在两边，则直接返回当前节点
        if (left_rst is not None) and (right_rst is not None):
            return root
        # 5. 如果左边是None则代表p,q都在右边，则直接返回右边结果
        elif left_rst is None:
            return right_rst
        # 6. 如果右边是None则代表p,q都在左边，则直接返回左边结果
        else:
            return left_rst


def create_tree(val_list):
    begin = None
    queue = []
    for val in val_list:
        this_node = TreeNode(val)
        if val is not None:
            queue.append(this_node)
        if begin is None:
            begin = this_node
            continue

        last_node = queue[0]
        if last_node.left is None:
            last_node.left = this_node
        else:
            last_node.right = this_node
            last_node.right = last_node.right if last_node.right.val is not None else None
            last_node.left = last_node.left if last_node.left.val is not None else None
            queue.pop(0)

    return begin


if __name__ == '__main__':
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 4
    root = create_tree(root)
    print(root)
    print(Solution().lowestCommonAncestor(root, p, q).val)