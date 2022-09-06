# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a76_revert_word.py
@Time: 2022-10-09 14:23
@Last_update: 2022-10-09 14:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def trim_word(_word_list):
    """
    使用双指针去除多余的空格
    1. 生成left，right指针
    2. 去除开头的空格，让right一直走到不是空格的字符
    3. 遍历right一直到结尾
    4. 如果right指代的数值不是空格则直接付给left，并left加一
    5. 如果right指代的数值是空格，但是left-1不是空格，也付给left，并left加一
    6. 如果right是空格，left当前也是空格，则跳过
    7. 去除结尾的空格，遍历left一直走到不是空格的字符
    """
    # 1. 生成left，right指针
    left, right = 0, 0
    # 2. 去除开头的空格，让right一直走到不是空格的字符
    while (right < len(_word_list)) and (_word_list[right] == ' '):
        right += 1
    # 3. 遍历right一直到结尾
    while right < len(_word_list):
        # 4. 如果right指代的数值不是空格则直接付给left，并left加一
        if _word_list[right] != ' ':
            _word_list[left] = _word_list[right]
            right += 1
            left += 1
            continue
        # 5. 如果right指代的数值是空格，但是left-1不是空格，也付给left，并left加一
        if (_word_list[right] == ' ') and (_word_list[left - 1] != ' '):
            _word_list[left] = _word_list[right]
            right += 1
            left += 1
            continue
        # 6. 如果right是空格，left当前也是空格，则跳过
        right += 1

    # 7. 去除结尾的空格，遍历left一直走到不是空格的字符
    left -= 1
    while left >= 0:
        if _word_list[left] != ' ':
            break
        left -= 1

    return _word_list[: left + 1]


def reverse_word(_word_list):
    """
    翻转字符串
    1. 创建left，right指针
    2. 遍历，条件为left<right
    3. 交换left，right的值
    4. 更新left，right
    """
    # 1. 创建left，right指针
    left, right = 0, len(_word_list) - 1
    # 2. 遍历，条件为left<right
    while left < right:
        # 3. 交换left，right的值
        _word_list[left], _word_list[right] = _word_list[right], _word_list[left]
        # 4. 更新left，right
        left += 1
        right -= 1

    return _word_list


def revert_word(_s):
    """
    翻转字符串
    1. 生成字符串列表
    2. 去除多余的空格
    3. 生成left指针，并在字符串列表最后加上一个空格
    4. 遍历字符串列表使用right指针
    5. 如果right指代的为空格，则翻转word_list[left:right]的字符串，并更新left
    6. 去除最后一个空格并整体翻转
    """
    # 1. 生成字符串列表
    word_list = list(s)
    # 2. 去除多余的空格
    word_list = trim_word(word_list)
    # 3. 生成left指针，并在字符串列表最后加上一个空格
    left = 0
    word_list += [' ']
    # 4. 遍历字符串列表使用right指针
    for right in range(len(word_list)):
        # 5. 如果right指代的为空格，则翻转word_list[left:right]的字符串，并更新left
        if word_list[right] == ' ':
            word_list[left: right] = reverse_word(word_list[left: right])
            left = right + 1

    # 6. 去除最后一个空格并整体翻转
    word_list = reverse_word(word_list[: -1])

    return ''.join(word_list)


if __name__ == '__main__':
    s = '  hello the   world!  '
    print(revert_word(s))
