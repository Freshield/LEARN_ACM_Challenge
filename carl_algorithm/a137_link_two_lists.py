# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a137_link_two_lists.py
@Time: 2022-10-24 19:16
@Last_update: 2022-10-24 19:16
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


def link_two_lists(list1, list2):
    """
    链接两个有序链表，使用双指针
    1. 处理特殊情况
    2. 创建虚拟头指针，以及链表指针
    3. 遍历，条件为list1不为None或者list2不为None
    4. 如果right为None，或者left的值小于等于right的值，则连接left，left断开
    5. 如果left为None，或者left的值大于right的值，则连接right，right断开
    """
    # 1. 处理特殊情况
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    # 2. 创建虚拟头指针，以及链表指针
    res_p = ListNode(None)
    fake_head = res_p
    # 3. 遍历，条件为list1不为None或者list2不为None
    while (list1 is not None) or (list2 is not None):
        # 4. 如果right为None，或者left的值小于等于right的值，则连接left，left断开
        if (list1 is not None) and ((list2 is None) or (list1.val <= list2.val)):
            res_p.next = list1
            list1 = list1.next
            res_p = res_p.next
            res_p.next = None
            continue
        # 5. 如果left为None，或者left的值大于right的值，则连接right，right断开
        if (list2 is not None) and ((list1 is None) or (list1.val > list2.val)):
            res_p.next = list2
            list2 = list2.next
            res_p = res_p.next
            res_p.next = None

    return fake_head.next


if __name__ == '__main__':
    list1 = link_list([1, 2, 4])
    list2 = link_list([1, 3, 4])
    print(link_two_lists(list1, list2))
