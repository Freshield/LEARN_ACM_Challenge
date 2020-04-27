#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a22_test1.py
@Time: 2020-04-26 13:25
@Last_update: 2020-04-26 13:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def test1():
    """
    开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
    处理:
    1.记录最多8条错误记录，对相同的错误记录(即文件名称和行号完全匹配)只记录一条，错误计数增加；(文件所在的目录不同，文件名和行号相同也要合并)
    2.超过16个字符的文件名称，只记录文件的最后有效16个字符；(如果文件名不同，而只是文件名的后16个字符和行号相同，也不要合并)
    3.输入的文件可能带路径，记录文件名称不能带路径
    整体流程：
    1. 用列表记录错误记录名的出现顺序
    2. 用字典记录错误信息
    3. 如果字典没有则加到字典和列表
    4. 如果字典有则更新字典
    5. 最终输出
    """
    error_dict = dict()
    error_list = []
    while True:
        try:
            path, line = input().strip().split(' ')
            file_name = path.split('\\')[-1]
            key = '%s_%s' % (file_name, line)
            if key not in error_dict.keys():
                error_list.append(key)
                error_dict[key] = 1
            else:
                error_dict[key] += 1
        except Exception as e:
            break

    rst_list = ['%s_%s' % (key, value) for key, value in error_dict.items()]
    rst_list.sort(key=lambda x: int(x.split('_')[-1]) * 100000 - error_list.index('_'.join(x.split('_')[:2])), reverse=True)
    for i in range(min(len(rst_list), 8)):
        file_name, line, num = rst_list[i].split('_')
        file_name = file_name if len(file_name)<=16 else file_name[-16:]
        print_str = "%s %s %s" % (file_name, line, num)
        print(print_str)




if __name__ == '__main__':
    input_str = r'E:\V1R2\product\fpgadrive.c 1325'
    test1()
