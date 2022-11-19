# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a79_link_inter.py
@Time: 2022-10-09 16:00
@Last_update: 2022-10-09 16:00
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


def link_inter(_head_a, _head_b):
    """
    判断两个链表是否相交
    1. 构建所需的set
    2. 遍历，条件为head_a为None，head_b也为None
    3. 如果head a不为None，看head a的hash是否在set中，如果在则返回True，否则放入set，并更新head a
    4. 如果head b不为None，看head b的hash是否在set中，如果在则返回True，否则放入set，并更新head b
    """
    # 1. 构建所需的set
    hash_set = set()
    #  2. 遍历，条件为head_a为None，head_b也为None
    while (_head_a is not None) or (_head_b is not None):
        # 3. 如果head a不为None，看head a的hash是否在set中，如果在则返回True，否则放入set，并更新head a
        if _head_a is not None:
            if hash(_head_a) in hash_set:
                return _head_a
            hash_set.add(hash(_head_a))
            _head_a = _head_a.next
        # 4. 如果head b不为None，看head b的hash是否在set中，如果在则返回True，否则放入set，并更新head b
        if _head_b is not None:
            if hash(_head_b) in hash_set:
                return _head_b
            hash_set.add(hash(_head_b))
            _head_b = _head_b.next

    return None


if __name__ == '__main__':
    head_a = link_list([1,2,3])
    head_b = link_list([4,5,6])
    inter = link_list([7,8,9])
    node = head_a
    while node.next is not None:
        node = node.next
    node.next = inter
    node = head_b
    while node.next is not None:
        node = node.next
    node.next = inter

    print(link_inter(head_a, head_b))

