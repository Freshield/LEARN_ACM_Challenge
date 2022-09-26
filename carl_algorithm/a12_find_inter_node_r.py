# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a12_find_inter_node_r.py
@Time: 2022-10-05 21:31
@Last_update: 2022-10-05 21:31
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


def find_inter_node(head_a, head_b):
    """
    找出两个链表相交的起始节点
    整体流程：
    1. 构建node的hash值set
    2. 循环直到head a或者head b都为None
    3. 如果head a为None则跳过
    4. 如果head a在hash值set则返回head a
    5. 否则把head a的hash放到set中，head a为head a的下一个
    6. 如果head b为None则跳过
    7. 如果head b在hash值set则返回head b
    8. 否则把head b的hash放到set中，head b为head b的下一个
    """
    # 1. 构建node的hash值set
    hash_set = set()

    #  2. 循环直到head a或者head b都为None
    while not ((head_a is None) and (head_b is None)):
        # 3. 如果head a为None则跳过
        if head_a is not None:
            # 4. 如果head a在hash值set则返回head a
            if hash(head_a) in hash_set:
                return head_a
            # 5. 否则把head a的hash放到set中，head a为head a的下一个
            hash_set.add(hash(head_a))
            head_a = head_a.next

        # 6. 如果head b为None则跳过
        if head_b is not None:
            # 7. 如果head b在hash值set则返回head b
            if hash(head_b) in hash_set:
                return head_b
            # 8. 否则把head b的hash放到set中，head b为head b的下一个
            hash_set.add(hash(head_b))
            head_b = head_b.next

    return None


if __name__ == '__main__':
    head_a = link_list([0, 9, 1])
    head_b = link_list([3])
    inter = link_list([2, 4])
    node = head_a
    while node.next is not None:
        node = node.next
    node.next = inter
    node = head_b
    while node.next is not None:
        node = node.next
    node.next = inter

    print(head_a)
    print(head_b)

    print(find_inter_node(head_a, head_b))
