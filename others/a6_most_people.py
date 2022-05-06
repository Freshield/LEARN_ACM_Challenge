#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_most_people.py
@Time: 2020-04-24 11:15
@Last_update: 2020-04-24 11:15
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
    统计投票个数，返回投票最多的人名，相同的话，字典序在前面的优先
    """
    def get_most_people(self, name_list):
        """
        整体流程：
        1. 处理特殊情况
        2. 生成记录字典和最大值
        3. 遍历放到字典和比较最大值
        4. 得到最大值列表
        """
        # 1. 处理特殊情况
        if len(name_list) == 0:
            return None
        elif len(name_list) == 1:
            return name_list[0]

        # 2. 生成记录字典和最大值
        name_dict = dict()
        max_val = -1

        # 3. 遍历放到字典和比较最大值
        for name in name_list:
            name_dict[name] = name_dict.get(name, 0) + 1
            max_val = max_val if max_val > name_dict[name] else name_dict[name]

        # 4. 得到最大值列表
        max_val_list = []
        for key, value in name_dict.items():
            if value == max_val:
                max_val_list.append(key)
        max_val_list.sort()

        return max_val_list[0]


if __name__ == '__main__':
    name_list = ['Lily', 'Tom', 'Lucy', 'Lucy', 'Tim']
    print(Solution().get_most_people(name_list))