# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a26_queue_to_stack.py
@Time: 2022-04-17 18:12
@Last_update: 2022-04-17 18:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

class MyStack:

    def __init__(self):
        """使用一个queue来达到stack"""
        self.queue = []

    def push(self, x: int) -> None:
        """
        push则直接进行入队
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        出栈操作
        循环操作
        1. 遍历queue的值长度减一，同时入队
        2. 弹出顶部的数值
        """
        # 1. 遍历queue的值长度减一，同时入队
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

        # 2. 弹出顶部的数值
        return self.queue.pop(0)

    def top(self) -> int:
        """
        得到顶部数据
        把pop的再放入
        """
        value = self.pop()
        self.queue.append(value)

        return value

    def empty(self) -> bool:
        """
        看当前是否为空
        """
        return len(self.queue) == 0


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    stack.push(3)
    print(stack.top())
    print(stack.empty())
    print(stack.pop())
