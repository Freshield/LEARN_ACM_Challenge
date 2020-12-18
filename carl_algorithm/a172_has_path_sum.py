# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a172_has_path_sum.py
@Time: 2022-12-04 20:52
@Last_update: 2022-12-04 20:52
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import TreeNode, create_tree


def has_path_sum(root, target):
    """
    判断是否有总和为target的路径，使用递归回溯
    1. 处理特殊情况
    2. 创建总和数值
    """
    def _recursion(node, sum_value):
        """
        递归回溯部分
        1. 参数返回，当前的节点以及加上本节点后的总和
        2. 停止条件，当左右节点为空的时候，看当前和是否等于target
        3. 递归逻辑
        4. 如果左节点不为空，加上左节点值递归，然后减掉左节点的值，如果左节点返回True则直接返回True
        5. 如果右节点不为空，加上右节点值递归，然后减掉右节点的值，如果右节点返回True则直接返回True
        """
        # 2. 停止条件，当左右节点为空的时候，看当前和是否等于target
        if (node.left is None) and (node.right is None):
            return sum_value == target
        # 4. 如果左节点不为空，加上左节点值递归，然后减掉左节点的值，如果左节点返回True则直接返回True
        if node.left is not None:
            sum_value += node.left.val
            res = _recursion(node.left, sum_value)
            sum_value -= node.left.val
            if res is True:
                return True
        # 5. 如果右节点不为空，加上右节点值递归，然后减掉右节点的值，如果右节点返回True则直接返回True
        if node.right is not None:
            sum_value += node.right.val
            res = _recursion(node.right, sum_value)
            sum_value -= node.right.val
            if res is True:
                return True
        return False
    # 1. 处理特殊情况
    if root is None:
        return False
    # 2. 创建总和数值
    sum_value = root.val

    return _recursion(root, sum_value)


if __name__ == '__main__':
    root = create_tree([5, 4, 8, 11, None, 13, 4])
    target = 20
    print(has_path_sum(root, target))
