# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a18_distinct_and_sort.py
@Time: 2020-04-25 22:35
@Last_update: 2020-04-25 22:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution(object):
    """
    明明想在学校中请一些同学一起做一项问卷调查，
    为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
    对于其中重复的数字，只保留一个，把其余相同的数去掉，
    不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，
    按照排好的顺序去找同学做调查。
    请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，
    希望大家能正确处理)。
    """
    def distinct_and_sort(self, input_nums):
        return sorted(list(set(input_nums)))


def input_to_str():
    while True:
        try:
            num = int(input())
            num_list = []
            for i in range(num):
                num_list.append(int(input()))
            for i in Solution().distinct_and_sort(num_list):
                print(i)
        except Exception as e:
            break

if __name__ == '__main__':
    input_nums = [2, 2, 1]
    input_nums = [10, 20, 40, 32, 67, 40, 20, 89, 300, 400, 15]
    print(Solution().distinct_and_sort(input_nums))