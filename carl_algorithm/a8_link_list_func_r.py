# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a8_link_list_func_r.py
@Time: 2022-09-17 20:00
@Last_update: 2022-09-17 20:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a6_link_list_r import ListNode, link_list


class MyLinkList(object):
    """构建链表的对应方法"""
    def __init__(self):
        self.fake_head = ListNode(None)
        self.count = 0

    def get(self, index):
        """
        获取index的节点
        1. 如果不在范围则返回-1
        2. 否则遍历index+1次添加
        """
        # 1. 如果不在范围则返回-1
        if not (0 <= index < self.count):
            return -1

        # 2. 否则遍历index次
        tmp = self.fake_head
        for i in range(index+1):
            tmp = tmp.next

        return tmp

    def addAtIndex(self, index, val):
        """
        在index处增加节点
        1. 如果index小于0则等于0
        2. 如果index大于count则直接返回
        3. 否则遍历index次进行节点添加
        """
        # 1. 如果index小于0则等于0
        index = 0 if index < 0 else index

        # 2. 如果index大于count则直接返回
        if index > self.count:
            return

        # 3. 否则遍历index次进行节点添加
        tmp = self.fake_head
        for i in range(index):
            tmp = tmp.next

        new_node = ListNode(val, tmp.next)
        tmp.next = new_node
        self.count += 1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.count, val)

    def deleteAtIndex(self, index):
        """
        删除index位置的节点
        1. 如果index无效则返回
        2. 遍历index次，进行节点的删除
        """
        # 1. 如果index无效则返回
        if not (0 <= index < self.count):
            return

        # 2. 遍历index次，进行节点的删除
        tmp = self.fake_head
        for i in range(index):
            tmp = tmp.next

        post = tmp.next.next
        tmp.next.next = None
        tmp.next = post
        self.count -= 1


if __name__ == '__main__':
    the_link_list = MyLinkList()
    for i in range(5):
        the_link_list.addAtIndex(0, i)

    print(the_link_list.get(0))
    the_link_list.addAtHead(100)
    the_link_list.addAtTail(200)
    print(the_link_list.get(0))
    the_link_list.deleteAtIndex(1)
    print(the_link_list.get(0))
