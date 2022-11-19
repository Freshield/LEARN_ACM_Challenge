# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a162_daily_temperatures.py
@Time: 2022-11-13 18:02
@Last_update: 2022-11-13 18:02
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def daily_temperatures(temperatures):
    """
    计算每天距离下一个更高温度在几天后，使用单调栈
    1. 创建res list和temp stack
    2. 遍历temperatures列表
    3. 情况一，如果当前的温度小于栈顶，则推入栈
    4. 情况二，如果当前的温度等于栈顶，则推入栈
    5. 情况三，如果当前的温度大于栈顶
    6. 遍历，条件为单调栈长度大于0，且当前的温度大于栈顶
    7. 弹出栈顶，计算天数为当前的位置减去栈顶的位置，放入res list
    8. 放当前的位置入栈
    """
    # 1. 创建res list和temp stack
    res_list, temp_stack = [0] * len(temperatures), [0]
    # 2. 遍历temperatures列表
    for i in range(1, len(temperatures)):
        temp = temperatures[i]
        # 3. 情况一，如果当前的温度小于栈顶，则推入栈
        if temp < temperatures[temp_stack[-1]]:
            temp_stack.append(i)
            continue
        # 4. 情况二，如果当前的温度等于栈顶，则推入栈
        elif temp == temperatures[temp_stack[-1]]:
            temp_stack.append(i)
            continue
        # 5. 情况三，如果当前的温度大于栈顶
        # 6. 遍历，条件为单调栈长度大于0，且当前的温度大于栈顶
        while (len(temp_stack) > 0) and (temp > temperatures[temp_stack[-1]]):
            # 7. 弹出栈顶，计算天数为当前的位置减去栈顶的位置，放入res list
            stack_top = temp_stack.pop()
            res = i - stack_top
            res_list[stack_top] = res
        # 8. 放当前的位置入栈
        temp_stack.append(i)

    return res_list


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures(temperatures))

