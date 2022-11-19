# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a127_dispatch_cookie.py
@Time: 2022-10-19 18:15
@Last_update: 2022-10-19 18:15
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def dispatch_cookie(cookies, children):
    """
    分发饼干，策略为从小到大，让s里小的尽量先满足小胃口的g，贪心算法
    1. 生成cookie_p，child_p指针分别指向s和g
    2. 遍历，条件为cookie_p不大于等于s长度，child_p不大于等于g长度
    3. 如果当前的cookie_p大于等于child_p，则结果加一，两个指针都加一
    4. 否则child_p加一
    """
    # 1. 生成cookie_p，child_p指针分别指向s和g
    result = 0
    cookies.sort()
    children.sort()
    cookie_p, child_p = 0, 0
    # 2. 遍历，条件为cookie_p不大于等于s长度，child_p不大于等于g长度
    while (cookie_p < len(cookies)) and (child_p < len(children)):
        # 3. 如果当前的cookie_p大于等于child_p，则结果加一，两个指针都加一
        if cookies[cookie_p] >= children[child_p]:
            result += 1
            cookie_p += 1
            child_p += 1
            continue
        # 4. 否则child_p加一
        cookie_p += 1

    return result


if __name__ == '__main__':
    cookies = [5, 6, 7, 8]
    children = [10, 9, 8, 7]
    cookies = [1, 1]
    children = [1, 2]
    print(dispatch_cookie(cookies, children))

