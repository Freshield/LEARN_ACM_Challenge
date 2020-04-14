#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_cal_sum_k.py
@Time: 2020-04-14 11:03
@Last_update: 2020-04-14 11:03
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def cal_sum_k(index, num_list, k, sum=0):
    """
    计算是否可以从num_list中选出若干数使他们的和为k
    解法：
    使用深度优先搜索，把所有是否相加都进行计算
    整体流程：
    2. 判断是否已经到了n也就是边界了，则返回sum的判别
    3. 如果sum为k则返回True
    4. 判别下一个加的分支
    5. 判别下一个不加的分支
    """
    # 2. 判断是否已经到了n也就是边界了，则返回sum的判别
    if index == len(num_list):
        return sum == k
    # 3. 如果sum为k则返回True
    elif sum == k:
        return True
    # 4. 判别下一个加的分支
    elif cal_sum_k(index+1, num_list, k, sum + num_list[index]):
        return True
    elif cal_sum_k(index+1, num_list, k, sum):
        return True
    else:
        return False


if __name__ == '__main__':
    num_list = [1,2,4,7]
    k = 14
    print(cal_sum_k(0, num_list, k))