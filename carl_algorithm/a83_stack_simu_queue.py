# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a83_stack_simu_queue.py
@Time: 2022-10-10 11:12
@Last_update: 2022-10-10 11:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, value):
        self.in_stack.append(value)

    def pop(self):
        """
        模拟queue的pop操作，需要通过out stack来调整顺序
        1. 如果out stack不为空则直接从最后弹出
        2. 否则，把in stack的所有数据放到out stack中，再从最后弹出
        """
        # 1. 如果out stack不为空则直接从最后弹出
        if len(self.out_stack) != 0:
            return self.out_stack.pop(-1)
        # 2. 否则，把in stack的所有数据放到out stack中，再从最后弹出
        for i in range(len(self.in_stack)):
            self.out_stack.append(self.in_stack.pop(-1))

        return self.out_stack.pop(-1)

    def peek(self):
        value = self.pop()
        self.out_stack.append(value)

        return value

    def is_empty(self):
        return (len(self.in_stack) + len(self.out_stack)) == 0


if __name__ == '__main__':
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.peek())
    print(my_queue.pop())
    print(my_queue.is_empty())
