# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0092_reverseBetween.py
@Time: 2020-06-22 11:17
@Last_update: 2020-06-22 11:17
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
        return f'val:{self.val}, next:{self.next}'


class Solution:
    """
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
    说明:
    1 ≤ m ≤ n ≤ 链表长度。
    解法：
    使用暂存节点进行连接
    """
    def __init__(self):
        self.last = None
        self.next = None

    def reverseBetween(self, head, m, n):
        """
        整体流程：
        1. 生成索引的中间变量，处理特殊情况
        2. 遍历链表，更新中间节点
        3. 当达到m时
        4. 生成outer_head_node, inner_tail_node
        5. 使用tmp_node进行节点反转
        6. 当到达n时
        7. 生成outer_tail_node, inner_head_node
        8. 把inner和outer进行连接
        """
        if m == n:
            return head

        # 1. 生成索引的中间变量，处理特殊情况
        index = 1
        tmp_head = ListNode(None)
        tmp_head.next = head
        tmp_last = tmp_head
        tmp_node = head
        inner_next = None
        inner_last = None


        # 2. 遍历链表，更新中间节点
        while True:

            # 3. 当达到m时
            if index == m:
                # 4. 生成outer_head_node, inner_tail_node
                outer_head_node = tmp_last
                inner_tail_node = tmp_node

                inner_next = tmp_node.next
                tmp_node.next = inner_last
                inner_last = tmp_node
                tmp_node = inner_next
            elif m < index < n:
                # 5. 使用tmp_node进行节点反转
                inner_next = tmp_node.next
                tmp_node.next = inner_last
                inner_last = tmp_node
                tmp_node = inner_next
            # 6. 当到达n时
            elif index == n:
                # 7. 生成outer_tail_node, inner_head_node
                outer_tail_node = tmp_node.next
                inner_head_node = tmp_node

                inner_next = tmp_node.next
                tmp_node.next = inner_last
                inner_last = tmp_node
                tmp_node = inner_next
                # 8. 把inner和outer进行连接
                outer_head_node.next = inner_head_node
                inner_tail_node.next = outer_tail_node
            else:

                tmp_node = tmp_node.next
                tmp_last = tmp_last.next

            index += 1
            if tmp_node is None:
                break

        return tmp_head.next


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    head = ListNode(None)
    last_node = head
    for num in nums:
        this_node = ListNode(num)
        last_node.next = this_node
        last_node = this_node
    head = head.next

    m, n = 1, 5
    print(Solution().reverseBetween(head, m, n))