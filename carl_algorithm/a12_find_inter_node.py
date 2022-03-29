# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a12_find_inter_node.py
@Time: 2022-04-13 14:51
@Last_update: 2022-04-13 14:51
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


def find_inter_node(head1, head2):
    """
    找到交叉的节点
    通过对齐结尾来找有没有相同的节点
    1. 得到link1的长度和link2的长度
    2. 让长的一边移到差值共同长度部分
    3. 开始遍历看是否有共同节点
    """
    # 1. 得到link1的长度和link2的长度
    link1_length, link2_length = 0, 0
    tmp_node = head1
    while tmp_node is not None:
        link1_length += 1
        tmp_node = tmp_node.next
    tmp_node = head2
    while tmp_node is not None:
        link2_length += 1
        tmp_node = tmp_node.next

    # 2. 让长的一边移到差值共同长度部分
    long_head = head1 if link1_length > link2_length else head2
    short_head = head1 if link1_length <= link2_length else head2
    diff = abs(link1_length - link2_length)
    for _ in range(diff):
        long_head = long_head.next

    # 3. 开始遍历看是否有共同节点
    while (long_head is not None) and (short_head is not None):
        if long_head is short_head:
            return long_head

        long_head = long_head.next
        short_head = short_head.next

    return None


if __name__ == '__main__':
    nums1 = [1, 4]
    nums2 = [1, 0, 5]
    merge = [5, 4, 8]
    last_node = None
    for num in merge:
        this_node = ListNode(num, last_node)
        last_node = this_node
    merge_node = last_node

    for num in nums1:
        this_node = ListNode(num, last_node)
        last_node = this_node
    head1 = last_node

    last_node = merge_node
    for num in nums2:
        this_node = ListNode(num, last_node)
        last_node = this_node
    head2 = last_node

    head1 = ListNode(1)
    head2 = head1
    print(head1)
    print(head2)
    inter_node = find_inter_node(head1, head2)
    print(inter_node)
