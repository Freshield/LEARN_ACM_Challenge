# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0148_sortList.py
@Time: 2020-05-13 15:02
@Last_update: 2020-05-13 15:02
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

    def __str__(self):
        return '%s %s' % (self.val, self.next)


class Solution:
    """
    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
    使用快慢指针和归并排序
    """
    def sortList(self, head):
        """
        整体流程：
        1. 结束条件：如果head的下一个是None则返回
        2. 设定快慢指针
        3. 遍历，结束条件为快指针的下一个是None或者下下个为None
        4. 慢指针走一步，快指针走两步
        5. 从slow开始断开
        6. 得到左右部分递归
        7. 遍历左右部分
        8. 进行比较
        9. 结束条件为其中一个为空
        10. 把不空的那个连接上
        11. 返回根节点
        """
        # 1. 结束条件：如果head的下一个是None则返回
        if (head is None) or (head.next is None):
            return head
        # 2. 设定快慢指针
        slow = head
        fast = head
        # 3. 遍历，结束条件为快指针的下一个是None或者下下个为None
        while (fast.next is not None) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        # 5. 从slow开始断开
        right = slow.next
        slow.next = None
        # 6. 得到左右部分递归
        left = self.sortList(head)
        right = self.sortList(right)
        # 7. 遍历左右部分
        # 9. 结束条件为其中一个为空
        begin = ListNode(None)
        last = begin
        while (left is not None) and (right is not None):
            # 8. 进行比较
            if left.val < right.val:
                last.next = left
                last = left
                left = left.next
            else:
                last.next = right
                last = right
                right = right.next
        # 10. 把不空的那个连接上
        last.next = left if left is not None else right

        # 11. 返回根节点
        return begin.next


def create_link(val_list):
    head = None
    last = None
    for val in val_list:
        this_node = ListNode(val)
        if head is None:
            head = this_node
            last = this_node
            continue

        last.next = this_node
        last = this_node

    return head


if __name__ == '__main__':
    val_list = [-1, 5, 3, 4, 0]
    head = create_link(val_list)
    print(head)
    head = Solution().sortList(head)
    print(head)