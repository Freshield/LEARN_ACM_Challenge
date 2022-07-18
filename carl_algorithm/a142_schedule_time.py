# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t2_schedule_time.py
@Time: 2022-10-24 20:33
@Last_update: 2022-10-24 20:33
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def schedule_time(time_list):
    """
    规划时间序列，使用回溯
    1. 对time list按照开始时间倒序排列
    2. 进行回溯
    3. 对于结果进行排序
    4. 恢复正常顺序
    """
    # 1. 对time list按照开始时间倒序排列
    time_list.sort(key=lambda x: x[0], reverse=True)
    # print(time_list)

    count_list_dict, max_count = dict(), 0
    path_list = []

    def backtrack(begin_index, max_count):
        """
        回溯递归部分
        1. 参数返回，begin_index
        2. 停止条件，begin_index等于time list的长度，则和总count进行对比，
        如果大于则更新结果列表，如果等于则先放到结果哈希中
        3. 回溯逻辑，遍历，从begin index到time list的长度
        4. 如果当前tuple不满足条件，则跳过
        5. 如果当前tuple可以满足条件，则放到path中
        6. 回溯递归，弹出tuple
        """
        # 2. 停止条件，begin_index等于time list的长度，则和总count进行对比，
        # 如果大于则更新结果列表，如果等于则先放到结果哈希中
        if begin_index == len(time_list):
            this_count = len(path_list)
            if this_count > max_count:
                max_count = this_count
                count_list_dict[max_count] = [path_list[:]]
            elif this_count == max_count:
                count_list_dict[max_count].append(path_list[:])

            return max_count

        # 3. 回溯逻辑，遍历，从begin index到time list的长度
        for i in range(begin_index, len(time_list)):
            # 4. 如果当前tuple不满足条件，则跳过
            is_append = False
            this_begin, this_end = time_list[i]
            if (len(path_list) == 0) or (this_end <= path_list[-1][0]):
                # 5. 如果当前tuple可以满足条件，则放到path中
                path_list.append(time_list[i])
                is_append = True
            # 6. 回溯递归，弹出tuple
            max_count = backtrack(i+1, max_count)
            if is_append:
                path_list.pop()

        return max_count

    # 2. 进行回溯
    max_count = backtrack(0, max_count)
    # print(max_count)
    # print(count_list_dict)

    # 3. 对于结果进行去重
    res_list = count_list_dict[max_count]
    for sub_list in res_list:
        sub_list.sort(key=lambda x: x[1])
    res_list.sort(key=lambda x: x[0][1])
    # print(res_list)

    # 4. 恢复正常顺序
    return res_list[0]


if __name__ == '__main__':
    import sys
    # time_list = [(3, 6), (1, 5), (6, 7)]
    # time_list = [(6, 7), (8, 10), (9, 10)]
    # time_list = [(3, 6), (4, 5), (6, 7), (8, 10), (9, 10)]
    #
    # print(schedule_time(time_list))

    # line = '(3, 6) (4, 5) (6, 7) (8, 10) (9, 10)'
    # line = f'[{line.replace(", ", ",").replace(" ", ",")}]'
    # time_list = eval(line)
    # print(schedule_time(time_list))
    for line in sys.stdin:
        line = f'[{line.replace(", ", ",").replace(" ", ",")}]'
        time_list = eval(line)
        res_list = schedule_time(time_list)
        print(f'count:{len(res_list)}')
        res_str = str(res_list)[1: -1].replace(', ', ',').replace('),', ') ')
        print(res_str)
