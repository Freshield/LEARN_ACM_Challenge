# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a77_revese_link_list.py
@Time: 2022-10-09 15:02
@Last_update: 2022-10-09 15:02
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


def reverse_link_list(head):
    """
    翻转链表
    1. 构建last节点，遍历节点
    2. 遍历节点，条件为node不为None
    3. 生成暂存next节点，并变化node的next指向
    4. 更新last和node
    5. 返回last
    """
    # 1. 构建last节点，遍历节点
    last, node = None, head
    # 2. 遍历节点，条件为node不为None
    while node is not None:
        # 3. 生成暂存next节点，并变化node的next指向
        tmp = node.next
        node.next = last
        # 4. 更新last和node
        last = node
        node = tmp

    # 5. 返回last
    return last


if __name__ == '__main__':
    head = link_list(range(5))
    print(head)
    print(reverse_link_list(head))
