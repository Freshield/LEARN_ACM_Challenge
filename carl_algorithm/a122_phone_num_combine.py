# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a122_phone_num_combine.py
@Time: 2022-10-17 22:18
@Last_update: 2022-10-17 22:18
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def phone_num_combine(phone_num):
    """
    返回电话号码所有可能的组合，使用回溯算法
    1. 生成电话的对应字典
    2. 创建path列表，结果列表
    3. 处理空情况
    4. 调用回溯算法
    """
    # 1. 生成电话的对应字典
    phone_num_dict = {
        '1': ['-'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
        '*': ['-'], '0': ['-'], '#': ['-']
    }
    # 2. 创建path列表，结果列表
    path_list, res_list = [], []

    def backtrack(str_index):
        """
        回溯递归
        1. 参数返回，str_index
        2. 停止条件，当path列表等于phone num长度，则把path列表去除-转换为字符串结果放到结果列表中
        3. 回溯逻辑，获取str_index的字符集合，遍历所有字符，path列表加上字符，回溯str_index+1，path弹出
        """
        # 2. 停止条件，当path列表等于phone num长度，则把path列表去除-转换为字符串结果放到结果列表中
        if len(path_list) == len(phone_num):
            cur_str = ''.join(path_list).replace('-', '')
            res_list.append(cur_str)
            return
        # 3. 回溯逻辑，获取str_index的字符集合，遍历所有字符，path列表加上字符，回溯str_index+1，path弹出
        str_list = phone_num_dict[phone_num[str_index]]
        for sub_str in str_list:
            path_list.append(sub_str)
            backtrack(str_index + 1)
            path_list.pop()
    # 3. 处理空情况
    if phone_num == '':
        return []
    # 4. 调用回溯算法
    backtrack(0)

    return res_list


if __name__ == '__main__':
    phone_num = '23'
    print(phone_num_combine(phone_num))
