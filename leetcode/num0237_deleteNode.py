# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0237_deleteNode.py
@Time: 2020-05-01 19:11
@Last_update: 2020-05-01 19:11
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，
    你将只被给定要求被删除的节点。
    说明:
    链表至少包含两个节点。
    链表中所有节点的值都是唯一的。
    给定的节点为非末尾节点并且一定是链表中的一个有效节点。
    不要从你的函数中返回任何结果。
    """
    def deleteNode(self, node):
        """
        整体流程：
        1. 得到下个节点的值
        2. 更换自己的next
        """
        # 1. 得到下个节点的值
        node.val = node.next.val
        node.next = node.next.next

    def deleteTheNode(self, head, node):
        """
        整体流程：
        1. 遍历列表
        2. 如果是目标节点则调用deleteNode函数
        """
        # 1. 遍历列表
        while True:
            if head is None:
                break
            # 2. 如果是目标节点则调用deleteNode函数
            if head.val == node:
                self.deleteNode(head)
                break

            head = head.next



def print_node(root):
    while True:
        if root is None:
            break
        print(root.val)
        root = root.next


if __name__ == '__main__':
    num_list = [4, 5, 1, 9]
    root = None
    last_node = None
    for num in num_list:
        new_node = ListNode(num)
        if root is None:
            root = new_node
            last_node = new_node
            continue
        last_node.next = new_node
        last_node = new_node

    print_node(root)
    print()
    node = 5
    Solution().deleteTheNode(root, node)
    print_node(root)