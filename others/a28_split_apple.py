#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a28_split_apple.py
@Time: 2020-04-26 16:39
@Last_update: 2020-04-26 16:39
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
    M个相同苹果放到N个相同篮子里有多少种放法,允许有篮子不放。
    1<=M<=10，1<=N<=10
    例如5个苹果三个篮子，3，1，1 和 1,1,3是同一种放法
    输入 7 3
    输出 8
    解法：
    递归调用
    """
    split_dict = dict()
    split_list = []

    def split_apple(self, m_apple, n_bag):
        """
        整体流程：
        1. 结束条件：n_bag=1时，把情况放到情况字典中
        2. 对于m_apple进行遍历
        3. 选择，递归，回溯
        """
        # 1. 结束条件：n_bag=1时，把情况放到情况字典中
        if n_bag == 1:
            self.split_list.append(m_apple)
            self.split_dict[str(sorted(self.split_list))] = 1
            self.split_list.pop(-1)
            return True

        # 2. 对于m_apple进行遍历
        for i in range(m_apple):
            # 3. 选择，递归，回溯
            self.split_list.append(i)
            self.split_apple(m_apple-i, n_bag-1)
            self.split_list.pop(-1)

        return len(self.split_dict)



if __name__ == '__main__':
    m = 7
    n = 3
    s = Solution()
    print(s.split_apple(m, n))
    print(s.split_dict)