# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0155_MinStack.py
@Time: 2020-05-15 10:04
@Last_update: 2020-05-15 10:04
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class MinStack:
    """
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。
    解法：
    添加维护当前最小元素的列表
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = [float('inf')]

    def push(self, x):
        """
        压栈
        整体流程：
        1. 放入数值
        2. 和min_val顶值比较，如果小则放入
        """
        # 1. 放入数值
        self.stack.append(x)

        # 2. 和min_val顶值比较，如果小则放入
        if x <= self.min_val[-1]:
            self.min_val.append(x)

    def pop(self):
        """
        弹出
        整体流程：
        1. 栈弹出
        2. 如果当前值等于min_val的顶值则也弹出
        """
        # 1. 栈弹出
        val = self.stack.pop(-1)
        # 2. 如果当前值等于min_val的顶值则也弹出
        if val == self.min_val[-1]:
            self.min_val.pop(-1)

    def top(self):
        """得到栈顶值"""
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self):
        """得到当前最小值"""
        return self.min_val[-1]


if __name__ == '__main__':
    MinStack
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())