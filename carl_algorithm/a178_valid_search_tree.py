# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a178_valid_search_tree.py
@Time: 2022-12-20 20:18
@Last_update: 2022-12-20 20:18
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


def valid_search_tree(root):
    """
    验证二叉搜索树，使用递归的方式
    通过返回的最大最小值进行比较，使用后序遍历
    """
    def _recursion(node):
        """
        递归逻辑，前序遍历
        1. 参数返回，参数为节点，返回为是否为二叉搜索树，最小值，最大值
        2. 递归逻辑，先获取当前节点的值
        3. 如果左节点不为空，则递归获取左节点
        4. 如果右节点不为空，则递归获取右节点
        5. 获取子树是否是搜索二叉树，子树最小值，子树最大值
        6. 如果其中一个子树不为搜索二叉树直接返回false，val，val
        7. 判断左树的数值是否都小于当前节点
        8. 判断右树的值是否都大于当前节点
        9. 返回是否为二叉搜索树，最小值，最大值
        """
        # 2. 递归逻辑，先获取当前节点的值
        this_val = node.val
        val_list = [this_val]
        # 3. 如果左节点不为空，则递归获取左节点
        if node.left is not None:
            left_val = node.left.val
            # 5. 获取子树是否是搜索二叉树，子树最小值，子树最大值
            is_search, low_val, high_val = _recursion(node.left)
            # 6. 如果其中一个子树不为搜索二叉树直接返回false，val，val
            if not is_search:
                return False, this_val, this_val
            # 8. 判断右树的值是否都大于当前节点
            if (low_val < this_val) and (left_val < this_val) and (high_val < this_val):
                val_list += [low_val, left_val, high_val]
            else:
                return False, this_val, this_val

        # 4. 如果右节点不为空，则递归获取右节点
        if node.right is not None:
            right_val = node.right.val
            # 5. 获取子树是否是搜索二叉树，子树最小值，子树最大值
            is_search, low_val, high_val = _recursion(node.right)
            # 6. 如果其中一个子树不为搜索二叉树直接返回false，val，val
            if not is_search:
                return False, this_val, this_val
            # 7. 判断左树的数值是否都小于当前节点
            if (this_val < low_val) and (this_val < right_val) and (this_val < high_val):
                val_list += [low_val, right_val, high_val]
            else:
                return False, this_val, this_val

        # 9. 返回是否为二叉搜索树，最小值，最大值
        max_val, min_val = max(val_list), min(val_list)

        return True, min_val, max_val

    is_search, _, _ = _recursion(root)

    return is_search


if __name__ == '__main__':
    root = create_tree([5, 1, 4, None, None, 3, 6])
    root = create_tree([2, 1, 3])
    print(valid_search_tree(root))
