#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-07 00:11
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_14.py
# @Software: PyCharm

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        1、思路：遍历，两重循环: 一重第一个字符串，第二重每一个字符串
        注意边界条件的处理
        2、使用Python zip函数作为解压，zip：一个迭代对象的共同前缀、后缀
        :param strs:
        :return:
        """
        # s = ""
        # for i in zip(*strs):
        #     if len(set(i)) == 1:
        #         s+=i[0]
        #     else:
        #         break
        # return s

        if not strs:
            return ""

        prefix = strs[0]
        for i in range(len(prefix)):
            for test_str in strs[1:]:
                # 因为后边用到test_str[i], 判断是否超限
                if i >= len(test_str):
                    return prefix[:i]
                # 不相等
                if test_str[i] != prefix[i]:
                    return prefix[:i]
        # 全部相等时
        return prefix



if __name__ == '__main__':

    test_str = ["113", "224", "336"]
    for i in zip(*test_str):
        print(i)

