# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_url_test.py
@Time: 2022-10-24 20:17
@Last_update: 2022-10-24 20:17
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def url_test(url_list):
    """
    拼接url前缀和后缀
    1. 获取前后缀
    2. 处理空的特殊情况
    3. 对前后缀进行处理
    4. 进行拼接
    """
    if len(url_list) == 0:
        return '/'
    # 1. 获取前后缀
    pre, post = url_list
    # 2. 处理空的特殊情况
    if (pre == '') and (post == ''):
        return '/'
    # 3. 对前后缀进行处理
    pre = pre.replace('/', '')
    post = post.replace('/', '')
    # 4. 进行拼接
    return f'/{pre}/{post}'


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        url_list = line.split()
        # print(url_list)
        # print(int(a[0]) + int(a[1]))
        print(url_test(url_list))

    url_list = ['', '']
    print(url_test(url_list))
