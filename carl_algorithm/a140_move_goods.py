# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_move_goods.py
@Time: 2022-10-20 15:01
@Last_update: 2022-10-20 15:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def get_car_times(goods_list, car_weight):
    """
    获取当前重量下，汽车需要的次数
    整体流程：
    1. 生成所需的count，sum
    2. 遍历goods list，累加和
    3. 如果当前和大于car weight，则count加一，sum为当前good的值
    4. 处理最后一次
    """
    # 1. 生成所需的count，sum
    count, sum = 0, 0
    # 2. 遍历goods list，累加和
    for good_value in goods_list:
        sum += good_value
        # 3. 如果当前和大于car weight，则count加一，sum为当前good的值
        if sum > car_weight:
            count += 1
            sum = good_value
    # 4. 处理最后一次
    count += 1

    return count


def move_goods(goods_list, target_days):
    """
    求出要在target days内办完goods列表的最小载重量
    物品的最大值保证肯定能运完，物品总和保证一次就能运完，再在中间的重量通过二分法进行遍历
    整体流程：
    1. 去除空的情况
    2. 获取物品的最大值以及总和，用left和right表示，方便之后计算mid
    3. 遍历，条件为left小于right，使用左闭右开
    4. 得到mid，以及需要的次数
    5. 如果等于目标次数则直接返回
    6. 如果当前需要的次数大于目标次数则加大重量，left变为mid+1
    7. 否则则减少重量，right变为mid
    """
    # 1. 去除空的情况
    if (len(goods_list) == 0) or (target_days == 0):
        return 0
    # 2. 获取物品的最大值以及总和，用left和right表示，方便之后计算mid
    left = max(goods_list)
    right = sum(goods_list)
    # 3. 遍历，条件为left小于right，使用左闭右开
    while left < right:
        # 4. 得到mid，以及需要的次数
        mid = (left + right) // 2
        car_times = get_car_times(goods_list, mid)
        # 5. 如果等于目标次数则直接返回
        if car_times == target_days:
            return mid
        # 6. 如果当前需要的次数大于目标次数则加大重量，left变为mid+1
        if car_times > target_days:
            left = mid + 1
        # 7. 否则则减少重量，right变为mid
        else:
            right = mid

    return -1


if __name__ == '__main__':
    w = [i+1 for i in range(10)]
    d = 5
    print(move_goods(w, d))
