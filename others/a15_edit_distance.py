# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a15_edit_distance.py
@Time: 2020-04-25 21:12
@Last_update: 2020-04-25 21:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def edit_distance(input_str):
    """
    输入n，接下来2n行，前n行表示待修改文章，后n行表示已修改文章
    输出从待修改文章到已修改文章最少编辑的次数
    一次编辑：删除 添加 替换都算一次编辑
    解法：
    使用动态规划
    1. dp的含义：dp[i][j]代表word1的i变为word2的j所需要的改表次数
    2. dp的转换公式：
        i. 如果word1[i]==word2[j]则dp[i][j]=dp[i-1][j-1]

        不等的话有三种情况：
        ii. 替换：dp[i][j] = dp[i-1][j-1] + 1
        iii. 增加：dp[i][j] = dp[i][j-1] + 1
        iv. 删除：dp[i][j] = dp[i-1][j] + 1
    3. dp的初始值：
        增加空字符一列一行，dp[0][j]为一直添加，dp[i][0]为一直删除
    4. dp的遍历方式：
        i的依赖为上边，j的依赖为左边，所以从小到大遍历即可
    整体流程：
    1. 先解析字符串
    2. 遍历字符列表
    3. 计算distance
    4. 合并到一起
    5. 返回结果
    """
    # 1. 先解析字符串
    str_list = input_str.split('\n')
    n = int(str_list[0])
    str_list = str_list[1:]
    raw_str_list = str_list[:(len(str_list)//n)]
    target_str_list = str_list[(len(str_list)//n):]

    # 2. 遍历字符列表
    distance = 0
    for index in range(len(raw_str_list)):
        raw_str = raw_str_list[index]
        target_str = target_str_list[index]
        # 3. 计算distance
        m = len(raw_str)
        n = len(target_str)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if raw_str[i-1] == target_str[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1] + 1,
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1
                    )

        distance += dp[m-1][n-1]

    return distance



if __name__ == '__main__':
    input_str = '2\n' \
                'abcdef\n' \
                '2334\n' \
                'bcdg\n' \
                '123'
    distance = edit_distance(input_str)
    print(distance)