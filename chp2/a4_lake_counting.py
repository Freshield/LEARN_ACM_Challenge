#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_lake_counting.py
@Time: 2020-04-14 12:56
@Last_update: 2020-04-14 12:56
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np


def del_linking(lake_i, lake_j, lake_list):
    """
    去除关联的水洼
    整体流程：
    1. 本点去除
    2. 找到周围8个点，如果有水洼则递归
    """
    # 1. 本点去除
    n, m = lake_list.shape
    lake_list[lake_i, lake_j] = '.'
    # 2. 找到周围8个点，如果有水洼则递归
    for i in range(lake_i-1, lake_i+2):
        for j in range(lake_j-1, lake_j+2):
            if (i >= 0) and (i < n) and (j >= 0) and (j < m) and (lake_list[i, j] == 'W'):
                del_linking(i, j, lake_list)


def lake_counting(lake_list):
    """
    求出一共有多少水洼，水洼按八联通
    解法：
    遍历到W，把相连的水洼都去除，看共能遍历几次
    整体路程：
    1. 遍历水洼找W
    2. 若找到则把联通的都去除
    3. 返回去除的次数
    """
    n, m = lake_list.shape
    lake_num = 0
    # 1. 遍历水洼找W
    for i in range(n):
        for j in range(m):
            # 2. 若找到则把联通的都去除
            if lake_list[i,j] == 'W':
                del_linking(i, j, lake_list)
                lake_num += 1

    return lake_num


if __name__ == '__main__':
    lake_list = [
        'W........WW.',
        '.WWW.....WWW',
        '....WW...WW.',
        '.........WW.',
        '.........W..',
        '..W......W..',
        '.W.W.....WW.',
        'W.W.W.....W.',
        '.W.W......W.',
        '..W.......W.'
    ]
    lake_list = np.array([[j for j in i] for i in lake_list])

    print(lake_counting(lake_list))