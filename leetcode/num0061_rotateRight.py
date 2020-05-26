# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0061_rotateRight.py
@Time: 2020-05-26 10:21
@Last_update: 2020-05-26 10:21
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
        return f'{self.val} {self.next}'


class Solution:
    """
    给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
    解法：
    遍历链表得到链表的长度，计算从第几个节点转换，然后找到这个节点进行变换
    """
    def rotateRight(self, head, k):
        """
        整体流程：
        1. 得到链表的长度
        2. 计算转换的节点
        3. 找到节点进行变换
        """
        if head is None:
            return head

        # 1. 得到链表的长度
        length = 1
        tmp = head
        while tmp.next is not None:
            length += 1
            tmp = tmp.next
        tmp.next = head

        if k % length == 0:
            tmp.next = None
            return head

        # 2. 计算转换的节点
        change_index = length + 1 - (k % length)

        # 3. 找到节点进行变换
        length = 0
        while True:
            length += 1
            tmp = tmp.next
            if length == change_index - 1:
                head = tmp.next
                tmp.next = None
                break

        return head



def create_link(nums):
    begin_node = None
    last_node = None
    for num in nums:
        this_node = ListNode(num)
        if begin_node is None:
            begin_node = this_node
            last_node = this_node
            continue
            
        last_node.next = this_node
        last_node = this_node
        
    return begin_node


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 2
    nums = [0,1,2]
    k = 3
    head = create_link(nums)
    print(head)
    print(Solution().rotateRight(head, k))