# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a133_get_rain.py
@Time: 2022-10-23 19:46
@Last_update: 2022-10-23 19:46
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def get_rainfall(in_height):
    """
    接雨水，使用栈
    1. 处理特殊情况
    2. 创建需要的栈，sum
    3. 遍历i_height
    4. 遍历，条件为栈不为空
    5. 如果当前的值比栈顶小或者相等，则break
    6. 否则获取栈顶元素top，并弹出，如果栈为空则break
    7. 得到当前的栈顶，并对比计算雨水
    8. 接到的雨水为，长度是当前的位置减去栈顶的位置-1，高度为当前高度和栈顶小的那个高度减去top的高度
    9. 更新sum
    10. 把当前的值放入堆栈
    """
    # 1. 处理特殊情况
    if len(in_height) == 0:
        return 0
    # 2. 创建需要的栈，sum
    stack, sum_v = [], 0
    # 3. 遍历i_height
    for index, height_v in enumerate(in_height):
        # 4. 遍历，条件为栈不为空
        while len(stack) != 0:
            top_i, top_v = stack[-1]
            # 5. 如果当前的值比栈顶小或者相等，则break
            if height_v <= top_v:
                break
            # 6. 否则获取栈顶元素top，并弹出，如果栈为空则break
            stack.pop()
            if len(stack) == 0:
                break
            # 7. 得到当前的栈顶，并对比计算雨水
            new_top_i, new_top_v = stack[-1]
            # 8. 接到的雨水为，长度是当前的位置减去栈顶的位置-1，高度为当前高度和栈顶小的那个高度减去top的高度
            l = index - new_top_i - 1
            h = min(new_top_v, height_v) - top_v
            sum_v += l * h
        # 10. 把当前的值放入堆栈
        stack.append((index, height_v))

    return sum_v


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]
    print(get_rainfall(height))

