# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0235_lowestCommonAncestor.py
@Time: 2020-06-02 10:42
@Last_update: 2020-06-02 10:42
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
    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
    最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
    解法：
    使用迭代，通过比较p,q的值，如果在两边则目前为公共祖先
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        整体流程：
        1. 处理特殊情况
        2. 遍历当前树
        3. 如果都大则转到右树
        4. 如果都小则转到左树
        5. 如果一边一个则返回当前节点
        """
        # 1. 处理特殊情况
        if root is None:
            return None

        node = root
        # 2. 遍历当前树
        while node is not None:
            # 3. 如果都大则转到右树
            if (p.val > node.val) and (q.val > node.val):
                node = node.right
            # 4. 如果都小则转到左树
            elif (p.val < node.val) and (q.val < node.val):
                node = node.left
            # 5. 如果一边一个则返回当前节点
            else:
                return node

        return None


def create_tree(nums):
    begin_node = None
    node_list = []

    for num in nums:
        this_node = TreeNode(num)
        if num is not None:
            node_list.append(this_node)

        if begin_node is None:
            begin_node = this_node
            continue

        if node_list[0].left is None:
            node_list[0].left = this_node
        else:
            node_list[0].right = this_node if this_node.val is not None else None
            node_list[0].left = node_list[0].left if node_list[0].left.val is not None else None
            node_list.pop(0)

    return begin_node


if __name__ == '__main__':
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = create_tree(root)
    p = TreeNode(2)
    q = TreeNode(4)
    print(root)
    print(Solution().lowestCommonAncestor(root, p, q).val)