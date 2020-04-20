#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0146_LRUCache.py
@Time: 2020-04-20 10:25
@Last_update: 2020-04-20 10:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class ListNode(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return '%s %s' % (self.key, self.next)


class LRUCache:
    """
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
    进阶:
    你是否可以在 O(1) 时间复杂度内完成这两种操作？
    解法：
    记录使用字典，顺序用双链表来维持，创建head和tail节点，这样保证没有边界问题
    整体流程：
    1. put时：
        i. 如果没到capacity，dict加，list加
        ii. 如果到了capacity，head 的node去除，在后边加入新的node
    2. get时：
        i. 如果没有key，返回-1
        ii. 如果有key，相应的node移动到tail，返回相应的值
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mem_dict = dict()
        self.head = ListNode('head', 'head')
        self.tail = ListNode('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key):
        """
        把key的node移动到末尾
        """
        node = self.mem_dict[key]
        # 移出，两根线
        node.prev.next = node.next
        node.next.prev = node.prev

        # 移到末尾，四根线
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        # i. 如果没有key，返回-1
        if key not in self.mem_dict.keys():
            return -1
        # ii. 如果有key，相应的node移动到tail，返回相应的值
        else:
            self.move_to_tail(key)
            return self.mem_dict[key].value

    def put(self, key, value):
        if key in self.mem_dict.keys():
            self.move_to_tail(key)
            self.mem_dict[key].value = value
        else:
            # i. 如果没到capacity，dict加，list加
            if len(self.mem_dict) == self.capacity:
                # 去除head的下一个，四根线
                next_node = self.head.next
                next_node.next.prev = self.head
                self.head.next = next_node.next
                next_node.prev = None
                next_node.next = None
                del self.mem_dict[next_node.key]

            # 添加到结尾，四根线
            node = ListNode(key, value, self.tail.prev, self.tail)
            self.tail.prev.next = node
            self.tail.prev = node
            self.mem_dict[key] = node






if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache.head)
    print(cache.get(2))
    cache.put(2, 6)
    print(cache.head)
    print(cache.get(1))
    print(cache.head)
    cache.put(1, 5)
    print(cache.head)
    cache.put(1, 2)
    print(cache.head)
    print(cache.get(1))
    print(cache.head)
    print(cache.get(2))
    print(cache.head)