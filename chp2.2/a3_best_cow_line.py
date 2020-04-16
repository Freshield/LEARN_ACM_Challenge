#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_best_cow_line.py
@Time: 2020-04-16 10:42
@Last_update: 2020-04-16 10:42
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def solve(word_S, n):
    """
    给定长度N的字符串S，构造一个长度N的字符串T，一开始T是空串，可以反复进行一下两个操作之一
    1. 从S头部pop一个字符给T 2. 从S尾部pop一个字符给T
    目的要构建字典序最大的字符T也就是尽可能把小的字符先给T
    解法：
    使用贪心算法，判断word_S和word_S的反过来的字符串不断比较大小来决定从前边还是后边选取字符
    整体流程：
    1. 构建r_word_S
    2. 遍历所有位置
    3. 比较两个字符串大小决定从什么位置选取
    4. 更新word_S, r_word_S和T
    """
    T = ''
    # 1. 构建r_word_S
    r_word_S = [word_S[i] for i in range(len(word_S)-1, -1, -1)]
    word_S = [i for i in word_S]

    # 2. 遍历所有位置
    fetch_left = True
    for _ in range(n):

        print(T)
        print(word_S)
        print(r_word_S)

        # 3. 比较两个字符串大小决定从什么位置选取
        for i in range(len(word_S)):
            if word_S[i] < r_word_S[i]:
                fetch_left = True
                break
            elif r_word_S[i] < word_S[i]:
                fetch_left = False
                break
            else:
                continue

        # 4. 更新word_S, r_word_S和T
        if fetch_left:
            T += word_S[0]
            word_S.pop(0)
            r_word_S.pop(-1)
        else:
            T += word_S[-1]
            word_S.pop(-1)
            r_word_S.pop(0)

    return T


if __name__ == '__main__':
    S = 'acdbcb'
    print(solve(S, len(S)))