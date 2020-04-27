#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a25_del_num.py
@Time: 2020-04-26 14:51
@Last_update: 2020-04-26 14:51
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

class LinkNode(object):
    def __init__(self, val, begin_index):
        self.val = val
        self.begin_index = begin_index
        self.pre = None
        self.next = None

    def __str__(self):
        return str(self.begin_index)


class Solution(object):
    """
    有一个数组a[N]顺序存放0~N-1，要求每隔两个数删掉一个数，
    到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。
    以8个数(N=7)为例:｛0，1，2，3，4，5，6，7｝，0->1->2(删除)->3->4->5(删除)->6->7->0(删除),
    如此循环直到最后一个数被删除。
    解法：
    递归复制列表
    """
    def del_num(self, input_list):
        """
        整体流程：
        1. 生成nodes
        2. 结束条件：this_node的next指向自己
        3. 递归调用
        """
        this_node = None
        last_node = None
        # 1. 生成nodes
        for i in range(len(input_list)):
            tmp_node = LinkNode(input_list[i], i)
            if this_node is None:
                this_node = tmp_node
                last_node = tmp_node
                continue

            last_node.next = tmp_node
            tmp_node.pre = last_node
            last_node = tmp_node

        last_node.next = this_node
        this_node.pre = last_node

        index = 1
        while True:
            if this_node.next.next == this_node:
                if index == 0:
                    return this_node
                else:
                    return this_node.next

            this_node = this_node.next
            index += 1

            if index % 3 == 0:
                this_node.pre.next = this_node.next
                this_node.next.pre = this_node.pre
                index = 0


def input_to_str():
    while True:
        try:
            n = min(int(input()), 999)
            input_list = list(range(n))
            last_node = Solution().del_num(input_list)
            print(str(last_node))
        except Exception as e:
            break


if __name__ == '__main__':
    input_list = list(range(8))
    print(Solution().del_num(input_list))