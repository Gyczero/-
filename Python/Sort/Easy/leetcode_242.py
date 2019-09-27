#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-13 16:36
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_242.py
# @Software: PyCharm

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        思路1：排序，O(nlogN)
        思路2：Hash表
        :param s:
        :param t:
        :return:
        """
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    Solution().isAnagram("anagram", "nagaram")