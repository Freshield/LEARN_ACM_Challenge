# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a126_repaire_ip_addr.py
@Time: 2022-10-18 21:21
@Last_update: 2022-10-18 21:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def is_valid(sub_str):
    """
    判断当前str是否有效
    1. 位数大于1，且开头是0则为False
    2. 位数大于3则返回False
    3. int之后结果大于255则为False
    """
    if len(sub_str) == 0:
        return False
    # 1. 位数大于1，且开头是0则为False
    if (len(sub_str) > 1) and (sub_str[0] == '0'):
        return False
    # 2. 位数大于3则返回False
    if len(sub_str) > 3:
        return False
    # 3. int之后结果大于255则为False
    if int(sub_str) > 255:
        return False

    return True


def repair_ip_addr(s):
    """
    复原ip地址，给出所有可能的ip地址，回溯递归
    1. 处理空的情况
    2. 创建path列表，结果列表
    3. 调用回溯算法
    """
    # 1. 处理空的情况
    if len(s) < 4:
        return []
    # 2. 创建path列表，结果列表
    path_list, res_list = [], []

    def backtrack(start_index):
        """
        回溯递归部分
        1. 参数返回，参数start_index
        2. 停止条件，当path列表长度为3的时候，如果当前begin_index到结尾也符合条件则合并放到结果列表，否则直接返回
        3. 回溯逻辑，遍历i从start_index到start_index+3，获取当前截取的字符串
        4. 如果符合条件，则放到path，否则continue
        5. 回溯递归i+1，path弹出
        """
        # 2. 停止条件，当path列表长度为3的时候，如果当前begin_index到结尾也符合条件则合并放到结果列表，否则直接返回
        if len(path_list) == 3:
            sub_str = s[start_index:]
            if is_valid(sub_str):
                res_list.append('.'.join(path_list + [sub_str]))
            return
        # 3. 回溯逻辑，遍历i从start_index到start_index+3，获取当前截取的字符串
        for i in range(start_index, start_index+3):
            if i == len(s):
                break
            sub_str = s[start_index: i+1]
            # 4. 如果符合条件，则放到path，否则continue
            if not is_valid(sub_str):
                continue
            path_list.append(sub_str)
            # 5. 回溯递归i+1，path弹出
            backtrack(i + 1)
            path_list.pop()

    # 3. 调用回溯算法
    backtrack(0)

    return res_list


if __name__ == '__main__':
    s = '25525511135'
    s = '0000'
    s = '101023'
    print(repair_ip_addr(s))
