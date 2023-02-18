# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a189_combine_review.py
@Time: 2023-02-20 13:33
@Last_update: 2023-02-20 13:33
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
    组合问题，给定n，k染回1-n中所有可能的k个数的组合
    使用回溯算法
    """
    n_list = list(range(1, n + 1))
    path, result = [], []

    def _back_tracking(index):
        """
        回溯部分
        1. 参数返回，index索引
        2. 停止条件，当path的长度等于k的时候则停止，保存结果，并返回
        3. 回溯逻辑，遍历，从index开始到n_list的结尾
        4. 把index指向的元素放到path中，并递归
        5. 递归结束后，弹出对应的元素
        """
        # 2. 停止条件，当path的长度等于k的时候则停止，保存结果，并返回
        if len(path) == k:
            result.append(path[:])
            return
        # 3. 回溯逻辑，遍历，从index开始到n_list的结尾
        for i in range(index, len(n_list)):
            # 4. 把index指向的元素放到path中，并递归
            elem = n_list[i]
            path.append(elem)
            _back_tracking(i + 1)
            # 5. 递归结束后，弹出对应的元素
            path.pop()

        return

    _back_tracking(0)

    return result


if __name__ == '__main__':
    n, k = 4, 2
    print(combine(n, k))
