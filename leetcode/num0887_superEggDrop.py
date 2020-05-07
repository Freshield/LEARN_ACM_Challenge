#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0887_superEggDrop.py
@Time: 2020-05-07 10:57
@Last_update: 2020-05-07 10:57
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
    你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
    你的目标是确切地知道 F 的值是多少。
    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
    解法：
    使用动态规划
    1. dp的含义：dp[i][j]代表i个区间，j个鸡蛋下最小移动次数
    2. dp的转移公式：
        引入k，1<=k<=i，k代表从区间中的第k个位置开始扔
        那么会有两种情况:
        (1)如果鸡蛋没碎：dp[i][j] = dp[i-k][j] + 1
        (2)如果鸡蛋碎了：dp[i][j] = dp[k-1][j-1] + 1
        我们要假设运气最差的情况，也就是max(dp[i-k][j], dp[k-1][j-1]) + 1
        然后遍历k，从中找到最小的值
        min(max(dp[i-k][j], dp[k-1][j-1]) + 1)
    3. dp的初始化：dp[0][j]=0, dp[1][j]=1, dp[i][0]=0, dp[i][1]=i
    4. dp的遍历方向：
        i的依赖向左，j的依赖向左，k的依赖向左，所以都从小到大遍历
    """
    def superEggDrop(self, K, N):
        """
        K是鸡蛋，N是楼层
        整体流程：
        1. 生成dp矩阵
        2. 初始化dp
        3. 遍历i，j来更新dp矩阵
        4. 返回最终的值
        """
        # 1. 生成dp矩阵
        dp = [[N+1 for _ in range(K+1)] for _ in range(N+1)]
        # 2. 初始化dp
        dp[0][0] = 0
        for i in range(1, N+1):
            dp[i][0] = 0
            dp[i][1] = i
        for j in range(1, K+1):
            dp[0][j] = 0
            dp[1][j] = 1

        # 3. 遍历i，j来更新dp矩阵
        for i in range(2, N+1):
            for j in range(2, K+1):
                for k in range(1, i):
                    dp[i][j] = min(dp[i][j], max(dp[i-k][j], dp[k-1][j-1]) + 1)

        return dp[-1][-1]


if __name__ == '__main__':
    K = 3
    N = 14
    K = 2
    N = 6
    print(Solution().superEggDrop(K, N))