# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a7_remove_list_node_r.py
@Time: 2022-09-08 21:00
@Last_update: 2022-09-08 21:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a6_link_list_r import ListNode


def remove_list_node(head, val):
    """
    删除相应值的节点
    整体流程：
    1. 构建虚拟头结点
    2. 遍历链表直到node为None
    3. 如果遇到和val相同的则让上一个节点的next直接为下一个
    """
    # 1. 构建虚拟头结点
    fake_head_node = ListNode(None, head)
    last_node = fake_head_node
    this_node = head
    # 2. 遍历链表直到node为None
    while this_node is not None:
        # 3. 如果遇到和val相同的则让上一个节点的next直接为下一个
        if this_node.val == val:
            last_node.next = this_node.next
        else:
            last_node = this_node
        this_node = this_node.next

    return fake_head_node.next


if __name__ == '__main__':
    from a6_link_list_r import link_list
    head = [7, 7]
    val = 7
    head = link_list(head)
    print(remove_list_node(head, val))

