# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a125_substr_innerloop.py
@Time: 2022-10-18 17:29
@Last_update: 2022-10-18 17:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def is_palindrome(sub_str):
    """
    判断是否为回文，双指针法
    1. 创建左右指针
    2. 遍历，条件为左指针不大于右指针
    3. 如果左右指针指向的不同则返回False
    4. 更新左右指针
    """
    # 1. 创建左右指针
    left, right = 0, len(sub_str) - 1
    # 2. 遍历，条件为左指针不大于右指针
    while left < right:
        # 3. 如果左右指针指向的不同则返回False
        if sub_str[left] != sub_str[right]:
            return False
        left += 1
        right -= 1

    return True


def substr_inner_loop(s):
    """
    分割回文串，使用回溯递归
    1. 处理空的情况
    2. 生成path列表，结果列表
    3. 调用回溯算法
    """
    # 1. 处理空的情况
    if len(s) == 0:
        return []
    # 2. 生成path列表，结果列表
    path_list, res_list = [], []

    def backtrack(start_index):
        """
        回溯递归
        1. 参数返回，start_index
        2. 停止条件，如果当前start_index大于等于字符串长度，则存path到结果列表中
        3. 回溯逻辑，遍历i从start_index到字符串的长度
        4. 获取当前截取字符串，s[start_index:i+1]，如果不是回文则跳过，否则放到path
        5. 回溯递归，i+1，
        6. path弹出截取字符串
        """
        # 2. 停止条件，如果当前start_index大于等于字符串长度，则存path到结果列表中
        if start_index >= len(s):
            res_list.append(path_list[:])
            return
        # 3. 回溯逻辑，遍历i从start_index到字符串的长度
        for i in range(start_index, len(s)):
            # 4. 获取当前截取字符串，s[start_index:i+1]，如果不是回文则跳过，否则放到path
            sub_str = s[start_index: i + 1]
            if not is_palindrome(sub_str):
                continue
            path_list.append(sub_str)
            # 5. 回溯递归，i+1，
            backtrack(i + 1)
            # 6. path弹出截取字符串
            path_list.pop()

    # 3. 调用回溯算法
    backtrack(0)

    return res_list


if __name__ == '__main__':
    s = 'aab'
    print(substr_inner_loop(s))

