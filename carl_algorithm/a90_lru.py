# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a90_lru.py
@Time: 2022-10-11 21:08
@Last_update: 2022-10-11 21:08
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class DeLinkNode(object):
    def __init__(self, prev=None, next=None, key=None, value=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value


class LRUCache:
    """使用哈希表和双向链表"""
    def __init__(self, capacity: int):
        # 创建哈希表和双向链表
        self.cache = dict()
        self.head = DeLinkNode()
        self.tail = DeLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete_tail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node

    def get(self, key: int) -> int:
        """
        获取key
        1. 如果没有key则返回-1
        2. 如果有key则把相应节点放到head，并返回值
        """
        # 1. 如果没有key则返回-1
        if key not in self.cache:
            return -1
        # 2. 如果有key则把相应节点放到head，并返回值
        node = self.cache[key]
        self.move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        LRU放入值
        1. 如果已经存在则直接把节点放到head
        2. 否则新建节点，并放入字典
        3. 把节点放到head
        4. 如果超过capacity则删除尾部节点
        """
        # 1. 如果已经存在则直接把节点放到head
        if key in self.cache:
            self.move_to_head(self.cache[key])
            self.cache[key].value = value
            return None
        # 2. 否则新建节点，并放入字典
        node = DeLinkNode(key=key, value=value)
        self.cache[key] = node
        # 3. 把节点放到head
        self.add_to_head(node)
        # 4. 如果超过capacity则删除尾部节点
        if len(self.cache) > self.capacity:
            tail_node = self.delete_tail()
            del self.cache[tail_node.key]


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    print(lru.cache)
    lru.put(2, 2)
    print(lru.cache)
    lru.get(1)
    print(lru.cache)
    lru.put(3, 3)
    print(lru.cache)
