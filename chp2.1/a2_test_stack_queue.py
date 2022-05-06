#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_test_stack.py
@Time: 2020-04-14 10:58
@Last_update: 2020-04-14 10:58
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

a = [1,2,3,4,5]

print(a.pop(-1))
print(a)

print(a.pop(0))
print(a)

a.insert(0, 1)
print(a)

a.append(5)
print(a)
