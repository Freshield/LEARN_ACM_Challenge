# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a159_relink_link_list.py
@Time: 2022-11-09 19:45
@Last_update: 2022-11-09 19:45
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


def find_mid_node(head):
    """
    找到链表的中心节点，使用快慢指针
    1. 创建left，right指针
    2. 遍历，条件为right的下一个，下下个不为None
    3. left为next，right为next next
    """
    dummy_head = ListNode(None, head)
    # 1. 创建left，right指针
    left, right = head, head
    # 2. 遍历，条件为right的下一个，下下个不为None
    while (right is not None) and (right.next is not None):
        # 3. left为next，right为next next
        dummy_head = left
        left = left.next
        right = right.next.next

    return left, dummy_head


def reverse_link_list(head):
    """
    翻转链表
    1. 生成虚拟头指针
    2. 遍历，条件为head不为None
    3. 创建next
    4. 调换head的指向
    5. 更新dummy head和head
    """
    # 1. 生成虚拟头指针
    dummy_head = None
    # 2. 遍历，条件为head不为None
    while head is not None:
        # 3. 创建next
        next_node = head.next
        # 4. 调换head的指向
        head.next = dummy_head
        # 5. 更新dummy head和head
        dummy_head = head
        head = next_node

    return dummy_head


def relink_link_list(head):
    """
    对链表重新排序
    1. 处理特殊情况
    2. 找到链表的中心点，并拆开
    3. 把后边的节点进行反序
    4. 遍历，条件为first head不为空
    5. 创建first next，second next
    6. 更新second head到first link中
    7. 更新first head，second head
    8. 遍历结束后，把second剩下的部分连接到first link中
    """
    # 1. 处理特殊情况
    if (head is None) or (head.next is None) or (head.next.next is None):
        return head
    # 2. 找到链表的中心点，并拆开
    mid, before_mid = find_mid_node(head)
    before_mid.next = None
    # 3. 把后边的节点进行反序
    first_head = head
    second_head = reverse_link_list(mid)
    # 4. 遍历，条件为first head不为空
    dummy_head = head
    while first_head is not None:
        dummy_head = second_head
        # 5. 创建first next，second next
        first_next, second_next = first_head.next, second_head.next
        # 6. 更新second head到first link中
        first_head.next = second_head
        second_head.next = first_next
        # 7. 更新first head，second head
        first_head = first_next
        second_head = second_next

    # 8. 遍历结束后，把second剩下的部分连接到first link中
    dummy_head.next = second_head

    return head


if __name__ == '__main__':
    head = link_list([i+1 for i in range(5)])
    print(head)
    print(relink_link_list(head))
