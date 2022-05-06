# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a7_remove_list_node.py
@Time: 2022-04-12 15:27
@Last_update: 2022-04-12 15:27
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


def remove_list_node(list_node, val):
    """
    去除链表中的val值的节点
    1. 创建虚拟头结点
    2. 遍历到next为None
    3. 如果发现下一个的值和val相同则让next为自己的下一个的next
    4. 返回虚拟头结点的next
    """
    # 1. 创建虚拟头结点，上一个节点
    fake_head = ListNode(None, list_node)
    this_node = fake_head
    # 2. 遍历到next为None
    while this_node.next is not None:
        # 3. 如果发现下一个的值和val相同则让next为自己的下一个的next
        if this_node.next.val == val:
            this_node.next = this_node.next.next
        else:
            this_node = this_node.next

    return fake_head.next


if __name__ == '__main__':
    val = 6
    val = 7
    list_value = [1,2,6,3,4,5,6]
    list_value = []
    list_value = [7, 7, 7, 7]
    list_value = list_value[::-1]
    last_node = None
    for value in list_value:
        new_node = ListNode(value, last_node)
        last_node = new_node

    print(last_node)
    print(remove_list_node(last_node, val))
