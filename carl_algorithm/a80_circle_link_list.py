# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a80_circle_link_list.py
@Time: 2022-10-09 16:12
@Last_update: 2022-10-09 16:12
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


def circle_link_list(head):
    """
    判断链表是否有环
    1. 构建hash set
    2. 遍历，条件为head不为None
    3. 如果head在hash set中则返回True
    4. 否则添加到hash set，并更新head
    """
    # 1. 构建hash set
    hash_set = set()
    # 2. 遍历，条件为head不为None
    while head is not None:
        # 3. 如果head在hash set中则返回True
        if hash(head) in hash_set:
            return head
        # 4. 否则添加到hash set
        hash_set.add(hash(head))
        head = head.next

    return None


if __name__ == '__main__':
    head = link_list(range(6))
    node = head
    while node.next is not None:
        node = node.next
    node.next = head

    print(circle_link_list(head).val)
