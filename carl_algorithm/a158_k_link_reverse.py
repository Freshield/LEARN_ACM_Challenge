# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a158_k_link_reverse.py
@Time: 2022-11-05 20:10
@Last_update: 2022-11-05 20:10
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


def reverse_link(head, end):
    """
    从head到end node进行翻转链表
    1. pre节点，next节点，node节点
    2. 遍历，条件为当前节点不为end的下一个
    3. 更新next节点，更新node的next，更新pre和node
    """
    # 1. pre节点，next节点，node节点
    pre, node, end_next = None, head, end.next
    # 2. 遍历，条件为当前节点不为end的下一个
    while node is not end_next:
        # 3. 更新next节点，更新node的next，更新pre和node
        next = node.next
        node.next = pre
        pre = node
        node = next

    return end, head


def k_link_reverse(head, k):
    """
    k个一组翻转链表
    1. 创建dummy head，pre，next，node，end
    2. 遍历，条件为node不为空
    3. 遍历k-1次，如果node为空则跳出
    4. 更新next，end
    5. 进行翻转
    6. pre连接，next连接
    7. 更新pre，node
    """
    # 1. 创建dummy head，pre，next，node，end
    dummy_head = ListNode(None, next=head)
    pre_node, next_node, node = dummy_head, dummy_head, head
    # 2. 遍历，条件为node不为空
    while node is not None:
        # 3. 遍历k-1次，如果node为空则跳出
        for i in range(k - 1):
            node = node.next
            if node is None:
                break
        else:
            # 4. 更新next，end
            next_node = node.next
            # 5. 进行翻转
            start_node, end_node = reverse_link(pre_node.next, node)
            # 6. pre连接，next连接
            pre_node.next = start_node
            end_node.next = next_node
            # 7. 更新pre，node
            pre_node = end_node
            node = next_node

    return dummy_head.next


if __name__ == '__main__':
    head = link_list([i + 1 for i in range(4)])
    k = 2
    print(k_link_reverse(head, k))
