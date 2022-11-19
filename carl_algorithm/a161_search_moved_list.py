# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a161_search_moved_list.py
@Time: 2022-11-11 12:41
@Last_update: 2022-11-11 12:41
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def search_moved_list(nums, target):
    """
    在旋转的列表中进行搜索，使用二分查找，左闭右开
    1. 创建left，right指针
    2. 遍历，条件为left小于right
    3. 获取mid指针
    4. 如果mid为target则直接返回mid
    5. 情况一，left到mid有序，target值在left到mid之间，则right更新为mid
    6. 情况二，left到mid有序，target值不在left到mid之间，则left更新为mid+1
    7. 情况三，mid到right-1有序，target值在mid到right-1之间，则left更新为mid+1
    8. 情况四，mid到right-1有序，target值不在mid到right-1之间，则right更新为mid
    """
    # 1. 创建left，right指针
    left, right = 0, len(nums)
    # 2. 遍历，条件为left小于right
    while left < right:
        # 3. 获取mid指针
        mid = (left + right) // 2
        # 4. 如果mid为target则直接返回mid
        if nums[mid] == target:
            return mid
        # 5. 情况一，left到mid有序，target值在left到mid之间，则right更新为mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            # 6. 情况二，left到mid有序，target值不在left到mid之间，则left更新为mid+1
            else:
                left = mid + 1
        # 7. 情况三，mid到right-1有序，target值在mid到right-1之间，则left更新为mid+1
        else:
            if nums[mid] < target <= nums[right - 1]:
                left = mid + 1
            # 8. 情况四，mid到right-1有序，target值不在mid到right-1之间，则right更新为mid
            else:
                right = mid

    return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    nums = [1]
    target = 0
    print(search_moved_list(nums, target))
