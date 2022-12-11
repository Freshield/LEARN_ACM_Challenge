# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a174_midorder_postorder_reconstruct_tree.py
@Time: 2022-12-11 12:40
@Last_update: 2022-12-11 12:40
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a32_treenode import TreeNode


def midorder_postorder_reconstruct_tree(mid_list, post_list):
    """
    通过中序遍历和后续遍历结果重建二叉树
    1. 构建递归逻辑
    """
    def _recursion(rec_mid_list, rec_post_list):
        """
        遍历递归部分
        1. 参数返回，参数为中序后序列表，返回为分割节点
        2. 停止条件，如果列表长度为0则返回None，如果为1则返回当前节点
        3. 递归逻辑，找到后序的最后一个数值，为分割节点
        4. 在中序中，根据此节点把列表分为左右两部分
        5. 对左部分进行递归为左节点
        6. 对右部分进行递归为右节点
        7. 返回分割节点树
        """
        assert len(rec_mid_list) == len(rec_post_list), 'The length not equal'
        # 2. 停止条件，如果列表长度为0则返回None，如果为1则返回当前节点
        if len(rec_mid_list) == 0:
            return None
        if len(rec_mid_list) == 1:
            return TreeNode(val=rec_mid_list[0])
        # 3. 递归逻辑，找到后序的最后一个数值，为分割节点
        mid_val = rec_post_list[-1]
        mid_node = TreeNode(mid_val)
        # 4. 在中序中，根据此节点把列表分为左右两部分
        index = rec_mid_list.index(mid_val)
        mid_left_list, mid_right_list = rec_mid_list[:index], rec_mid_list[index+1:]
        post_left_list, post_rigth_list = rec_post_list[:len(mid_left_list)], rec_post_list[len(mid_left_list): -1]
        assert len(mid_left_list) == len(post_left_list)
        assert len(mid_right_list) == len(post_rigth_list)
        # 5. 对左部分进行递归为左节点
        mid_node.left = _recursion(mid_left_list, post_left_list)
        # 6. 对右部分进行递归为右节点
        mid_node.right = _recursion(mid_right_list, post_rigth_list)
        # 7. 返回分割节点树
        return mid_node

    # 1. 构建递归逻辑
    return _recursion(mid_list, post_list)


if __name__ == '__main__':
    in_order = [9, 3, 15, 20, 7]
    post_order = [9, 15, 7, 20, 3]
    print(midorder_postorder_reconstruct_tree(in_order, post_order))
