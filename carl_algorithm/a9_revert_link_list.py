# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a9_revert_link_list.py
@Time: 2022-04-13 11:39
@Last_update: 2022-04-13 11:39
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


def revert_link_list(node):
    """
    反转链表
    使用快慢指针
    1. 创建快慢指针和中间暂存
    2. 遍历快指针，结束条件为快指针为None
    3. 把下一个存到暂存，快指针指向慢指针，然后都移动一位
    4. 返回慢指针
    """
    # 1. 创建快慢指针和中间暂存
    slow_index, fast_index = None, node
    # 2. 遍历快指针，结束条件为快指针为None
    while fast_index is not None:
        # 3. 把下一个存到暂存，快指针指向慢指针，然后都移动一位
        tmp = fast_index.next
        fast_index.next = slow_index
        slow_index = fast_index
        fast_index = tmp

    # 4. 返回慢指针
    return slow_index


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    nums = nums[::-1]
    last_node = None
    for num in nums:
        this_node = ListNode(num, last_node)
        last_node = this_node

    print(last_node)
    last_node = revert_link_list(last_node)
    print(last_node)
