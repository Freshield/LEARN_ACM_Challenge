# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0141_hasCycle.py
@Time: 2020-04-19 15:29
@Last_update: 2020-04-19 15:29
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


class Solution:
    def hasCycle(self, head: ListNode):
        """
        快慢指针法
        解法：慢指针每次走一步，快指针走两步，如果快指针直接到None则无环，如果快指针赶上了慢指针则有环
        整体流程：
        1. 定义两个指针
        2. 遍历node
        3. 结束条件：如果fast.next is None or fast.next.next is None则返回False
        4. 结束条件：如果fast.next == slow or fast.next.next is slow则返回True
        5. 更新slow，fast
        """
        # 1. 定义两个指针
        if head is None:
            return False
        slow = head
        fast = head
        # 2. 遍历node
        while True:
            # 3. 结束条件：如果fast.next is None or fast.next.next is None则返回False
            if (fast.next is None) or (fast.next.next is None):
                return False

            # 4. 结束条件：如果fast.next == slow or fast.next.next is slow则返回True
            if (fast.next is slow) or (fast.next.next is slow):
                return True

            # 5. 更新slow，fast
            slow = slow.next
            fast = fast.next.next


    def hasCycle_hash(self, head: ListNode):
        """
        哈希表解法
        整体流程：
        1. 遍历head
        2. 结束条件：如果head是None则返回False
        3. 结束条件：如果head存在于字典中则返回True
        4. 存到字典中，遍历下一个
        """
        node_dict = dict()
        # 1. 遍历head
        while True:
            # 2. 结束条件：如果head是None则返回False
            if head is None:
                return False

            # 3. 结束条件：如果head存在于字典中则返回True
            if head in node_dict.keys():
                return True

            # 4. 存到字典中，遍历下一个
            node_dict[head] = None
            head = head.next



if __name__ == '__main__':
    head_list = [3, 2, 0, -4]
    pos = 1
    # head = [1, 2]
    # pos = 0
    # head = [1]
    # pos = -1
    list_nodes = []
    begin_node = ListNode(head_list[0])
    link_node = begin_node
    list_nodes.append(link_node)
    for val in head_list[1:]:
        tmp = ListNode(val)
        link_node.next = tmp
        link_node = tmp
        list_nodes.append(link_node)
    if pos != -1:
        link_node.next = list_nodes[pos]

    for node in list_nodes:
        print('%s %s' % (node.val, node.next.val if node.next is not None else None))

    print(Solution().hasCycle(begin_node))