# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0002_addTwoNumbers.py
@Time: 2020-04-18 17:22
@Last_update: 2020-04-18 17:22
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
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return '%s %s' % (self.val, self.next)


def addTwoNumbers(l1, l2):
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
    并且它们的每个节点只能存储一位数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0开头。
    解法：
    遍历l1, l2，需要注意的是两点:
        1. 进位问题
        2. 当l1,l2不等时的补零问题
    整体流程：
    1. 准备需要的中间变量
    2. 结束条件：l1 == l2 == None且flag==0
    3. 获得l1 l2的值进行计算，如果是None则用0代替
    4. 更新l1 l2为next值，如果是None则用None代替
    """
    # 1. 准备需要的中间变量
    flag = 0
    rst_node = None
    last_node = None
    while True:
        # 2. 结束条件：l1 == l2 == None
        if (l1 is None) and (l2 is None) and (flag == 0):
            return rst_node

        # 3. 获得l1 l2的值进行计算，如果是None则用0代替
        l1_val = l1.val if l1 is not None else 0
        l2_val = l2.val if l2 is not None else 0
        sum_val = l1_val + l2_val + flag
        l3_val = sum_val % 10
        flag = sum_val // 10
        this_node = ListNode(l3_val)
        if last_node is not None:
            last_node.next = this_node

        last_node = this_node

        if rst_node is None:
            rst_node = this_node

        # 4. 更新l1 l2为next值，如果是None则用None代替
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None



if __name__ == '__main__':
    list1 = [3, 4, 2]
    list2 = [4, 6, 5]
    # list1 = [1]
    # list2 = [9, 9]
    begin_node = None
    for val in list1:
        l1 = ListNode(val)
        l1.next = begin_node
        begin_node = l1
    begin_node = None
    for val in list2:
        l2 = ListNode(val)
        l2.next = begin_node
        begin_node = l2
    print(l1)
    print(l2)
    l3 = addTwoNumbers(l1, l2)
    print(l3)

