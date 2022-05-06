# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a11_del_last_n_node.py
@Time: 2022-04-13 14:23
@Last_update: 2022-04-13 14:23
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


def del_last_n_node(head, n):
    """
    删除倒数第n个节点
    使用快慢指针的方法
    1. 生成快慢指针和虚拟头节点
    2. 让快指针移动n次
    3. 让快慢指针一起移动，直到快指针的下一个为None
    4. 使用慢指针来进行删除节点
    """
    # 1. 生成快慢指针和虚拟头节点
    fake_node = ListNode(None, head)
    slow_node = fake_node
    fast_node = fake_node
    # 2. 让快指针移动n次
    for _ in range(n):
        fast_node = fast_node.next

    # 3. 让快慢指针一起移动，直到快指针的下一个为None
    while fast_node.next is not None:
        fast_node = fast_node.next
        slow_node = slow_node.next

    # 4. 使用慢指针来进行删除节点
    slow_node.next = slow_node.next.next

    return fake_node.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    nums = [1]
    nums = [1, 2]
    n = 2
    n = 1
    n = 1
    nums = nums[::-1]
    last_node = None
    for num in nums:
        this_node = ListNode(num, last_node)
        last_node = this_node

    print(last_node)
    last_node = del_last_n_node(last_node, n)
    print(last_node)
