#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_maze_short_path.py
@Time: 2020-04-14 13:45
@Last_update: 2020-04-14 13:45
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np


def maze_short_path(maze_list, start_tuple, goal_tuple):
    """
    寻找起点到重点的最小步数
    解法：
    使用宽度优先搜索，使用queue
    整体流程：
    1. 构建和maze同等大小的步长矩阵
    2. 把起点放到队列
    3. 终止条件为队列为空
    4. 判别四连通，如果是路就放到queue处理
    5. 找到G则break
    6. 返回G的位置的步长
    """
    # 1. 构建和maze同等大小的步长矩阵
    n, m = maze_list.shape
    path_list = np.ones_like(maze_list, dtype=np.int8) * -1
    path_list[start_tuple[0],start_tuple[1]] = 0
    # 2. 把起点放到队列
    process_queue = [start_tuple]
    next_tuple = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 3. 终止条件为队列为空
    while len(process_queue) != 0:
        process_x, process_y = process_queue.pop(0)
        # 4. 判别四连通，如果是路就放到queue处理
        for path_x, path_y in next_tuple:
            next_x = path_x + process_x
            next_y = path_y + process_y
            if (next_x>=0) and (next_x<n) and (next_y>=0) and (next_y<m) and \
                    (maze_list[next_x, next_y] != '#') and (path_list[next_x, next_y] == -1):
                path_list[next_x, next_y] = path_list[process_x, process_y] + 1
                # 5. 找到G则break
                if maze_list[next_x, next_y] == 'G':
                    break
                else:
                    process_queue.append((next_x, next_y))


    return path_list[goal_tuple[0], goal_tuple[-1]]


if __name__ == '__main__':
    maze_list = [
        '#S######.#',
        '......#..#',
        '.#.##.##.#',
        '.#........',
        '##.##.####',
        '....#....#',
        '.#######.#',
        '....#.....',
        '.####.###.',
        '....#...G#'
    ]
    maze_list = np.array([[j for j in i] for i in maze_list])
    print(maze_list.shape)
    print(maze_short_path(maze_list, (0,1), (9, 8)))
