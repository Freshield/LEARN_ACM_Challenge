# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a64_inorder_post_order_build_tree.py
@Time: 2022-04-26 20:10
@Last_update: 2022-04-26 20:10
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


def inorder_postorder_build_tree(_inorder_list, _postorder_list):
    """
    通过中序和后序结果重构树，递归不断缩小空间，参返，结束，逻辑
    1. 参返：输入为当前的inorder和postorder列表，返回为当前部分的根节点
    2. 结束：如果当前列表为空则返回None
    3. 逻辑：先通过后序找到当前的根节点，然后找到中序相应的位置
    4. 把中序列表根据根节点分为左右列表
    5. 通过左右列表的长度得到后序列表的左右列表
    6. 进行递归，然后和根节点连接，返回
    """
    # 1. 参返：输入为当前的inorder和postorder列表，返回为当前部分的根节点
    def inner_loop(_inner_inorder, _inner_postorder):
        # 2. 结束：如果当前列表为空则返回None
        if len(_inner_inorder) == 0:
            return None
        # 3. 逻辑：先通过后序找到当前的根节点，然后找到中序相应的位置
        root_val = _inner_postorder[-1]
        root = TreeNode(root_val)
        inorder_index = _inner_inorder.index(root_val)
        # 4. 把中序列表根据根节点分为左右列表
        inorder_left = _inner_inorder[:inorder_index]
        inorder_right = _inner_inorder[inorder_index+1:]
        # 5. 通过左右列表的长度得到后序列表的左右列表
        postorder_left = _inner_postorder[:len(inorder_left)]
        postorder_right = _inner_postorder[len(inorder_left): len(inorder_left)+len(inorder_right)]

        assert (len(inorder_left) == len(postorder_left)) and (len(inorder_right) == len(postorder_right))

        # 6. 进行递归，然后和根节点连接，返回
        left_root = inner_loop(inorder_left, postorder_left)
        right_root = inner_loop(inorder_right, postorder_right)
        root.left = left_root
        root.right = right_root

        return root

    if (len(_inorder_list) == 0) or (len(_postorder_list) == 0):
        return None

    return inner_loop(_inorder_list, _postorder_list)


if __name__ == '__main__':
    root = create_tree([3, 9, 20, None, None, 15, 7])
    inorder_list = [9, 3, 15, 20, 7]
    postorder_list = [9, 15, 7, 20, 3]
    print(inorder_postorder_build_tree(inorder_list, postorder_list))

