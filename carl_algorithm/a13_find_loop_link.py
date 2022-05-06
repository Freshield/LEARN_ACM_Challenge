# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a13_find_loop_link.py
@Time: 2022-04-13 15:26
@Last_update: 2022-04-13 15:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a6_link_list import ListNode


def find_loop_link(head):
    """
    找出链表循环的节点
    1. 快慢指针
    2. 快指针每次走两步，慢指针每次走一步，直到相遇
    3. 建立相遇指针
    4. 遍历直到和慢指针相遇
    """
    if head is None:
        return None
    # 1. 建立快慢指针
    slow_index, fast_index = head, head
    # 2. 快指针每次走两步，慢指针每次走一步，直到相遇
    while (slow_index.next is not None) and (fast_index.next is not None) and (fast_index.next.next is not None):
        slow_index = slow_index.next
        fast_index = fast_index.next.next

        if slow_index is fast_index:
            # 3. 建立相遇指针
            meet_index = head
            # 4. 遍历直到和慢指针相遇
            while meet_index is not slow_index:
                meet_index = meet_index.next
                slow_index = slow_index.next

            return meet_index

    return None


if __name__ == '__main__':
    nums = [3, 2, 0, -4]
    nums = nums[::-1]
    last_node = None
    for num in nums:
        this_node = ListNode(num, last_node)
        last_node = this_node

    link_node = None
    begin_node = last_node
    while last_node.next is not None:
        last_node = last_node.next
        if last_node.val == 2:
            link_node = last_node

    last_node.next = link_node
    print(link_node)
    print(last_node)
    inter_node = find_loop_link(begin_node)
    print(inter_node)
