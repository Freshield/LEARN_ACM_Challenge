# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a10_twotwo_revert_link_list_r.py
@Time: 2022-09-19 21:27
@Last_update: 2022-09-19 21:27
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


def twotwo_revert_link_list(head):
    """
    两两交换链表中的节点
    1. 创建pre，cur节点
    2. 遍历直到当前节点不为None，下个节点不为None
    3. 进行交换
    """
    # 1. 创建pre，cur节点
    fake_head, cur = ListNode(None), head
    fake_head.next = cur
    pre = fake_head

    # 2. 遍历直到当前节点不为None，下个节点不为None
    while (cur is not None) and (cur.next is not None):
        # 3. 进行交换
        nex = cur.next
        nnex = cur.next.next

        pre.next = nex
        cur.next = nnex
        nex.next = cur

        pre = cur
        cur = nnex

    return fake_head.next


if __name__ == '__main__':
    head = link_list(range(5))
    print(head)
    print(twotwo_revert_link_list(head))

