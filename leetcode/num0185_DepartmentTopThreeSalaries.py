# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0185_DepartmentTopThreeSalaries.py
@Time: 2020-07-09 14:33
@Last_update: 2020-07-09 14:33
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
"""
Employee 表包含所有员工信息，每个员工有其对应的工号 Id，姓名 Name，工资 Salary 和部门编号 DepartmentId 。
Department 表包含公司所有部门的信息。
编写一个 SQL 查询，找出每个部门获得前三高工资的所有员工。例如，根据上述给定的表，查询结果应返回
"""

sql_str = 'select d.Name as "Department", e1.Name as "Employee", e1.Salary from ' \
          'Employee as e1 join Department as d on e1.DepartmentId = d.Id ' \
          'where 3 > (' \
          '    select count(distinct e2.Salary) from Employee as e2 where ' \
          '    e1.Salary < e2.Salary and e1.DepartmentId = e2.DepartmentId);'