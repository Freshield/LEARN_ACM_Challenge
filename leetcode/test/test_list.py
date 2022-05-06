# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: test_list.py
@Time: 2020-06-10 11:45
@Last_update: 2020-06-10 11:45
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

a = [[]] * 5
print(a) # [[], [], [], [], []]
a[2] = [5]
print(a) # [[], [], [5], [], []]
a[3] = [4]
print(a) # [[], [], [5], [4], []]
a[1].append(1)
print(a) # [[1], [1], [5], [4], [1]]
a[4].extend([2,3])
print(a) # [[1, 2, 3], [1, 2, 3], [5], [4], [1, 2, 3]]
a[2].append(10)
print(a) # [[1, 2, 3], [1, 2, 3], [5, 10], [4], [1, 2, 3]]
a[3].extend([4,5,6])
print(a) # [[1, 2, 3], [1, 2, 3], [5, 10], [4, 4, 5, 6], [1, 2, 3]]
print()

dp = {i: [] for i in range(5)}
print(dp)
dp[1].append(1)
print(dp)
print()

b = [[] for _ in range(10)]
# b = [[]] * 10
print(b)
c = [b[i] for i in range(len(b))]
for i in range(len(b)):
    b[i].append(i)
for i in range(len(c)):
    c[i] += [i]
d = [c[i] + [i] for i in range(len(c))]
print(b)
print(c)
print(d)
print()

e = [[1,2,3],[2,3,1],[2,3,4]]
print([1,2,3] in e)
print([1,3,2] in e)
print([2,3,4] in e)
print([3,2,4] in e)
