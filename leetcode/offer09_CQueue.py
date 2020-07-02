# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: offer09_CQueue.py
@Time: 2020-07-02 11:05
@Last_update: 2020-07-02 11:05
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class CQueue:
    """
    用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
    分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
    解法：
    两个栈，栈是先入后出，队的先入先出
    在deleteHead的时候，如果head栈有元素则直接弹出，如果没有元素则把tail栈的元素都放到head栈并弹出一个
    转后head栈仍为空则返回-1
    """
    def __init__(self):
        self.head_stack = []
        self.tail_stack = []

    def appendTail(self, value):
        self.tail_stack.append(value)

    def deleteHead(self):
        """
        整体流程：
        1. 如果head_stack为空则把tail栈的元素都放入
        2. 如果head_stack仍为空则返回-1
        3. 否则返回顶元素
        """
        # 1. 如果head_stack为空则把tail栈的元素都放入
        if len(self.head_stack) == 0:
            while len(self.tail_stack) != 0:
                self.head_stack.append(self.tail_stack.pop(-1))

        # 2. 如果head_stack仍为空则返回-1
        if len(self.head_stack) == 0:
            return -1
        else:
            return self.head_stack.pop(-1)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

if __name__ == '__main__':
    obj = CQueue()
    # obj.appendTail(3)
    # print(obj.deleteHead())
    # print(obj.deleteHead())

    print(obj.deleteHead())
    print(obj.appendTail(5))
    print(obj.appendTail(2))
    print(obj.deleteHead())
    print(obj.deleteHead())