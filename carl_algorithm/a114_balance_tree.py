# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a114_balance_tree.py
@Time: 2022-10-16 16:53
@Last_update: 2022-10-16 16:53
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from collections import deque
from a91_tree_struct import make_tree


def balance_tree(root):
    """
    判断是否为对称树，使用层序遍历
    1. 处理空的情况
    2. 创建结果列表，节点队列
    3. 遍历，条件为节点队列不为空
    4. 获取节点队列长度
    5. 遍历节点队列
    6. 获取节点队列最左推出节点
    7. 如果当前节点不为空，把左右节点放到节点队列中，并把数值放到本层列表中
    8. 如果为空则直接放None
    9. 使用双指针判断本层是否对称
    """
    # 1. 处理空的情况
    if root is None:
        return False
    # 2. 节点队列
    node_queue = deque([root])
    # 3. 遍历，条件为节点队列不为空
    while len(node_queue) != 0:
        # 4. 获取节点队列长度
        length, layer_list = len(node_queue), []
        # 5. 遍历节点队列
        for _ in range(length):
            # 6. 获取节点队列最左推出节点
            cur_node = node_queue.popleft()
            # 7. 如果当前节点不为空，把左右节点放到节点队列中，并把数值放到本层列表中
            if cur_node is not None:
                layer_list.append(cur_node.val)
                node_queue.append(cur_node.left)
                node_queue.append(cur_node.right)
            else:
                # 8. 如果为空则直接放None
                layer_list.append(None)
        # 9. 使用双指针判断本层是否对称
        left, right = 0, len(layer_list) - 1
        while left < right:
            if layer_list[left] != layer_list[right]:
                return False
            left += 1
            right -= 1

    return True


if __name__ == '__main__':
    node = make_tree([1, 2, 2, None, 3, None, 3])
    print(node)
    print(balance_tree(node))




