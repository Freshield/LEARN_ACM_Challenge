# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a11_del_last_n_node_r.py
@Time: 2022-09-21 14:32
@Last_update: 2022-09-21 14:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a6_link_list_r import ListNode, link_list


def del_last_n_node(head, n):
    """
    删除倒数第n个节点，使用双指针法来进行删除
    整体流程：
    1. 生成需要的快指针和慢指针以及虚拟头结点
    2. 让快指针走n步，如果快指针为None则直接返回
    3. 让快慢指针一起走，直到快指针的下一个为None
    4. 进行删除，并返回头结点
    """
    # 1. 生成需要的快指针和慢指针以及虚拟头结点
    fake_head = ListNode(None, head)
    fast_n, slow_n = fake_head, fake_head

    # 2. 让快指针走n步，如果快指针为None则直接返回
    for _ in range(n):
        fast_n = fast_n.next
        if fast_n is None:
            return fast_n.next

    # 3. 让快慢指针一起走，直到快指针的下一个为None
    while fast_n.next is not None:
        fast_n = fast_n.next
        slow_n = slow_n.next

    # 4. 进行删除，并返回头结点
    slow_n.next = slow_n.next.next

    return fake_head.next


if __name__ == '__main__':
    head = link_list(range(6))
    n = 1
    print(head)
    print(del_last_n_node(head, n))


