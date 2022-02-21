# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a43_find_loop_link.py
@Time: 2022-04-20 14:24
@Last_update: 2022-04-20 14:24
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


def find_loop_link(head):
    """
    找出链表循环的节点
    增加是否遍历过的attribute
    """
    this_node = head
    node_dict = dict()
    while True:
        # 如果到头了则返回None
        if this_node is None:
            return None

        node_hash = hash(this_node)
        # 如果access为True则表示访问过了
        if node_hash in node_dict:
            return this_node

        node_dict[node_hash] = True
        this_node = this_node.next


if __name__ == '__main__':
    nums = [3, 2, 0, -4]
    nums = nums[::-1]
    last_node = None
    for num in nums:
        this_node = ListNode(num, last_node)
        last_node = this_node

    link_node = None
    begin_node = last_node
    while last_node.next is not None:
        last_node = last_node.next
        if last_node.val == 2:
            link_node = last_node

    last_node.next = link_node
    print(link_node)
    print(last_node)
    inter_node = find_loop_link(begin_node)
    print(inter_node)