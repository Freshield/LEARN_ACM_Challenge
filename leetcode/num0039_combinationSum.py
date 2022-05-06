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
        1. dp的含义：dp[i]代表当前的target下的所有组合
        2. dp的转换方程：遍历candidates，得到差值rest_val，如果差值大于0遍历dp[rest_val]把当前num进行合并
            为了避免重复，遍历同时需要维护一个已经访问的值的表
        3. dp的初始化：初始化为空列表即可
        4. dp的遍历方向：i依赖于小的方向，从小到大遍历即可
    """
    def __init__(self):
        self.rst_list = []

    def combinationSum(self, candidates, target):
        """
        整体流程：
        1. 对candidates进行排序
        2. 初始化dp矩阵
        3. 遍历candidates中最小的值到target+1
        4. 遍历candidates，计算rest_val
        5. 如果已经访问过则continue
        6. 如果rest_val小于0，直接break
        7. 如果rest_val等于0，则放入num自己，然后break
        8. 如果rest_val大于0，则找到dp[rest_val]并遍历值合并，同时记录当前的已经访问过得num和rest_val
        9. 返回dp[target]
        """
        # 1. 对candidates进行排序
        candidates.sort()

        # 2. 初始化dp矩阵
        dp = [[] for _ in range(target+1)]
        dp[0] = [[]]

        # 3. 遍历candidates中最小的值到target+1
        for target_val in range(candidates[0], target+1):
            visited = []
            # 4. 遍历candidates，计算rest_val
            for num in candidates:
                # 5. 如果已经访问过则continue
                if num in visited:
                    continue
                elif num > target_val:
                    break
                # 6. 如果rest_val小于0，直接break
                rest_val = target_val - num
                if rest_val < 0:
                    break
                # 7. 如果rest_val等于0，则放入num自己，然后break
                # 8. 如果rest_val大于0，则找到dp[rest_val]并遍历值合并，同时记录当前的已经访问过得num和rest_val
                else:
                    for rest_val_list in dp[rest_val]:
                        tmp_list = rest_val_list[:] + [num]
                        tmp_list.sort()
                        if tmp_list not in dp[target_val]:
                            dp[target_val].append(tmp_list)

                    if rest_val != 0:
                        visited.append(rest_val)
                    else:
                        break

        return dp[target]

    def combinationSum_reverse_dp(self, candidates, target):
        dp = [[] for _ in range(target+1)]

        # 这里一定要将candidates降序排列
        for num in sorted(candidates, reverse=True):
            for target_val in range(num, target + 1):
                if target_val == num:
                    dp[target_val] = [[num]]
                else:
                    extend_index = target_val - num
                    dp[target_val].extend([dp_val + [num] for dp_val in dp[extend_index]])
        return dp[target]

    def combinationSum_dfs(self, candidates, target, com_list=[], begin_index=0):
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
                self.combinationSum_dfs(candidates, calculed, com_list, i)
                com_list.pop(-1)

        return self.rst_list


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))