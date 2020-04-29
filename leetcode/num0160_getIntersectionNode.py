# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0160_getIntersectionNode.py
@Time: 2020-05-04 21:45
@Last_update: 2020-05-04 21:45
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
    编写一个程序，找到两个单链表相交的起始节点。
    注意：
    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
    解法：
    1. 测量A和B的长度，然后从同样的长度开始
    2. 把A链接到B，再把B链接到A上，这样就可以保证长度一样且会相遇
    """
    def getIntersectionNode(self, headA, headB):
        """
        整体流程：
        1. 生成左右两个指针
        2. 遍历headA和headB
        3. 如果到达了结尾，则继续链接到对面的头节点
        """
        # 1. 生成左右两个指针
        point_a = headA
        point_b = headB

        # 2. 遍历headA和headB
        while True:
            if point_a == point_b:
                return point_b

            point_a = point_a.next if point_a is not None else headB
            point_b = point_b.next if point_b is not None else headA


    def getIntersectionNode_length(self, headA, headB):
        """
        整体流程：
        1. 遍历得到A和B的长度
        2. 把长的那个遍历长度差遍
        3. 遍历A和B看是否有相同的节点
        """
        # 1. 遍历得到A和B的长度
        lengthA = 0
        lengthB = 0
        loopA = headA
        while True:
            if loopA is None:
                break
            lengthA += 1
            loopA = loopA.next
        loopB = headB
        while True:
            if loopB is None:
                break
            lengthB += 1
            loopB = loopB.next

        # 2. 把长的那个遍历长度差遍
        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                headA = headA.next
        elif lengthB > lengthA:
            for i in range(lengthB - lengthA):
                headB = headB.next

        # 3. 遍历A和B看是否有相同的节点
        while True:
            if (headA is None) or (headB is None):
                return None

            if headA is headB:
                return headA

            headA = headA.next
            headB = headB.next


def create_link(list_a, list_b, index_a, index_b):
    """
    生成链表节点
    """
    begin_a = None
    last_a = None
    for i in range(index_a):
        this_node = ListNode(list_a[i])
        if begin_a is None:
            begin_a = this_node
            last_a = this_node
            continue

        last_a.next = this_node
        last_a = this_node

    begin_b = None
    last_b = None
    for i in range(index_b):
        this_node = ListNode(list_b[i])
        if begin_b is None:
            begin_b = this_node
            last_b = this_node

        last_b.next = this_node
        last_b = this_node

    if (index_a < len(list_a)) and (index_b < len(list_b)):
        intersection_node = ListNode(list_a[index_a])
        last_a.next = intersection_node
        last_b.next = intersection_node
        last_a = intersection_node

        for i in range(index_a + 1, len(list_a)):
            this_node = ListNode(list_a[i])
            last_a.next = this_node
            last_a = this_node

    return begin_a, begin_b


if __name__ == '__main__':
    listA = [4, 1, 8, 4, 5]
    listB = [5, 0, 1, 8, 4, 5]
    listA = [0, 9, 1, 2, 4]
    listB = [3, 2, 4]
    listA = [2, 6, 4]
    listB = [1, 5]
    headA, headB = create_link(listA, listB, 3, 2)

    # while headA is not None:
    #     print(headA.val, end=' ')
    #     headA = headA.next
    # print()
    # while headB is not None:
    #     print(headB.val, end=' ')
    #     headB = headB.next

    intersection_node = Solution().getIntersectionNode(headA, headB)
    print(intersection_node.val)