# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a188_combine.py
@Time: 2023-01-30 13:22
@Last_update: 2023-01-30 13:22
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def combine(n, k):
    """
    组合问题，使用回溯算法
    """
    rst_list, path_list = [], []

    def backtracking(n, k, start_index):
        """
        回溯部分
        1. 参数返回，遍历的长度n，起始start_index，最大长度k
        2. 停止条件，当path长度等于k的时候，则保存当前的path
        3. 回溯逻辑，遍历长度n
        4. 判断当前的长度是否够，如果不够则直接跳出
        5. path加入当前的数字，并递归start_index到n
        6. 回溯部分，把path进行弹出
        """
        # 2. 停止条件，当path长度等于k的时候，则保存当前的path
        if len(path_list) == k:
            rst_list.append(path_list[:])
            return
        # 3. 回溯逻辑，遍历长度n
        for i in range(start_index, n):
            # 4. 判断当前的长度是否够，如果不够则直接跳出
            if (n - i) < (k - len(path_list)):
                break
            # 5. path加入当前的数字，并递归start_index到n
            path_list.append(i+1)
            backtracking(n, k, i + 1)
            path_list.pop()

        return

    backtracking(n, k, 0)

    return rst_list


if __name__ == '__main__':
    n, k = 4, 2
    print(combine(n, k))
