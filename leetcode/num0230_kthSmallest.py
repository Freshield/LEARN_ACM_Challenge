# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0230_kthSmallest.py
@Time: 2020-05-05 14:27
@Last_update: 2020-05-05 14:27
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


class Solution:
    """
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
    说明：
    你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
    解法：
    使用中序遍历，找出第k个元素
    """
    def mid_search_yield(self, root):
        """
        中序遍历，yield版本
        """
        if root.left is not None:
            yield from self.mid_search_yield(root.left)

        yield root.val

        if root.right is not None:
            yield from self.mid_search_yield(root.right)

    def kthSmallest(self, root, k):
        """
        整体流程：
        1. 使用中序遍历查找
        2. 使用yield版本的遍历，直接得到第k-1个
        """
        gen = self.mid_search_yield(root)
        for i in range(k):
            num = next(gen)

        return num

    def mid_search(self, root):
        """
        中序遍历
        """
        if root is None:
            return []

        rst_list = self.mid_search(root.left)
        rst_list.append(root.val)
        rst_list += self.mid_search(root.right)

        return rst_list

    def kthSmallest_list(self, root, k):
        """
        整体流程：
        1. 使用递归，获得中序的列表
        2. 找到第k-1个元素
        """
        mid_search_list = self.mid_search(root)

        return mid_search_list[k-1]


def create_tree(root):
    """
    使用前序生成树
    """
    queue = []
    begin = None
    for val in root:
        tree_node = TreeNode(val)
        if begin is None:
            begin = tree_node
            queue.append(begin)
            continue

        if queue[0].left is None:
            queue[0].left = tree_node
        elif queue[0].right is None:
            queue[0].right = tree_node

            pop_node = queue.pop(0)
            pop_node.left = pop_node.left if pop_node.left.val is not None else None
            pop_node.right = pop_node.right if pop_node.right.val is not None else None

        if tree_node.val is not None:
            queue.append(tree_node)

    return begin


def print_tree(root):
    """
    使用bfs打印树
    """
    queue = [root]
    while True:
        if len(queue) == 0:
            break
        for i in range(len(queue)):
            this_node = queue.pop(0)
            if this_node is not None:
                print(this_node.val, end=' ')
                queue.append(this_node.left)
                queue.append(this_node.right)
            else:
                print(this_node, end=' ')

        print()


if __name__ == '__main__':
    root = [3, 1, 4, None, 2]
    root = create_tree(root)
    print_tree(root)
    k_node = Solution().kthSmallest(root, 1)
    print(k_node)
