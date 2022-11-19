# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a24_revert_word_r.py
@Time: 2022-10-08 22:22
@Last_update: 2022-10-08 22:22
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def trim_word(word_list):
    """
    去除字符列表中的多余空格
    1. 创建左右指针以及暂存列表
    2. 对于开头的空格，遍历left直到left不等于空格
    3. 对于结尾的空格，遍历right直到right不等于空格
    4. 遍历left到right+1
    5. 如果left不是空格，直接放到tmp中
    6. 如果left是空格，tmp最后一个不是空格，则放到tmp中
    7. 如果left是空格，tmp最后也是空格则跳过
    """
    # 1. 创建左右指针以及暂存列表
    left, right, tmp = 0, len(word_list)-1, []
    # 2. 对于开头的空格，遍历left直到left不等于空格
    while word_list[left] == ' ':
        left += 1
    # 3. 对于结尾的空格，遍历right直到right不等于空格
    while word_list[right] == ' ':
        right -= 1
    # 4. 遍历left到right+1
    for left in range(left, right + 1):
        # 5. 如果left不是空格，直接放到tmp中
        if word_list[left] != ' ':
            tmp.append(word_list[left])
            continue
        # 6. 如果left是空格，tmp最后一个不是空格，则放到tmp中
        if tmp[-1] != ' ':
            tmp.append(word_list[left])
            continue
        # 7. 如果left是空格，tmp最后也是空格则跳过

    return tmp


def reverse_word(word_list):
    """
    翻转字符
    1. 创建left，right指针
    2. 遍历，条件为left<right
    3. 交换left，right的值
    4. 更新left，right
    """
    # 1. 创建left，right指针
    left, right = 0, len(word_list) - 1
    # 2. 遍历，条件为left<right
    while left < right:
        # 3. 交换left，right的值
        word_list[left], word_list[right] = word_list[right], word_list[left]
        # 4. 更新left，right
        left, right = left + 1, right - 1

    return word_list


def revert_word(s):
    """
    单独翻转字符
    1. 把字符串转换为列表并去除空格
    2. 把字符串整体进行翻转，并在最后加上空格
    3. 生成left，right指针
    4. 遍历right
    5. 如果right的值为空格，翻转left到right的区间，并更新right为right+1，left为right
    6. 最后返回数组减去最后空格的字符
    """
    # 1. 把字符串转换为列表并去除空格
    word_list = trim_word(list(s))
    # 2. 把字符串整体进行翻转
    word_list = reverse_word(word_list) + [' ']
    # 3. 生成left，right指针
    left = 0
    # 4. 遍历right
    for right in range(len(word_list)):
        # 5. 如果right的值为空格，翻转left到right的区间，并更新right为right+1，left为right
        if word_list[right] == ' ':
            word_list[left: right] = reverse_word(word_list[left: right])
            right += 1
            left = right

    return ''.join(word_list[:-1])


if __name__ == '__main__':
    word = " the   sky is blue "
    print(revert_word(word))
