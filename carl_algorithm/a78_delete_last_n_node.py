# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a78_delete_last_n_node.py
@Time: 2022-10-09 15:46
@Last_update: 2022-10-09 15:46
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


def delete_last_n_node(_head, n):
    """
    删除倒数第n个节点
    1. 构建fake_head，left，right指针
    2. 让right指针先跑n个节点
    3. 然后遍历，条件为right的下一个不为None
    4. 对left后的节点进行调整
    """
    # 1. 构建left，right指针
    fake_head = ListNode(None, _head)
    left, right = fake_head, fake_head
    # 2. 让right指针先跑n个节点
    for i in range(n+1):
        right = right.next
    # 3. 然后遍历，条件为right不为None
    while right is not None:
        left = left.next
        right = right.next
    # 4. 对left后的节点进行调整
    left.next = left.next.next

    return fake_head.next


if __name__ == '__main__':
    head = link_list(range(6))
    n = 2
    head = link_list([1])
    n = 1
    print(delete_last_n_node(head, n))
