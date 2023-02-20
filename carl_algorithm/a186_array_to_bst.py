# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a186_array_to_bst.py
@Time: 2023-01-09 14:33
@Last_update: 2023-01-09 14:33
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


def array_to_bst(nums):
    """
    使用有序队列转换为二叉搜索树，使用递归的方法
    """
    def _recursion(left, right):
        """
        递归逻辑
        1. 参数返回，参数为左右的分割区域left, right，返回为生成的树节点
        2. 停止条件，当left大于right的时候就停止，返回None
        3. 获得中间位置mid，并用mid创建节点
        4. 使用左闭右闭的区间，左子节点为递归左边部分
        5. 右子节点为递归右边部分
        6. 返回当前节点
        """
        # 2. 停止条件，当left大于right的时候就停止，返回None
        if left > right:
            return None
        # 3. 获得中间位置mid，并用mid创建节点
        mid = left + (right - left) // 2
        this_node = TreeNode(nums[mid])
        # 4. 使用左闭右闭的区间，左子节点为递归左边部分
        this_node.left = _recursion(left, mid - 1)
        # 5. 右子节点为递归右边部分
        this_node.right = _recursion(mid + 1, right)
        # 6. 返回当前节点
        return this_node

    return _recursion(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-10, -2, 0, 5, 9]
    print(array_to_bst(nums))

