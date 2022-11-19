# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a84_queue_simu_stack.py
@Time: 2022-10-10 11:25
@Last_update: 2022-10-10 11:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class MyStack(object):

    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        """
        用queue模拟stack的pop动作，循环推出直到最后一个
        """
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

        return self.queue.pop(0)

    def top(self):
        value = self.pop()
        self.queue.append(value)

        return value

    def empty(self):
        return len(self.queue) == 0


if __name__ == '__main__':
    my_queue = MyStack()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.pop())
