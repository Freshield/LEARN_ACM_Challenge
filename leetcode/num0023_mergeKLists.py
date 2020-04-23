# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0023_mergeKLists.py
@Time: 2020-04-22 22:52
@Last_update: 2020-04-22 22:52
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import heapq
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%s %s' % (self.val, self.next)


def lt(self, other):
    return self.val < other.val


class Solution:
    """
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    解法：使用heapq来进行比较操作，每次放入和拿出最小的和最小的下一个直到queue为空
    """
    def mergeKLists(self, lists):
        """
        整体流程：
        1. 初始化堆以及相关变量
        2. 设定初始化条件
        3. 终止条件为堆为空
        4. 最终返回起始节点
        """
        if len(lists) == 0:
            return []
        # 1. 初始化堆以及相关变量
        heap = []
        ListNode.__lt__ = lt
        # 2. 设定初始化条件
        for node in lists:
            if node is not None:
                heapq.heappush(heap, node)

        start_node = ListNode(0)
        link_node = start_node

        # 3. 终止条件为堆为空
        while len(heap) != 0:
            min_node = heapq.heappop(heap)
            link_node.next = min_node
            link_node = min_node
            if min_node.next is not None:
                heapq.heappush(heap, min_node.next)

        # 4. 最终返回起始节点
        return start_node.next


if __name__ == '__main__':
    link0 = [1, 4, 5]
    link1 = [1, 3, 4]
    link2 = [2, 6]
    node0 = ListNode(link0[0])
    tmp = node0
    for i in range(1, len(link0)):
        tmp.next = ListNode(link0[i])
        tmp = tmp.next
    node1 = ListNode(link1[0])
    tmp = node1
    for i in range(1, len(link1)):
        tmp.next = ListNode(link1[i])
        tmp = tmp.next
    node2 = ListNode(link2[0])
    tmp = node2
    for i in range(1, len(link2)):
        tmp.next = ListNode(link2[i])
        tmp = tmp.next
    node_list = [node0, node1, node2]
    for node in node_list:
        print(node)
    # node_list = [ListNode(1), ListNode(0)]
    begin_node = Solution().mergeKLists(node_list)
    print(begin_node)

