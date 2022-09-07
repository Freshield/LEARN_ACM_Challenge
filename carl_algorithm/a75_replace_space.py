# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a75_replace_space.py
@Time: 2022-10-09 14:14
@Last_update: 2022-10-09 14:14
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def replace_space(_s: str):
    """
    替换空格
    1. 首先获取字符串中空格的数量
    2. 转换字符串为数组并增加空格数*2的长度
    3. 设置left，right双指针为字符串结尾和数组的结尾
    4. 遍历，条件为left>=0
    5. 如果left的值不为空格则直接拷贝left的值到right，并更新left，right
    6. 如果为空格，则加入%20到right相应的位置，并更新left，right
    """
    # 1. 首先获取字符串中空格的数量
    space_num = _s.count(' ')
    # 2. 转换字符串为数组并增加空格数*2的长度
    word_list = list(_s) + ['0'] * 2 * space_num
    # 3. 设置left，right双指针为字符串结尾和数组的结尾
    left, right = len(_s) - 1, len(word_list) - 1
    # 4. 遍历，条件为left>=0
    while left >= 0:
        # 5. 如果left的值不为空格则直接拷贝left的值到right，并更新left，right
        if word_list[left] != ' ':
            word_list[right] = word_list[left]
            left -= 1
            right -= 1
            continue
        # 6. 如果为空格，则加入%20到right相应的位置，并更新left，right
        word_list[right-2], word_list[right-1], word_list[right] = '%', '2', '0'
        left -= 1
        right -= 3

    return ''.join(word_list)


if __name__ == '__main__':
    s = 'we are the world'
    print(replace_space(s))
