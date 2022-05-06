#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a7_str_split_and_match.py
@Time: 2020-04-24 12:16
@Last_update: 2020-04-24 12:16
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution(object):
    """
    输入为两个，首先要匹配的字符串，然后是带有固定格式的字符串，
    如果没有匹配的组，则输出"FAIL"，注意回车是"\r\n"
    """
    def str_split_and_match(self, target, inpu_str):
        """
        整体流程：
        1. 对字符串切分
        2. 去除空字符并把相应位置加上引号
        3. 进行字符名匹配
        4. 直接使用eval进行获取数值
        5. 生成结果返回
        """
        # 1. 对字符串切分
        input_str = inpu_str.strip()[:-1]
        str_list = input_str.split('],')
        rst_list = []
        # 2. 去除空字符并把相应位置加上引号
        for sub_str in str_list:
            sub_str = sub_str.strip()
            sub_key = sub_str.split('[')[0]
            if sub_key != target:
                continue

            sub_str = 'dict' + sub_str.replace(sub_key, '').replace(
                '[', '(').replace('=', '="').replace(',', '",') + '")'
            sub_dict = eval(sub_str)
            rst_list.append('%s %s %s\r\n' % (sub_dict['addr'], sub_dict['mask'], sub_dict['val']))

        # 5. 生成结果返回
        if len(rst_list) == 0:
            return 'FAIL'
        else:
            return ''.join(rst_list)


if __name__ == '__main__':
    target = 'read'
    input_str = 'read[addr=0x17,mask=0xff,val=0x7],read_his[addr=0xff,mask=0xff,val=0x1],read[addr=0xf0,mask=0xff,val=0x80]'
    print(Solution().str_split_and_match(target, input_str))