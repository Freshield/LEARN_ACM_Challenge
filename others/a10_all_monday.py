# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a10_all_monday.py
@Time: 2020-04-25 11:27
@Last_update: 2020-04-25 11:27
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
    根据下列信息计算在1900年1月1日至2000年12月31日间共有多少个星期天落在每月的第一天上？
    a) 1900.1.1是星期一
    b) 1月，3月，5月，7月，8月，10月和12月是31天
    c) 4月，6月，9月和11月是30天
    d) 2月是28天，在闰年是29天
    e) 公元年数能被4整除且又不能被100整除是闰年
    f) 能直接被400整除也是闰年
    """
    def all_monday(self, year_t=2000):
        """
        整体流程：
        1. 生成月份的日期列表和初始化条件
        2. 遍历每月的第一天和19010107的日期差和7的余数
        3. 判断是否是闰年更新日期列表
        """
        # 1. 生成月份的日期列表
        month_days_list = [
            31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]
        days = 0
        count = 0

        # 2. 遍历每月的第一天和19010107的日期差和7的余数
        for year in range(1900, year_t+1):
            # 3. 判断是否是闰年更新日期列表
            if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
                month_days_list[1] = 29
            else:
                month_days_list[1] = 28

            for i in range(12):
                # 处理初始情况
                if (year == 1900) and (i == 1):
                    count += 1
                    continue
                else:
                    days += month_days_list[i]

                if days % 7 == 0:
                    count += 1

        return count


if __name__ == '__main__':
    target_year = 2000
    print(Solution().all_monday(target_year))