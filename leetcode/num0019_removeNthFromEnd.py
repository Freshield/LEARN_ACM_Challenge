# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0019_removeNthFromEnd.py
@Time: 2020-05-02 10:12
@Last_update: 2020-05-02 10:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
    说明：
    给定的 n 保证是有效的。
    进阶：
    你能尝试使用一趟扫描实现吗？
    """
    def removeNthFromEnd(self, head, n):
        """
        使用双指针法
        1. 先设置一个空节点指向head
        2. 然后设置快慢两个节点
        3. 遍历先把快节点放到多n的地方
        4. 当快节点为None时，修改慢节点的位置
        """
        # 1. 先设置一个空节点指向head
        null = ListNode(None)
        null.next = head
        # 2. 然后设置快慢两个节点
        slow = null
        fast = null
        # 3. 遍历先把快节点放到多n的地方
        for i in range(n):
            fast = fast.next
        # 4. 当快节点为None时，修改慢节点的位置
        while True:
            if fast.next is None:
                slow.next = slow.next.next
                break
            fast = fast.next
            slow = slow.next

        return null.next


    def removeNthFromEnd_list(self, head, n):
        """
        整体流程：
        1. 生成暂存列表
        2. 遍历node，看是否到了结尾
        3. 把node放到暂存列表中
        4. 如果到了结尾则删掉列表的第1个元素
        5. 处理特殊情况
        """
        # 1. 生成暂存列表
        node_tmp_list = []
        begin = head
        # 2. 遍历node，看是否到了结尾
        while True:
            if head is not None:
                # 3. 把node放到暂存列表中
                node_tmp_list.append(head)
                if len(node_tmp_list) == (n+2):
                    node_tmp_list.pop(0)
                head = head.next
            else:
                if len(node_tmp_list) == (n+1):
                    node_tmp_list[0].next = node_tmp_list[1].next
                # 5. 处理特殊情况
                elif len(node_tmp_list) == 0:
                    return begin
                elif len(node_tmp_list) == 1:
                    return None
                elif len(node_tmp_list) == n:
                    return node_tmp_list[1]

                break

        return begin

def print_link(head):
    while True:
        if head is None:
            break
        print('%s ' % head.val, end='')
        head = head.next

    print()


if __name__ == '__main__':
    num_list = [1,2,3,4,5]
    n = 2
    # num_list = [1]
    # n = 1
    # num_list = [1,2]
    # n = 2
    head = None
    last = None
    for num in num_list:
        this_node = ListNode(num)
        if head is None:
            head = this_node
            last = this_node
            continue
        last.next = this_node
        last = this_node

    print_link(head)
    begin = Solution().removeNthFromEnd(head, n)
    print_link(begin)
    print(begin)