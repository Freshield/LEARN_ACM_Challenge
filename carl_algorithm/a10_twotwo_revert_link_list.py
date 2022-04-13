# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a10_twotwo_revert_link_list.py
@Time: 2022-04-13 12:03
@Last_update: 2022-04-13 12:03
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


def twotwo_revert_link_list(head):
    """
    两两反转链表
    使用两个指针达成
    1. 创建虚拟头指针
    2. 遍历开始，条件为都不为None
    3. 创建快慢指针
    4. 进行next的调换
    """
    # 1. 创建虚拟头指针以及快慢指针
    this_node = ListNode(None, head)
    fake_node = this_node
    # 2. 遍历开始，条件为都不为None
    while (this_node.next is not None) and (this_node.next.next is not None):
        # 3. 创建快慢指针
        next_node = this_node.next
        nnext_node = this_node.next.next

        next_node.next = nnext_node.next
        nnext_node.next = next_node
        this_node.next = nnext_node

        this_node = next_node

    return fake_node.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    nums = []
    nums = nums[::-1]
    last_node = None
    for num in nums:
        this_node = ListNode(num, last_node)
        last_node = this_node

    print(last_node)
    last_node = twotwo_revert_link_list(last_node)
    print(last_node)
