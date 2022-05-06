# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0025_reverseKGroup.py
@Time: 2020-07-06 10:28
@Last_update: 2020-07-06 10:28
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

    def __str__(self):
        return f'{self.val}, {self.next}'


class Solution:
    """
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
    解法：
    使用多指针，遍历调换子链表
    """
    def reverse_sub(self, head, tail):
        """
        反转子链表
        整体流程：
        1. 生成pre，next等节点
        2. 结束条件为pre和tail相等
        3. 调换节点连接顺序
        """
        # 1. 生成pre，next等节点
        pre = tail.next
        p = head

        # 2. 结束条件为pre和tail相等
        while pre != tail:
            # 3. 调换节点连接顺序
            nex = p.next
            p.next = pre
            pre = p
            p = nex

        return tail, head

    def reverseKGroup(self, head, k):
        """
        整体流程：
        0. 进行特判
        1. 创建hair节点
        2. 遍历k个节点，如果不足k则直接返回头节点
        3. 对k节点内部进行掉转
        4. 进行连接
        """
        # 0. 进行特判
        if head is None or k <= 1:
            return head

        # 1. 创建hair节点
        hair = ListNode(None)
        hair.next = head
        pre = hair
        tail = hair

        while head is not None:
            # 2. 遍历k个节点，如果不足k则直接返回头节点
            for i in range(k):
                tail = tail.next
                if tail is None:
                    return hair.next

            # 3. 对k节点内部进行掉转
            nex = tail.next
            head, tail = self.reverse_sub(head, tail)

            # 4. 进行连接
            pre.next = head
            tail.next = nex

            pre = tail
            head = tail.next

        return hair.next


def create_link_list(nums):
    head, last = None, None
    for num in nums:
        this_node = ListNode(num)
        if head is None:
            head = this_node
            last = this_node
            continue

        last.next = this_node
        last = this_node

    return head, last


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 3
    head, tail = create_link_list(nums)

    head = Solution().reverseKGroup(head, k)
    print(head)