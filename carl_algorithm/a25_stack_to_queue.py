# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a25_stack_to_queue.py
@Time: 2022-04-17 17:21
@Last_update: 2022-04-17 17:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class MyQueue:
    """使用栈模拟队列"""
    def __init__(self):
        """
        新建两个堆栈
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        入队则直接放入入栈
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        出队
        要通过出栈来调整顺序
        1. 把当前的入栈中的全都出栈到出栈
        2. 然后再把出栈的出栈
        """
        # 1. 把当前的入栈中的全都出栈到出栈
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())

        # 2. 然后再把出栈的出栈
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        查看顶点值
        先出栈再放回来出栈
        """
        the_value = self.pop()
        self.out_stack.append(the_value)

        return the_value

    def empty(self) -> bool:
        """
        是否为空
        看入栈出栈是否都为空
        """
        return (len(self.in_stack) == 0) and (len(self.out_stack) == 0)


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.pop())
    queue.push(3)
    queue.push(4)
    print(queue.peek())
    print(queue.empty())
    print(queue.pop())


