# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: num0208_Trie.py
@Time: 2020-04-28 22:15
@Last_update: 2020-04-28 22:15
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Trie:
    """
    实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
    你可以假设所有的输入都是由小写字母 a-z 构成的。
    保证所有输入均为非空字符串。
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // 返回 true
    trie.search("app");     // 返回 false
    trie.startsWith("app"); // 返回 true
    trie.insert("app");
    trie.search("app");     // 返回 true
    解法：
    使用字典，字典中再套字典
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_dict = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        tmp_dict = self.trie_dict
        for w in word:
            if w not in tmp_dict:
                tmp_dict[w] = dict()
            tmp_dict = tmp_dict[w]
        tmp_dict['#'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        tmp_dict = self.trie_dict
        for w in word:
            if w not in tmp_dict:
                return False
            tmp_dict = tmp_dict[w]

        if '#' in tmp_dict:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp_dict = self.trie_dict
        for w in prefix:
            if w not in tmp_dict:
                return False
            tmp_dict = tmp_dict[w]

        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
    print(trie.trie_dict)

