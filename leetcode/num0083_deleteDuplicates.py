# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0083_deleteDuplicates.py
@Time: 2020-07-01 12:50
@Last_update: 2020-07-01 12:50
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
        return f'(val:{self.val}, next:{self.next})'


class Solution:
    """
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
    """
    def deleteDuplicates(self, head):
        """
        整体流程：
        1. 遍历所有节点
        2. 如果下一个节点和自己不同，则移动到下一个节点
        3. 如果下一个节点和自己相同，则改变连接
        4. 如果是None则退出
        """
        if head is None:
            return head

        this_node = head
        # 1. 遍历所有节点
        while True:
            # 4. 如果是None则退出
            if this_node.next is None:
                break
            # 2. 如果下一个节点和自己不同，则移动到下一个节点
            elif this_node.val != this_node.next.val:
                this_node = this_node.next
            # 3. 如果下一个节点和自己相同，则改变连接
            else:
                this_node.next = this_node.next.next

        return head


def create_link(nums):
    head = None
    last = None
    for num in nums:
        this_node = ListNode(num)
        if head is None:
            head = this_node
            last = this_node
            continue

        last.next = this_node
        last = this_node

    return head


if __name__ == '__main__':
    nums = [1,1,2]
    # nums = [1,1,2,3,3]
    head = create_link(nums)
    print(Solution().deleteDuplicates(head))