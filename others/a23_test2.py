#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a23_test2.py
@Time: 2020-04-26 14:00
@Last_update: 2020-04-26 14:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

poker_dict = {str(key+1): key+1 for key in range(10)}
poker_dict.update({'J': 11, 'Q': 12, 'K': 13})
poker_dict['1'] = 14
poker_dict['2'] = 15


def test2(input_str):
    """
    扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A，2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）:)
    3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
    输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格，如：4 4 4 4-joker JOKER
    请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR

    基本规则：
    （1）输入每手牌可能是个子，对子，顺子（连续5张），三个，炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
    （2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）
    （3）大小规则跟大家平时了解的常见规则相同，个子，对子，三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
    （4）输入的两手牌不会出现相等的情况。

    答案提示：
    （1）除了炸弹和对王之外，其他必须同类型比较。
    （2）输入已经保证合法性，不用检查输入是否是合法的牌。
    （3）输入的顺子已经经过从小到大排序，因此不用再排序了.
    整体流程：
    1. 分解两个手牌
    2. 判断是否有大小王
    3. 判断是否为一个是炸弹
    4. 判断是否长度相等
    5. 查找两个牌的牌面大小
    """
    # 1. 分解两个手牌
    poker1, poker2 = input_str.split('-')
    # 2. 判断是否有大小王
    if ('joker' in poker1) or ('joker' in poker2):
        return poker1 if 'joker' in poker1 else poker2

    poker1 = poker1.split(' ')
    poker2 = poker2.split(' ')
    # 3. 判断是否为一个是炸弹
    if ((len(poker1) == 4) or (len(poker2) == 4)) and (len(poker1) != poker2):
        return ' '.join(poker1) if len(poker1) == 4 else ' '.join(poker2)

    # 4. 判断是否长度相等
    if len(poker1) != len(poker2):
        return 'ERROR'

    return ' '.join(poker1) if poker_dict[poker1[0]] > poker_dict[poker2[0]] else ' '.join(poker2)


if __name__ == '__main__':
    input_str = '4-5'
    print(test2(input_str))