# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a11_max_stack_num.py
@Time: 2020-04-25 17:17
@Last_update: 2020-04-25 17:17
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
    输入内容描述
    第1行：调用关系总组数n  第1组被调函数个数  第2组被调函数个数 ... 第n组被调函数个数
    第2行：调用函数1  调用函数栈大小  被调函数1 ... 被调函数n
    ...
    第n+1行：调用函数n  函数n栈大小  被调函数1 ... 被调函数n
    1、所有调用栈中栈总和的最大值，注意输入之中的入口函数可能不唯一，
    比如可能存在1调用2、3，5调用6，6调用7，则有1->2，1->3，5->6->7三个调用链，
    有2个入口函数1和5。
    2、所有调用链中只要存在一个递归调用（即直接或间接调用自己，
    比如1->2->3->1即为递归调用），则输出R。
    3、如果调用链中有函数未给出调用栈大小，则输出为K。
    （这里也看不太清，就假设输出为K，影响不大。）
    """
    max_sum = -1

    def backtrack(self, key, relation_dict, sum_val, used_list):
        """
        深度优先搜索加回溯算法，递归找寻所有遍历的可能性
        整体流程：
        1. 异常情况：如果key已经在used_list中则返回R
        2. 结束条件：如果当前key的next为空则到达了最后，和最大值比较
        3. 遍历key的next列表
        4. 选择，递归，回溯
        """
        # 1. 异常情况：如果key已经在used_list中则返回R
        if key in used_list:
            return 'R'

        # 2. 结束条件：如果当前key的next为空则到达了最后，和最大值比较
        if len(relation_dict[key]['next']) == 0:
            sum_val += relation_dict[key]['weight']
            self.max_sum = self.max_sum if self.max_sum > sum_val else sum_val
            return True

        # 3. 遍历key的next列表
        for next in relation_dict[key]['next']:
            # 4. 选择，递归，回溯
            sum_val += relation_dict[key]['weight']
            used_list.append(key)
            self.backtrack(next, relation_dict, sum_val, used_list)
            sum_val -= relation_dict[key]['weight']
            used_list.pop(-1)

    def max_stack_num(self, input_str):
        """
        整体流程：
        1. 读取字符串解析为字符列表
        2. 根据字符列表生成关系字典
        3. 根据关系字典调用回溯算法
        4. 返回搜索到的最大值
        """
        # 1. 读取字符串解析为字符列表
        str_list = [[j.strip() for j in i.split(' ') if j != ''] for i in input_str.split('\n') if len(i) != 0]
        str_list = str_list[1:]
        # 2. 根据字符列表生成关系字典
        relation_dict = dict()
        for sub_list in str_list:
            # 去除未给出调用栈大小的情况
            if len(sub_list) < 2:
                return 'K'

            relation_dict[sub_list[0]] = {
                'weight': int(sub_list[1]),
                'next': [],
                'pre': []
            }
            for i in sub_list[2:]:
                relation_dict[sub_list[0]]['next'].append(i)
        # 生成pre
        for key, value in relation_dict.items():
            for next in value['next']:
                relation_dict[next]['pre'].append(key)
        # 找到最开始的节点
        start_key = None
        for key, value in relation_dict.items():
            if len(value['pre']) == 0:
                start_key = key
                break

        # 3. 根据关系字典调用回溯算法
        self.backtrack(start_key, relation_dict, 0, [])

        return self.max_sum


if __name__ == '__main__':
    input_str = '' \
                '5  2  3  1  0  0\n' \
                '1  20  2  3\n' \
                '2  30  3  4  5\n' \
                '3  50  4\n' \
                '4  60\n' \
                '5  80\n'
    stack_num = Solution().max_stack_num(input_str)
    print(stack_num)