# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0176_SecondHighestSalary.py
@Time: 2020-07-08 09:48
@Last_update: 2020-07-08 09:48
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

SQL = "select (select distinct " \
      "Salary from Employee " \
      "order by Salary desc " \
      "limit 1 offset 1) as SecondHighestSalary;"