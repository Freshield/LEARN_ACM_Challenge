# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0142_detectCycle.py
@Time: 2020-05-21 10:15
@Last_update: 2020-05-21 10:15
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
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    说明：不允许修改给定的链表。
    解法：
    使用快慢指针，当快指针碰到慢指针时为有环，设环的起始点前一共a个点，环内一共b个点
    碰到时：fast=slow+nb, fast=2*slow, fast=2nb, slow=nb
    入口的节点：k=a+nb，所以让fast回到0，每次走一步，这样再和slow相遇
    就走了fast=a, slow=a+nb，他们相遇的点就是入口点
    """
    def detectCycle(self, head):
        """
        整体流程：
        1. 先创建快慢指针
        2. 遍历看是否有环
        3. 如果有环，再遍历找到交叉节点
        """
        if head is None:
            return None
        # 1. 先创建快慢指针
        slow = head
        fast = head

        # 2. 遍历看是否有环
        while True:
            if (fast.next is None) or (fast.next.next is None):
                return None

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        # 3. 如果有环，再遍历找到交叉节点
        fast = head
        while True:
            if fast == slow:
                return fast

            fast = fast.next
            slow = slow.next


def create_link_list(head, pos):
    begin_node = None
    loop_node = None
    last_node = None
    for num, val in enumerate(head):
        this_node = ListNode(val)
        if num == pos:
            loop_node = this_node

        if begin_node is None:
            begin_node = this_node
            last_node = this_node
            continue

        last_node.next = this_node
        last_node = this_node

    last_node.next = loop_node

    return begin_node, loop_node


if __name__ == '__main__':
    head = [3, 2, 0, -4]
    pos = 1
    head, loop = create_link_list(head, pos)
    print(head.val)
    print(loop.val)
    # rst = Solution().detectCycle(head)
    # print(rst.val)
    rst = Solution().detectCycle_me(head)
    print(rst.val)