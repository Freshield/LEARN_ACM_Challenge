# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_circle_array_r.py
@Time: 2022-09-07 20:44
@Last_update: 2022-09-07 20:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def circle_array(n):
    """
    显示n的平方的螺旋矩阵
    记住左闭右开不变的规则
    1. 生成暂存矩阵以及x，y指针以及当前的值v，注意暂存矩阵的列表生成问题
    2. 结束条件为当前的值v大于n的平方
    3. 左下右上的方式画
    4. 调整x，y进到新的一轮
    """
    # 1. 生成暂存矩阵以及x，y指针以及当前的值v，注意暂存矩阵的列表生成问题
    rst_array = [[1 for _ in range(n)] for _ in range(n)]
    row, col, v, loop_length = 0, 0, 1, n
    # 2. 结束条件为当前的值v大于n的平方
    while v <= n ** 2:
        # 3. 右下左上的方式画
        for _ in range(loop_length - 1):
            rst_array[row][col] = v
            col += 1
            v += 1
        for _ in range(loop_length - 1):
            rst_array[row][col] = v
            row += 1
            v += 1
        for _ in range(loop_length -1):
            rst_array[row][col] = v
            col -= 1
            v += 1
        for _ in range(loop_length - 1):
            rst_array[row][col] = v
            row -= 1
            v += 1
        # 4. 调整x，y进到新的一轮
        loop_length -= 2
        row += 1
        col += 1
        # 对于奇数n最后的中心点
        if loop_length == 1:
            rst_array[row][col] = v
            break

        if loop_length < 0:
            break

    return rst_array


if __name__ == '__main__':
    n = 1
    print(circle_array(n))
