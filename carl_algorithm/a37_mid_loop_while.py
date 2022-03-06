# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a37_mid_loop_while.py
@Time: 2022-04-19 16:40
@Last_update: 2022-04-19 16:40
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree


def mid_loop_while(root):
    """
    中序遍历的迭代方法
    1. 生成结果列表和栈还有指针
    2. 遍历直到指针是None或者栈为空
    3. 如果当前指针不是None，则放入左节点，指针为左节点
    4. 如果是None，则指针为栈的top，放指针数值到结果，然后放入右节点
    """
    # 1. 生成结果列表和栈还有指针
    rst_list, stack = [], []
    cur = root
    # 2. 遍历直到指针是None且栈为空
    while not ((cur is None) and (len(stack) == 0)):
        # 3. 如果当前指针不是None，则放入指针节点，指针为左节点
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        # 4. 如果是None，则指针为栈的top，放指针数值到结果，然后指针为右节点
        else:
            cur = stack.pop()
            rst_list.append(cur.val)
            cur = cur.right

    return rst_list


if __name__ == '__main__':
    num_list = list(range(5))
    root = create_tree(num_list)
    print(mid_loop_while(root))

