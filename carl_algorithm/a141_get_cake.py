# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t2_get_cake.py
@Time: 2022-10-20 15:47
@Last_update: 2022-10-20 15:47
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def get_cake(M, N, K):
    """
    双人抢夺两堆蛋糕，M，N，每次可以拿1->K个，
    对于每堆蛋糕如果可以被K+1整除，则对于这堆蛋糕，先拿的人无法拿到这堆的最后一个
    于是会有四种情况，M可以或者不可以整除，N可以或者不可以整除
    对于M可以N不可以，和N可以M不可以是一样的，这时候先手可以保证自己在其中一堆最后一个，
    而另一堆第一个会输，所有先手会赢
    对于M,N都不可以整除，那么先手在一堆中会是最后一个拿，而另一堆则是后拿，这时候先手会输
    对于M,N都可以整除，情况也是类似，先手在一堆中会是倒数第二个拿，而另一堆是第一个拿，这个时候先手也会输
    综上可以看出，主要在于M,N是否同时同时可以被整除
    整体流程：
    1. 获取M是否可被整除
    2. 获取N是否可被整除
    3. 使用异或逻辑返回
    """
    # 1. 获取M是否可被整除
    is_M_div = M % (K + 1) == 0
    # 2. 获取N是否可被整除
    is_N_div = N % (K + 1) == 0
    # 3. 使用异或逻辑返回
    return is_M_div ^ is_N_div


if __name__ == '__main__':
    M = 4
    N = 3
    K = 2
    print(get_cake(M, N, K))
