# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0039_combinationSum.py
@Time: 2020-06-10 11:08
@Last_update: 2020-06-10 11:08
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution:
    """
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的数字可以无限制重复被选取。
    说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。 
    解法：
    1. 使用回溯算法加上剪枝
    2. 使用动态规划
    """
    def __init__(self):
        self.rst_list = []

    def combinationSum(self, candidates, target, com_list=[], begin_index=0):
        """
        回溯剪枝算法
        整体流程：
        1. 对candidates进行排序
        2. 遍历数值
        3. 如果target减去数值小于0则跳出
        4. 如果target减去数值等于0则保存
        5. 如果target减去数值大于0则递归，之后恢复
        """
        # 1. 对candidates进行排序
        if len(com_list) == 0:
            candidates.sort()

        # 2. 遍历数值
        for i in range(begin_index, len(candidates)):
            num = candidates[i]
            calculed = target - num
            # 3. 如果target减去数值小于0则跳出
            if calculed < 0:
                break
            # 4. 如果target减去数值等于0则保存
            elif calculed == 0:
                com_list.append(num)
                self.rst_list.append(com_list[:])
                com_list.pop(-1)
                break
            # 5. 如果target减去数值大于0则递归，之后恢复
            else:
                com_list.append(num)
                self.combinationSum(candidates, calculed, com_list, i)
                com_list.pop(-1)

        return self.rst_list


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))