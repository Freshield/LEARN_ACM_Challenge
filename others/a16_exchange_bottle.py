# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a16_exchange_bottle.py
@Time: 2020-04-25 21:57
@Last_update: 2020-04-25 21:57
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
    “某商店规定：三个空汽水瓶可以换一瓶汽水。
    小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？
    ”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，
    喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。
    然后你让老板先借给你一瓶汽水，喝掉这瓶满的，
    喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，
    最多可以换多少瓶汽水喝？
    """
    def exchange_bottle(self, bottles, sum_val=0):
        """
        使用递归来得到结果
        整体流程：
        1. 结束条件：n <= 1, 返回sum_val，n==2, 返回sum_val+1
        2. 得到商和余数
        3. 继续递归
        4. 返回sum_val
        """
        # 1. 结束条件：n <= 1, 返回sum_val，n==2, 返回sum_val+1
        if bottles <= 1:
            return sum_val
        elif bottles == 2:
            return sum_val + 1

        # 2. 得到商和余数
        exchanges = bottles // 3
        release = bottles % 3
        sum_val += exchanges

        # 3. 继续递归
        sum_val = self.exchange_bottle(exchanges + release, sum_val)

        # 4. 返回sum_val
        return sum_val


def input_to_str():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            print(Solution().exchange_bottle(n))
        except Exception as e:
            break

if __name__ == '__main__':
    bottles = 10
    print(Solution().exchange_bottle(bottles))