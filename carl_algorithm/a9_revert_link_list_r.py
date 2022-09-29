# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a9_revert_link_list_r.py
@Time: 2022-09-19 21:13
@Last_update: 2022-09-19 21:13
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


def revert_link_list(head):
    """
    反转链表
    整体流程：
    1. 创建last, this，next指针
    2. 遍历直到this为None
    3. 进行交换
    """
    # 1. 创建last, this，next指针
    last_n, this_n = None, head

    # 2. 遍历直到this为None
    while this_n is not None:
        next_n = this_n.next
        # 3. 进行交换
        this_n.next = last_n
        last_n = this_n
        this_n = next_n

    return last_n


if __name__ == '__main__':
    head = link_list(range(6))
    print(head)
    print(revert_link_list(head))
