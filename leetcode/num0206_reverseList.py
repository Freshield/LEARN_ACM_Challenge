# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0206_reverseList.py
@Time: 2020-04-18 15:48
@Last_update: 2020-04-18 15:48
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

list_last_node = None


class ListNode(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return '%s %s' % (self.value, self.next)

def reverseList(start_node):
    """
    反转一个单链表。
    解法：
    使用递归调用，直到最后一个节点
    整体流程：
    1. 存储next节点
    2. 更改当前节点的next为list last node
    3. list last node指向当前节点
    4. 递归遍历next节点
    5. 返回递归结果
    6. 结束条件：如果next为None，则返回当前节点
    """
    global list_last_node
    # 1. 存储next节点
    next_node = start_node.next
    # 2. 更改当前节点的next为list last node
    start_node.next = list_last_node
    # 3. list last node指向当前节点
    list_last_node = start_node
    # 6. 结束条件：如果next为None，则返回当前节点
    if next_node is None:
        return start_node
    # 4. 递归遍历next节点
    rst_node = reverseList(next_node)
    # 5. 返回递归结果
    return rst_node


if __name__ == '__main__':
    last_node = None
    for i in range(10):
        this_node = ListNode(i, last_node)
        last_node = this_node

    print(last_node)

    last_node = reverseList(last_node)

    print(last_node)