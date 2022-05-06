# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a8_link_list_func.py
@Time: 2022-04-12 16:48
@Last_update: 2022-04-12 16:48
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


class MyLinkedList:

    def __init__(self):
        self.fake_node = ListNode(None)
        self.tail = self.fake_node
        self.count = 0

    def get(self, index: int) -> int:
        """
        获取index的节点，如果索引无效返回-1
        """
        if (index >= self.count) or (index < 0):
            return -1

        this_node = self.fake_node.next
        for _ in range(index):
            this_node = this_node.next

        return this_node.val

    def addAtHead(self, val: int) -> None:
        """在链表的第一个元素之前添加一个值为 val 的节点"""
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """将值为 val 的节点追加到链表的最后一个元素"""
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """在链表中的第 index 个节点之前添加值为 val  的节点"""
        if index < 0:
            index = 0
        elif index > self.count:
            return

        this_node = self.fake_node
        for i in range(index):
            this_node = this_node.next

        new_node = ListNode(val, this_node.next)
        this_node.next = new_node
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        """如果索引 index 有效，则删除链表中的第 index 个节点"""
        if not (0 <= index < self.count):
            return

        this_node = self.fake_node
        for i in range(index):
            this_node = this_node.next

        this_node.next = this_node.next.next
        self.count -= 1

    def __str__(self):
        return f'{self.fake_node.next}'


if __name__ == '__main__':
    node_list = MyLinkedList()
    print(node_list)

    list_value = [1, 2, 6]
    # list_value = list_value[::-1]
    last_node = None
    for value in list_value:
        node_list.addAtTail(value)

    print(node_list)
    print(node_list.get(3))

    node_list.addAtIndex(0, 0)
    print(node_list)
    node_list.addAtIndex(1, 8)
    print(node_list)

    node_list.deleteAtIndex(1)
    print(node_list)
    node_list.deleteAtIndex(0)
    print(node_list)
    node_list.deleteAtIndex(2)
    print(node_list)
    node_list.deleteAtIndex(0)
    print(node_list)
    node_list.deleteAtIndex(0)
    print(node_list)
