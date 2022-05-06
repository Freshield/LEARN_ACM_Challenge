# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a30_move_window_max_value.py
@Time: 2022-04-18 16:31
@Last_update: 2022-04-18 16:31
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def move_window_max_value(value_list, k):
    """
    得到滑动窗口最大值
    构建一个单调队列来达成最大值的操作，重点在于最大值左侧的值对最大值没有意义
    """
    class _MyQueue(object):
        _queue = []

        def pop(self, value):
            """
            pop操作，看要pop的数值是否为最左侧的数值，如果是则pop
            """
            if (len(self._queue) != 0) and (self.front() == value):
                self._queue.pop(0)

        def push(self, value):
            """
            压入单调队列，要保证队列中的值都比value要大或者相等，否则弹出，再入队
            """
            while (len(self._queue) != 0) and (self._queue[-1] < value):
                self._queue.pop()

            self._queue.append(value)

        def front(self):
            """获取当前的最大值"""
            return self._queue[0] if len(self._queue) != 0 else None

    # 创建新的queue
    max_list = []
    queue = _MyQueue()
    for i in range(k):
        queue.push(value_list[i])
    max_list.append(queue.front())

    for i in range(k, len(value_list)):
        queue.pop(value_list[i - k])
        queue.push(value_list[i])
        max_list.append(queue.front())

    return max_list


if __name__ == '__main__':
    value_list = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(move_window_max_value(value_list, k))
