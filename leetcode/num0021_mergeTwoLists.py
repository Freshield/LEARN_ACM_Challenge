# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0021_mergeTwoLists.py
@Time: 2020-04-18 22:29
@Last_update: 2020-04-18 22:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%s %s' % (self.val, self.next)

class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        """
        将两个升序链表合并为一个新的升序链表并返回。
        新链表是通过拼接给定的两个链表的所有节点组成的。
        解法：
        通过递归来生成链表，保证l1为小的那个值
        """
        if (l1 is not None) and (l2 is not None):
            if l1.val > l2.val:
                l1, l2 = l2, l1

            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 if l1 is not None else l2



if __name__ == '__main__':
    list1 = [2]
    list2 = [1]
    l1 = None
    for i in range(len(list1)-1, -1, -1):
        new_node = ListNode(list1[i])
        new_node.next = l1
        l1 = new_node
    print(l1)
    l2 = None
    for i in range(len(list2)-1, -1, -1):
        new_node = ListNode(list2[i])
        new_node.next = l2
        l2 = new_node
    print(l2)
    l3 = Solution().mergeTwoLists(l1, l2)
    print(l3)

