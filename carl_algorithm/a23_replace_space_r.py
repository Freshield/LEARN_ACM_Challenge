# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a23_replace_space_r.py
@Time: 2022-10-08 22:00
@Last_update: 2022-10-08 22:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def replace_space_r(s):
    """
    替换数组中的空格
    1. 把s变成数组并获得空格的数量
    2. 拓展s数组
    3. 创建left，right指针
    4. 遍历，条件为left>=0
    5. 如果left的值不为空格，则复制值到right，同时更新left，right
    6. 如果left的值为空格，则right反着写入%20，同时更新left，right
    """
    # 1. 把s变成数组并获得空格的数量
    s_list, space_num = list(s), s.count(' ')
    # 2. 拓展s数组
    s_list += [''] * 2 * space_num
    # 3. 创建left，right指针
    left, right = len(s)-1, len(s_list)-1
    # 4. 遍历，条件为left>=0
    while left >= 0:
        # 5. 如果left的值不为空格，则复制值到right，同时更新left，right
        if s_list[left] != ' ':
            s_list[right] = s_list[left]
            left -= 1
            right -= 1
            continue
        # 6. 如果left的值为空格，则right反着写入%20，同时更新left，right
        s_list[right-2], s_list[right-1], s_list[right] = '%', '2', '0'
        left -= 1
        right -= 3

    return ''.join(s_list)


if __name__ == '__main__':
    s = "We are happy."
    print(replace_space_r(s))