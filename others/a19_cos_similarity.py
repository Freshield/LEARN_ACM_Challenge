# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a19_cos_similarity.py
@Time: 2020-04-25 22:41
@Last_update: 2020-04-25 22:41
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


class Solution(object):
    """
    余弦相似度
    """
    def cos_similarity(self, array0, array1):
        upper = np.sum(array0 * array1)
        down = np.sum(np.sqrt(array0 ** 2)) + np.sum(np.sqrt(array1 ** 2)) + 1e-8

        return upper / down


if __name__ == '__main__':
    array0 = np.array([1, 3, 2])
    array1 = np.array([2, 2, 1])
    print(Solution().cos_similarity(array0, array1))