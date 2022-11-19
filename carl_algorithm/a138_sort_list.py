# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a138_sort_list.py
@Time: 2022-10-25 09:54
@Last_update: 2022-10-25 09:54
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


def merge_seq_list(head_a, head_b):
    """
    合并两个有序链表
    1. 处理特殊情况
    2. 创建结果的虚拟节点
    3. 遍历，条件为head a和head b不同时为空
    4. 如果head a为空，则直接连接head b，并继续
    5. 如果head b为空，则直接连接head a，并继续
    6. 否则对比head a，head b的值，连接小的那个
    """
    # 1. 处理特殊情况
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a
    # 2. 创建结果的虚拟节点
    fake_head = ListNode(None)
    this_node = fake_head
    # 3. 遍历，条件为head a和head b不同时为空
    while not ((head_a is None) and (head_b is None)):
        # 4. 如果head a为空，则直接连接head b，并继续
        if head_a is None:
            this_node.next = head_b
            head_b = head_b.next
        # 5. 如果head b为空，则直接连接head a，并继续
        elif head_b is None:
            this_node.next = head_a
            head_a = head_a.next
        # 6. 否则对比head a，head b的值，连接小的那个
        elif head_a.val <= head_b.val:
            this_node.next = head_a
            head_a = head_a.next
        elif head_a.val > head_b.val:
            this_node.next = head_b
            head_b = head_b.next

        this_node = this_node.next
        this_node.next = None

    return fake_head.next


def split_list(head, steps):
    """
    从第n个节点切开链表
    1. 遍历steps减一步，如果中间head.next为None则直接返回
    2. 保存steps.next为res
    3. 断开，并返回res
    """
    if head is None:
        return None
    # 1. 遍历steps减一步，如果中间head.next为None则直接返回
    for i in range(steps - 1):
        if head.next is None:
            return None
        head = head.next
    # 2. 保存steps.next为res
    res = head.next
    # 3. 断开，并返回res
    head.next = None

    return res


def sort_list(head):
    """
    对链表进行排序
    1. 生成遍历间隔step，dummy
    2. 遍历获取链表长度
    3. 遍历，条件为间隔小于链表长度
    4. 初始化pre和cur指针
    5. 遍历，条件为cur不为空
    6. left指向cur，right指向split step的left，cur更新指向split step的right
    7. temp为合并后的left，right
    8. pre.next指向temp，并把pre移动到末尾
    9. step乘2
    """
    # 1. 生成遍历间隔step，dummy
    step, length = 1, 0
    dummy = head
    # 2. 遍历获取链表长度
    while dummy is not None:
        dummy = dummy.next
        length += 1
    dummy = ListNode(None, head)
    # 3. 遍历，条件为间隔小于链表长度
    while step <= length:
        # 4. 初始化pre和cur指针
        pre, cur = dummy, dummy.next
        # 5. 遍历，条件为cur不为空
        while cur is not None:
            # 6. left指向cur，right指向split step的left，cur更新指向split step的right
            left = cur
            right = split_list(left, step)
            cur = split_list(right, step)
            # 7. temp为合并后的left，right
            temp = merge_seq_list(left, right)
            # 8. pre.next指向temp，并把pre移动到末尾
            pre.next = temp
            while pre.next is not None:
                pre = pre.next
        step *= 2

    return dummy.next


if __name__ == '__main__':
    head = link_list([4, 3, 2, 6, 5, 7, 1])
    print(sort_list(head))

