# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a168_is_balance_tree.py
@Time: 2022-11-26 17:51
@Last_update: 2022-11-26 17:51
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


def is_balance_tree(root):
    """
    判读是否为平衡二叉树，使用递归方法
    1. 处理特殊情况
    2. 进行递归，返回结果
    """
    def _recursion(node):
        """
        使用递归进行是否为平衡二叉树的判断，递归顺序为中左右
        1. 参数返回，传入相应的节点，返回为当前的深度
        2. 停止条件，当前节点为空则返回0
        3. 递归逻辑，递归获取左节点的深度
        4. 递归获取右节点的深度
        5. 左右节点为-1，如果左右深度相差1，则返回-1
        6. 否则返回1+左右节点中大的值
        """
        # 2. 停止条件，当前节点为空则返回0
        if node is None:
            return 0
        # 3. 递归逻辑，递归获取左节点的高度
        left_depth = _recursion(node.left)
        # 4. 递归获取右节点的深度
        right_depth = _recursion(node.right)
        # 5. 左右节点为-1，如果左右深度相差1，则返回-1
        if (left_depth == -1) or (right_depth == -1) or (
            abs(left_depth - right_depth) > 1
        ):
            return -1
        # 6. 否则返回1+左右节点中大的值
        return 1 + max(left_depth, right_depth)

    # 1. 处理特殊情况
    if root is None:
        return True
    # 2. 进行递归，返回结果
    return False if _recursion(root) == -1 else True


if __name__ == '__main__':
    root = create_tree([3, 9, 20, None, None, 15, 7])
    print(is_balance_tree(root))
