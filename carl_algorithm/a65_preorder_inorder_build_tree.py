# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a65_preorder_inorder_build_tree.py
@Time: 2022-04-26 20:28
@Last_update: 2022-04-26 20:28
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


def preorder_inorder_build_tree(_inorder_list, _preorder_list):
    """
    通过中序和后序结果重构树，递归不断缩小空间，参返，结束，逻辑
    1. 参返：输入为当前的inorder和preorder列表，返回为当前部分的根节点
    2. 结束：如果当前列表为空则返回None
    3. 逻辑：先通过前序找到当前的根节点，然后找到中序相应的位置
    4. 把中序列表根据根节点分为左右列表
    5. 通过左右列表的长度得到前序列表的左右列表
    6. 进行递归，然后和根节点连接，返回
    """
    # 1. 参返：输入为当前的inorder和postorder列表，返回为当前部分的根节点
    def inner_loop(_inner_inorder, _inner_preorder):
        # 2. 结束：如果当前列表为空则返回None
        if len(_inner_inorder) == 0:
            return None
        # 3. 逻辑：先通过后序找到当前的根节点，然后找到中序相应的位置
        root_val = _inner_preorder[0]
        root = TreeNode(root_val)
        inorder_index = _inner_inorder.index(root_val)
        # 4. 把中序列表根据根节点分为左右列表
        inorder_left = _inner_inorder[:inorder_index]
        inorder_right = _inner_inorder[inorder_index+1:]
        # 5. 通过左右列表的长度得到后序列表的左右列表
        preorder_left = _inner_preorder[1:len(inorder_left)+1]
        preorder_right = _inner_preorder[len(inorder_left)+1:]

        assert (len(inorder_left) == len(preorder_left)) and (len(inorder_right) == len(preorder_right))

        # 6. 进行递归，然后和根节点连接，返回
        left_root = inner_loop(inorder_left, preorder_left)
        right_root = inner_loop(inorder_right, preorder_right)
        root.left = left_root
        root.right = right_root

        return root

    if (len(_inorder_list) == 0) or (len(_preorder_list) == 0):
        return None

    return inner_loop(_inorder_list, _preorder_list)


if __name__ == '__main__':
    root = create_tree([3, 9, 20, None, None, 15, 7])
    inorder_list = [9, 3, 15, 20, 7]
    preorder_list = [3, 9, 20, 15, 7]
    print(preorder_inorder_build_tree(inorder_list, preorder_list))

