# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a88_slide_window_max_value.py
@Time: 2022-10-11 17:20
@Last_update: 2022-10-11 17:20
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from collections import deque


class SingleQueue(object):
    def __init__(self):
        """初始化创建队列，这里需要用deque否则会超时"""
        self.queue = deque()

    def pop(self, value):
        """
        弹出相应的value，这是是只有相等的时候才弹出
        """
        if (len(self.queue) != 0) and (value == self.front()):
            return self.queue.popleft()

    def push(self, value):
        """
        往单调队列中放入数据
        1. 遍历队列，条件为队列不为空且value比当前的队尾数值大
        2. 把队尾的数值弹出
        3. 直接append value
        """
        # 1. 遍历队列，条件为队列不为空且value比当前的队尾数值大
        while (len(self.queue) != 0) and (value > self.queue[-1]):
            # 2. 把队尾的数值弹出
            self.queue.pop()
        # 3. 直接append value
        self.queue.append(value)

    def front(self):
        """获取最大值"""
        if len(self.queue) != 0:
            return self.queue[0]


def slide_window_max_value(nums, k):
    """
    获取滑动窗口的最大值，使用单调队列
    1. 创建单调队列，返回列表
    2. 遍历插入最开始的滑动窗口的值
    3. 遍历剩下的数值
    4. 弹出左指针的值
    5. 插入右指针的值
    6. 放入结果
    """
    # 1. 创建单调队列，返回列表
    single_queue = SingleQueue()
    result_list = []
    # 2. 遍历插入最开始的滑动窗口的值
    for i in range(k):
        single_queue.push(nums[i])
    result_list.append(single_queue.front())
    # 3. 遍历剩下的数值
    for i in range(k, len(nums)):
        # 4. 弹出左指针的值
        single_queue.pop(nums[i - k])
        # 5. 插入右指针的值
        single_queue.push(nums[i])
        # 6. 放入结果
        result_list.append(single_queue.front())

    return result_list


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    nums = [1, -1]
    k = 1
    nums = [-7, -8, 7, 5, 7, 1, 6, 0]
    k = 4
    print(slide_window_max_value(nums, k))
