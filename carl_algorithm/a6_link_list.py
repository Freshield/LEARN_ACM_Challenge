# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_link_list.py
@Time: 2022-04-12 15:03
@Last_update: 2022-04-12 15:03
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'# -> {self.next}'
