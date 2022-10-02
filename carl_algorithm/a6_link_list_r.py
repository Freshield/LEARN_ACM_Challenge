# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_link_list_r.py
@Time: 2022-09-08 20:54
@Last_update: 2022-09-08 20:54
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}->{self.next}'


def link_list(head_list):
    """
    构建链表节点
    """
    fake_head_node = ListNode(None)
    last_node = fake_head_node
    for val in head_list:
        this_node = ListNode(val)
        last_node.next = this_node
        last_node = this_node

    return fake_head_node.next


if __name__ == '__main__':
    head = [1, 2, 6, 3, 4, 5, 6]
    print(link_list(head))
