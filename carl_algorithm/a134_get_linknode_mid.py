# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a134_get_linknode_mid.py
@Time: 2022-10-24 14:23
@Last_update: 2022-10-24 14:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a6_link_list_r import link_list, ListNode


def get_linknode_mid(in_head):
    """
    得到链表中间的节点
    1. 处理特殊情况
    2. 创建快慢节点
    3. 遍历，条件为快节点不为空
    4. 如果快节点的下一个节点为空，？
    5. 如果快节点的下下个节点为空，？
    6. 快慢节点都走一步以及两步
    """
    # 1. 处理特殊情况
    if (in_head is None) or (in_head.next is None):
        return in_head
    if in_head.next.next is None:
        return in_head.next
    # 2. 创建快慢节点
    slow, fast = in_head, in_head.next.next
    # 3. 遍历，条件为快节点不为空
    while fast is not None:
        # 4. 如果快节点的下一个节点为空，？
        if fast.next is None:
            slow = slow.next
            break
        # 5. 如果快节点的下下个节点为空，？
        if fast.next.next is None:
            slow = slow.next.next
            break
        # 6. 快慢节点都走一步以及两步
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    head = link_list([i+1 for i in range(5)])
    print(head)
    print(get_linknode_mid(head))
