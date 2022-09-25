# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a13_find_loop_link_r.py
@Time: 2022-10-07 22:02
@Last_update: 2022-10-07 22:02
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


def find_loop_link(head):
    """
    找到循环的入口位置
    1. 构建需要的set
    2. 遍历head直到head为None
    3. 如果在set中找到head的hash，则返回head
    4. 不在则把head的hash放到set中
    """
    # 1. 构建需要的set
    node_set = set()

    # 2. 遍历head直到head为None
    while not (head is None):
        head_hash = hash(head)
        # 3. 如果在set中找到head的hash，则返回head
        if head_hash in node_set:
            return head
        # 4. 不在则把head的hash放到set中
        node_set.add(head_hash)
        head = head.next

    return None


if __name__ == '__main__':
    node_list = [3, 2, 0, -4]
    pos = 1
    fake_head = ListNode(None)
    link_node, last_node = None, fake_head
    for index, num in enumerate(node_list):
        this_node = ListNode(num)
        last_node.next = this_node
        last_node = this_node
        if index == pos:
            link_node = this_node

    this_node.next = link_node
    head = fake_head.next
    print(link_node.val)

    loop_node = find_loop_link(head)
    print(loop_node.val)


