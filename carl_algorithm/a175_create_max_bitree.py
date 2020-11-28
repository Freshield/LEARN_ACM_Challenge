# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a175_create_max_bitree.py
@Time: 2022-12-16 22:50
@Last_update: 2022-12-16 22:50
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import create_tree, TreeNode


def create_max_bitree(num_list):
    """
    创建最大二叉树
    """
    def _recursion(num_list: list):
        """
        递归部分
        1. 参数返回，参数为num list，返回为树节点
        2. 停止条件，如果当前列表为空或者只有一个节点，则进行相应的返回
        3. 递归逻辑，先找到当前数组最大的节点和位置，创建根节点
        4. 当前节点的左节点为递归左边的数组
        5. 当前节点的右节点为递归右边的数组
        """
        # 2. 停止条件，如果当前列表为空或者只有一个节点，则进行相应的返回
        if len(num_list) == 0:
            return None
        if len(num_list) == 1:
            return TreeNode(val=num_list[0])
        # 3. 递归逻辑，先找到当前数组最大的节点和位置，创建根节点
        max_index = num_list.index(max(num_list))
        max_value = num_list[max_index]
        this_node = TreeNode(max_value)
        # 4. 当前节点的左节点为递归左边的数组
        this_node.left = _recursion(num_list[:max_index])
        # 5. 当前节点的右节点为递归右边的数组
        this_node.right = _recursion(num_list[max_index+1:])

        return this_node

    return _recursion(num_list)


if __name__ == '__main__':
    num_list = [3, 2, 1, 6, 0, 5]
    print(create_max_bitree(num_list))
